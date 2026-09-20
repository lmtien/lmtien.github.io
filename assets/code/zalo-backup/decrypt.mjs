import fs from 'node:fs';
import { createHash, createDecipheriv } from 'node:crypto';
import { pipeline } from 'node:stream/promises';

// Zalo Desktop V2 observed in September 2026. No account keys are included.
function credentials(file) {
  const uin = fs.readFileSync(file, 'utf8').replace(/\r?\n$/, '');
  if (uin.length !== 32) throw new Error('Expected the observed 32-character UIN');
  const key = createHash('sha256').update(uin, 'utf8').digest();
  const iv = Buffer.from('zie' + uin.slice(0, 13), 'utf8');
  if (iv.length !== 16) throw new Error('Expected a 16-byte IV');
  return { key, iv };
}

function verify(source, key, iv) {
  const size = fs.statSync(source).size;
  if (size < 512 || size % 16) throw new Error('Invalid size for this CBC format');
  const encrypted = Buffer.alloc(512);
  const fd = fs.openSync(source, 'r');
  try {
    if (fs.readSync(fd, encrypted, 0, 512, 0) !== 512) throw new Error('Short read');
  } finally { fs.closeSync(fd); }
  const decipher = createDecipheriv('aes-256-cbc', key, iv);
  decipher.setAutoPadding(false);
  const block = Buffer.concat([decipher.update(encrypted), decipher.final()]);
  const checksum = block.subarray(148, 156).toString('ascii').replace(/\0.*$/, '').trim();
  let sum = 0;
  for (let i = 0; i < 512; i++) sum += i >= 148 && i < 156 ? 32 : block[i];
  if (!/^[0-7]+$/.test(checksum) || parseInt(checksum, 8) !== sum ||
      block.subarray(257, 262).toString('ascii') !== 'ustar') {
    throw new Error('Invalid TAR header: wrong UIN, different format, or damaged file');
  }
  return block.subarray(0, 100).toString('utf8').replace(/\0.*$/, '');
}

async function main() {
  const [command, source, profile, destination, ...extra] = process.argv.slice(2);
  if (!['verify', 'decrypt'].includes(command) || !source || !profile || extra.length ||
      (command === 'decrypt' && !destination) || (command === 'verify' && destination)) {
    throw new Error('Usage: node decrypt.mjs verify SOURCE UIN_FILE | decrypt SOURCE UIN_FILE OUTPUT_TAR');
  }
  const { key, iv } = credentials(profile);
  const firstEntry = verify(source, key, iv);
  if (command === 'verify') {
    console.log('TAR header verified\nFirst entry: ' + firstEntry);
    return;
  }
  if (fs.existsSync(destination)) throw new Error('Destination already exists');
  const temporary = destination + '.partial';
  const fd = fs.openSync(temporary, 'wx', 0o600);
  try {
    await pipeline(
      fs.createReadStream(source),
      createDecipheriv('aes-256-cbc', key, iv),
      fs.createWriteStream(temporary, { fd }),
    );
    // Both names are in one directory; linking publishes without overwriting.
    fs.linkSync(temporary, destination);
    fs.unlinkSync(temporary);
    console.log('Decrypted; inspect the TAR before extraction.');
  } catch (error) {
    console.error('Unpublished partial output: ' + temporary);
    throw error;
  }
}

main().catch(error => { console.error(error.message); process.exitCode = 1; });
