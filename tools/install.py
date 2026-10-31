#!/usr/bin/env python3
"""Copy selected local Codex skills without overwriting existing project files.

This helper performs no network calls, installation of packages, Git commands,
model changes, or modifications outside the explicitly selected target directory.
Dry-run is the default; use --apply to copy files.
"""

import argparse
import shutil
import sys
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = KIT_ROOT / ".agents" / "skills"
DEFAULT_SKILLS = ["task-intake", "task-build", "task-verify"]
ALL_SKILLS = ["task-intake", "task-build", "task-verify", "data-audit", "rule-analysis"]


def main():
    parser = argparse.ArgumentParser(description="범용 Codex Skill을 지정한 과제 폴더에 안전하게 복사합니다.")
    parser.add_argument("--target", default=".", help="기존 과제 루트 (기본값: 현재 디렉터리)")
    parser.add_argument("--skills", nargs="+", choices=ALL_SKILLS, default=DEFAULT_SKILLS,
                        help="가져올 Skill 이름 (기본: task-intake, task-build, task-verify)")
    parser.add_argument("--include-agents", action="store_true",
                        help="AGENTS.md가 없을 때에만 추가 (기본: 복사 안 함)")
    parser.add_argument("--apply", action="store_true", help="실제로 복사 (생략 시 변경 없는 미리보기)")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    if not target.is_dir():
        parser.error(f"대상 폴더가 존재하지 않습니다: {target}")
    if target == KIT_ROOT or KIT_ROOT in target.parents:
        parser.error("키트 자체를 과제 작업 공간으로 지정할 수 없습니다.")

    mode = "실제 복사" if args.apply else "미리보기 (파일 변경 없음)"
    print(f"모드: {mode}\n과제 위치: {target}")
    operations = [(SKILL_ROOT / skill, target / ".agents" / "skills" / skill)
                  for skill in dict.fromkeys(args.skills)]
    if args.include_agents:
        operations.append((KIT_ROOT / "AGENTS.md", target / "AGENTS.md"))

    failures = 0
    for source, dest in operations:
        if not source.exists():
            print(f"[오류] 원본 없음: {source}")
            failures += 1
            continue
        if dest.exists() or dest.is_symlink():
            print(f"[건너뜀] 이미 존재함, 덮어쓰지 않음: {dest}")
            continue
        if not args.apply:
            print(f"[예정] {source.relative_to(KIT_ROOT)} -> {dest}")
            continue
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir():
                shutil.copytree(source, dest)
            else:
                shutil.copy2(source, dest)
            print(f"[완료] {source.name} -> {dest}")
        except OSError as exc:
            failures += 1
            print(f"[오류] 복사 실패: {dest} ({exc})")

    if not args.apply:
        print("실제 복사를 원하면 확인 후 --apply 옵션을 붙이세요.")
    if failures:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
