"""Inspect an uncompressed TAR, then extract regular files into a new directory."""
import argparse
import math
import pathlib
import re
import shutil
import tarfile

parser = argparse.ArgumentParser()
parser.add_argument('archive')
parser.add_argument('destination')
parser.add_argument('max_gib', type=float, help='Maximum declared extracted file bytes in GiB')
args = parser.parse_args()
if not math.isfinite(args.max_gib) or args.max_gib <= 0:
    parser.error('max_gib must be finite and positive')

limit = args.max_gib * 1024**3
seen = set()
total = 0
with tarfile.open(args.archive, 'r:') as archive:
    for entry in archive:
        path = pathlib.PurePosixPath(entry.name)
        if (path.is_absolute() or '..' in path.parts or '\\' in entry.name
                or re.match(r'^[A-Za-z]:', entry.name) or '\x00' in entry.name
                or str(path) == '.' or str(path) in seen):
            raise ValueError('Unsafe or duplicate path: ' + repr(entry.name))
        if not (entry.isfile() or entry.isdir()):
            raise ValueError('Links and special files are not supported')
        seen.add(str(path))
        total += entry.size
        if total > limit or len(seen) > 100000:
            raise ValueError('Archive exceeds byte or entry limit')

output = pathlib.Path(args.destination)
output.mkdir(mode=0o700, exist_ok=False)
root = output.resolve()
with tarfile.open(args.archive, 'r:') as archive:
    for entry in archive:
        target = root / entry.name
        if not target.resolve().is_relative_to(root):
            raise ValueError('Path escapes destination')
        if entry.isdir():
            target.mkdir(mode=0o700, parents=True, exist_ok=True)
        else:
            target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            with archive.extractfile(entry) as src, target.open('xb') as dst:
                target.chmod(0o600)
                shutil.copyfileobj(src, dst, 1024 * 1024)
            if target.stat().st_size != entry.size:
                raise ValueError('Extracted size mismatch')
print(f'Extracted {len(seen)} entries, {total} file-content bytes.')
