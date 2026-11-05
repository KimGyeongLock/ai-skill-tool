# AI 업무형 과제 Codex 준비 키트 v4 (보이는 `agents/` 폴더)

공개 GitHub에서 가져올 수 있는 **범용 작업 지침**입니다. 정답이나 실제 시험 데이터를 포함하지 않습니다. 공식 과제 지침과 운영 규정이 항상 우선합니다.

## 변경 사항

- 숨김 폴더 `.agents/` 대신 **일반 폴더 `agents/skills/`**를 사용합니다. 파일 탐색기에서 찾기 쉽습니다.
- **짧은 프롬프트만으로 진행:** 상세 지침은 각 `SKILL.md`와 `AGENTS.md`에 포함했습니다.
- 검증에 **입력 근거, 중간값·단위, 정상·경계·실패 사례, 독립 검산, 목적함수·제약조건, 미확인 표시**를 명시했습니다.
- Codex 보고 형식은 **요약 → 체크리스트/표 → 실제 근거 → 미확인 및 다음 행동**입니다. `[x] 완료`, `[!] 실패`, `[?] 미확인`은 실제 검증 결과에 따라 사용합니다.
- 최적화가 필요하면 **유효 기준선 → 개선 전후 비교 → 하드 제약 재확인 → 검증된 결과 채택** 순서로 수행합니다.

## 파일 구조

```text
ai-skill-tool/
├── AGENTS.md
├── START_HERE.md
├── PROMPTS.md
├── CHECKLIST.md
├── WORKLOG_TEMPLATE.md
├── README.md
├── agents/skills/
│   ├── task-intake/SKILL.md
│   ├── task-build/SKILL.md
│   ├── task-optimize/SKILL.md
│   ├── task-verify/SKILL.md
│   ├── data-audit/SKILL.md
│   └── rule-analysis/SKILL.md
├── tools/install.py
└── tests/test_kit.py
```

## 사용 방법 (추가 설치 없이 읽기)

과제 파일과 다른 허용된 경로에 Clone합니다.

```bash
git clone https://github.com/KimGyeongLock/ai-skill-tool.git /tmp/ai-skill-tool
```

**위 GitHub 저장소에 v4를 직접 Push한 이후에 새 구조가 반영됩니다.** 본 ZIP을 받는 것만으로 GitHub 저장소가 바뀌지 않습니다.

Codex에 처음 입력할 문장:

```text
/tmp/ai-skill-tool/AGENTS.md와 /tmp/ai-skill-tool/agents/skills/task-intake/SKILL.md를 읽고 공식 과제 README를 분석해줘. 필수 제약, 목적함수, 담당자 질문, 구현·검증 계획을 체크리스트로 정리해. 아직 수정하지 마.
```

그다음은 `/tmp/ai-skill-tool/PROMPTS.md`의 **구현 → (필요하면 데이터/규정 분석과 최적화) → 최종 검증** 예시 중 필요한 문장만 사용하세요.

**중요:** `agents/skills/`는 보이는 일반 폴더입니다. Codex의 표준 자동 Skill 검색 경로인 `.agents/skills/`와 다르므로 **자동 발견이나 `$task-intake` 호출을 보장하지 않습니다.** 대신 위 예시처럼 `agents/skills/.../SKILL.md`를 **직접 읽게 하면 됩니다.** 원한다면 공식적으로 허용된 환경에서 별도 Skill 경로에 복사할 수 있지만 이 키트의 기본 사용법은 파일 직접 읽기입니다.

## 선택: 파일 복사 스크립트

```bash
# 실행 전 경로 및 허용 여부 확인
python3 /tmp/ai-skill-tool/tools/install.py --target .
python3 /tmp/ai-skill-tool/tools/install.py --target . --apply
```

과제 작업 폴더에 `agents/skills/`로 복사합니다. **이 또한 자동 Skill 등록을 의미하지 않습니다.** 과제 제출물에 포함될 수 있으므로 굳이 복사하지 않는 방법을 추천합니다. 파일 복사 전 미리보기(dry run)이고, 기존 파일은 덮어쓰지 않습니다. 외부 API, 모델 연결, Git Push, 감독 설정 우회는 하지 않습니다.

## 개인 GitHub 저장소 업데이트 (시험 외부 개인 컴퓨터에서만)

1. v4 ZIP을 압축 해제합니다.
2. 기존 `ai-skill-tool` 로컬 저장소의 변경사항을 확인합니다: `git status --short`.
3. v4 폴더의 **전체 파일과 `agents/skills/` 디렉터리**를 기존 저장소에 복사합니다. 다른 프로젝트 데이터는 복사하지 않습니다.
4. 아래 순서로 GitHub에 반영합니다.

```bash
git add -A
git diff --cached --stat
git commit -m "Simplify skill paths and improve verified reporting"
git push origin main
```

업로드한 뒤 GitHub에서 `agents/skills/task-verify/SKILL.md`를 열어 내용이 보이는지 확인하세요. Clone 중인 기존 디렉터리는 자동 갱신되지 않으므로 새 경로에서 다시 Clone하거나, 개인 준비 환경에서 Git pull을 확인하세요.

## 지켜야 할 점

- AI가 결과를 **가독성 있게** 보여주더라도 체크가 사실 여부를 보장하지는 않습니다. 실제 실행 명령과 관찰값이 근거입니다.
- 최적화가 목표가 아닌 과제에는 불필요한 튜닝을 강행하지 않습니다.
- 과제 파일이나 결과를 외부 저장소/API로 전송하지 않으며, 평가에서 AI가 금지된 단계에는 사용하지 않습니다.
- 공개 준비물의 이용 허용과 환경의 파일 쓰기/도구 실행 허용은 별도로 확인합니다.
