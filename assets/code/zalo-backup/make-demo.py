"""Generate synthetic input for the accompanying public blog post. No real data."""
import io
import json
import pathlib
import subprocess
import tarfile

uin = '0123456789abcdef0123456789abcdef'
uid = '9000000000000000001'
peer = '9000000000000000002'
outputs = [pathlib.Path(name) for name in ['demo.tar', 'demo-uin.txt', 'demo.zl.zip']]
if any(path.exists() for path in outputs):
    raise SystemExit('Demo output already exists. Use a new empty directory.')

messages = [
    {'msgId': 'demo-1', 'fromUid': '0', 'toUid': peer,
     'serverTime': 1700000000000, 'message': 'Coffee tomorrow?'},
    {'msgId': 'demo-2', 'fromUid': peer, 'toUid': '0',
     'serverTime': 1700000060000, 'message': 'Yes, see you at ten.'},
]
payload = ''.join(json.dumps(record) + '\n' for record in messages).encode('utf-8')
with outputs[0].open('xb') as stream:
    with tarfile.open(fileobj=stream, mode='w', format=tarfile.USTAR_FORMAT) as archive:
        entry = tarfile.TarInfo(f'{uid}/ZaloDownloads/database/{uid}_zmessage.zdb')
        entry.size = len(payload)
        entry.mode = 0o600
        entry.mtime = 0
        archive.addfile(entry, io.BytesIO(payload))
with outputs[1].open('x') as stream:
    outputs[1].chmod(0o600)
    stream.write(uin + '\n')

subprocess.run(['node', '--input-type=module', '-e', r'''
import fs from 'node:fs';
import { createHash, createCipheriv } from 'node:crypto';
import { pipeline } from 'node:stream/promises';
const uin = fs.readFileSync('demo-uin.txt', 'utf8').trim();
const key = createHash('sha256').update(uin).digest();
const iv = Buffer.from('zie' + uin.slice(0, 13));
await pipeline(fs.createReadStream('demo.tar'), createCipheriv('aes-256-cbc', key, iv),
  fs.createWriteStream('demo.zl.zip', { flags: 'wx', mode: 0o600 }));
'''], check=True)
print('Created demo.tar, demo.zl.zip and demo-uin.txt using invented data.')
