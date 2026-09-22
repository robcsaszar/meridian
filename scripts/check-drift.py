#!/usr/bin/env python3
"""Detect whether the origin project has moved since these files were vendored.

Direction of travel is origin -> plugin. The vendored copies are deliberately
different (namespaced, decoupled), so this never compares them to each other.
It compares the ORIGIN against the fingerprint taken when we vendored, and
tells you what to re-port.

  RUTTER_ORIGIN=/path/to/origin/.claude python3 scripts/check-drift.py
  python3 scripts/check-drift.py --update    # re-fingerprint after porting
"""
import hashlib, json, io, os, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAN = os.path.join(ROOT, '.vendor-manifest.json')

def norm_sha(path):
    return hashlib.sha256(io.open(path, 'rb').read().replace(b'\r\n', b'\n')).hexdigest()

def main():
    man = json.load(io.open(MAN, encoding='utf-8'))
    origin = os.environ.get('RUTTER_ORIGIN', man.get('origin_default', ''))
    update = '--update' in sys.argv

    if not origin or not os.path.isdir(origin):
        print(f"drift: origin not available at {origin!r} - skipping.")
        print("       Set RUTTER_ORIGIN to check, or ignore where the origin is not cloned.")
        return 0

    moved, gone = [], []
    for here, rec in sorted(man['files'].items()):
        src = os.path.join(origin, rec['origin'].replace('/', os.sep))
        if not os.path.exists(src):
            gone.append((here, rec['origin'])); continue
        now = norm_sha(src)
        if now != rec['origin_sha256']:
            moved.append((here, rec['origin'], now))

    if not moved and not gone:
        print(f"drift: clean - origin unchanged since {man['vendored_at']} ({len(man['files'])} files)")
        return 0

    if update:
        for here, _, now in moved:
            man['files'][here]['origin_sha256'] = now
        man['vendored_at'] = datetime.date.today().isoformat()
        io.open(MAN, 'w', encoding='utf-8', newline='').write(json.dumps(man, indent=2) + "\n")
        print(f"drift: re-fingerprinted {len(moved)} file(s). Port the changes before trusting this.")
        return 0

    print("drift: ORIGIN HAS MOVED since these files were vendored.")
    print("       Direction of travel is origin -> plugin: review each change and port what applies,")
    print("       then re-run with --update to re-fingerprint.\n")
    for here, there, _ in moved:
        print(f"  changed at origin   {there}")
        print(f"    vendored here as  {here}")
    for here, there in gone:
        print(f"  MISSING at origin   {there}  (vendored here as {here})")
    return 1

if __name__ == '__main__':
    sys.exit(main())
