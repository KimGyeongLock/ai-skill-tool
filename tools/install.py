#!/usr/bin/env python3
"""Local copy-only installer. Dry-run default; no network, git, model changes."""
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'agents' / 'skills'
KNOWN = ('task-intake', 'task-build', 'task-optimize', 'task-verify', 'data-audit', 'rule-analysis')
DEFAULT = ('task-intake', 'task-build', 'task-optimize', 'task-verify')


def main():
    p = argparse.ArgumentParser(description='Selectively copy Codex skills without overwriting')
    p.add_argument('--target', default='.', help='existing task root')
    p.add_argument('--skills', nargs='+', choices=KNOWN, default=DEFAULT)
    p.add_argument('--include-agents', action='store_true', help='copy AGENTS.md only if absent')
    p.add_argument('--apply', action='store_true', help='copy instead of dry run')
    a = p.parse_args()
    target = Path(a.target).expanduser().resolve()
    if not target.is_dir():
        p.error('Target directory does not exist')
    if target == ROOT or ROOT in target.parents:
        p.error('Cannot install into own kit root or descendants')

    jobs = [(SOURCE / name, target / 'agents' / 'skills' / name) for name in dict.fromkeys(a.skills)]
    if a.include_agents:
        jobs.append((ROOT / 'AGENTS.md', target / 'AGENTS.md'))
    errors = 0
    print('MODE:', 'APPLY' if a.apply else 'DRY RUN', 'TARGET:', target)
    for src, dst in jobs:
        if not src.exists():
            print('ERROR missing source:', src)
            errors += 1
        elif dst.exists() or dst.is_symlink():
            print('SKIP existing:', dst)
        elif not a.apply:
            print('PLAN:', src.relative_to(ROOT), '->', dst)
        else:
            try:
                dst.parent.mkdir(parents=True, exist_ok=True)
                if src.is_dir():
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)
                print('DONE:', dst)
            except OSError as e:
                print('ERROR:', str(e))
                errors += 1
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
