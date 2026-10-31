# AI Hackathon Codex Kit

낯선 업무형 과제를 제공된 Codex로 분석, 구현, 검증할 때 사용하는 **개인용 공개 준비 키트**입니다.

- **정답이나 예상문제는 없습니다.** AI에게 일을 시키는 지침, 선택형 Skill, 문서 양식만 들어 있습니다.
- **MCP 서버는 포함하지 않습니다.** 내장 터미널과 파일 기능으로 시작하고, 필요한 MCP만 별도로 검토합니다.
- **검증 5단계:** 원문·입력 추출 → 핵심 중간값·근거 → 다른 방식의 검산 → 확인 여부 표기 → 원래 요구사항과 대조. 시작 프롬프트는 짧고 세부 규칙은 Skill과 AGENTS.md에 둡니다.
- **외부 AI, 개인 API 키, 외부 전송, 자동 배포, Git Push를 실행하지 않습니다.**
- 참가자들의 공개 하네스에서 보편적인 접근법(요구사항 정의, 인터뷰, 작은 구현, 독립 검증, 결정 기록)을 참고해 새로 작성한 범용 지침입니다.

> **가장 중요한 원칙:** 시험장에서는 실제 제공된 과제 설명과 최신 운영 규정이 이 키트보다 우선합니다. 공개 저장소 Clone이 허용되더라도 모든 외부 통신이나 설정 변경이 허용되는 것은 아닙니다.

## 파일 구성

```text
hynix-codex-kit/
├── README.md                        이 안내서
├── START_HERE.md                    시작할 때 복사할 첫 프롬프트
├── PROMPTS.md                       구현, 질문, 검증, 인계용 복사 프롬프트
├── AGENTS.md                        Codex에 적용할 범용 작업 원칙
├── CHECKLIST.md                     시작과 제출 전 체크리스트
├── WORKLOG_TEMPLATE.md              판단과 검증 결과 기록 양식
├── .agents/skills/
│   ├── task-intake/SKILL.md          문제 파악과 질문 정리
│   ├── task-build/SKILL.md           최소 동작 결과물 구현
│   ├── task-verify/SKILL.md          독립 검증과 반례 확인
│   ├── data-audit/SKILL.md           CSV, JSON 등 데이터 검토 (선택)
│   └── rule-analysis/SKILL.md        업무 규정과 판정 로직 분석 (선택)
└── tools/install.py                 선택한 Skill을 안전하게 복사 (선택)
```

## 1. 시험 전: 내 GitHub 저장소에 올리기

1. 압축파일을 풀어 `hynix-codex-kit` 폴더를 만듭니다.
2. GitHub에서 **빈 Public 저장소**를 만듭니다(예: `hynix-codex-kit`). README 자동 생성은 생략합니다.
3. 내 컴퓨터 터미널에서 폴더로 이동한 뒤 아래를 실행합니다. `YOUR_ID`를 본인 계정으로 바꿉니다.

```bash
cd /압축해제한/경로/hynix-codex-kit
git init
git add .
git commit -m "Add reusable Codex workflow skills"
git branch -M main
git remote add origin https://github.com/YOUR_ID/hynix-codex-kit.git
git push -u origin main
```

**위 Push 명령은 대회 시작 전 개인 PC에서 공개 준비물을 게시할 때만 사용합니다. 시험 과제 파일, 문제 내용, 시험 결과는 공개 저장소에 올리지 않습니다.** 이미 Git 저장소라면 `git init`이나 `remote add`를 반복하지 마세요.

## 2. 시험장에서 사용하는 방법: 가장 간단한 방식 (설치 불필요)

공개 GitHub 접근이 실제로 허용된 경우, **과제 폴더와 별도 위치**에 이 준비물을 가져옵니다. 아래 `/tmp`는 예시 경로이며, 제공 환경에서 허용된 디렉터리로 바꿉니다.

```bash
git clone https://github.com/YOUR_ID/hynix-codex-kit.git /tmp/hynix-codex-kit
cat /tmp/hynix-codex-kit/START_HERE.md
```

`START_HERE.md`의 첫 프롬프트를 **제공된 Codex 채팅에 복사**하면 됩니다. 이 단계에서 Skill 자동 등록은 필요하지 않습니다. `cat`은 터미널 명령이고, 프롬프트는 Codex 채팅에 넣는 문장입니다.

경로 접근이 제한되면 무리하게 변경하거나 우회하지 말고, 미리 익혀 둔 핵심 문장("요구사항, 질문, 완료 기준, 구현 순서, 검증")을 직접 입력하세요.

## 3. Skill로 쓰는 방법 (선택)

**과제 루트**에서 아래를 실행하기 전에 `pwd`, `ls`, `git status`로 위치와 기존 파일을 확인하세요. 예시의 `/tmp/hynix-codex-kit`은 실제 키트 위치로 변경합니다.

```bash
# 먼저 실제 복사 계획만 출력합니다. 파일은 변경하지 않습니다.
python3 /tmp/hynix-codex-kit/tools/install.py --target .

# 승인된 작업 공간에 기본 Skill 3개만 복사합니다.
python3 /tmp/hynix-codex-kit/tools/install.py --target . --apply

# 데이터 또는 규정 과제라면 해당 Skill을 추가로 복사할 수 있습니다.
python3 /tmp/hynix-codex-kit/tools/install.py --target . --skills data-audit rule-analysis --apply
```

설치 스크립트는 **기존 파일을 덮어쓰지 않습니다.** 과제에서 제공한 `AGENTS.md`도 기본적으로 건드리지 않습니다.

- Skill 인식 여부를 제공된 Codex의 `/skills` 또는 지원되는 Skill 목록에서 확인합니다.
- 보이는 경우: `$task-intake 를 사용해서 과제를 분석해줘.`
- 안 보이면: `과제 루트의 .agents/skills/task-intake/SKILL.md를 읽고 적용해줘.`
- 새 세션에서만 보일 수 있습니다. 제공된 환경이 지원하지 않으면 채팅 프롬프트 방식만 써도 됩니다.
- `AGENTS.md` 적용이 필요하면 설치 전에 규정을 확인하고, 새 과제 루트에 기존 파일이 없을 때만 `--include-agents --apply`로 복사합니다. **기존 AGENTS.md가 있으면 덮어쓰지 말고 필요한 원칙만 수동으로 검토하세요.** Codex는 보통 프로젝트 루트의 AGENTS.md를 세션 시작 시 읽습니다.

> **주의:** `.agents/skills/`에 복사한 파일이 제출물이나 Git 상태에 포함될 수 있습니다. 과제 제출 규칙을 확인하고, 불필요하면 설치하지 않은 채 `START_HERE.md`의 채팅 문구만 사용하세요. 외부 파일 설치나 변경이 허용되지 않으면 설치하지 않습니다.

## 4. 실제 과제 진행 순서

| 시점 | 사용할 것 | 기대 결과 |
|---|---|---|
| 과제 직후 | `START_HERE.md`, `task-intake` | 필수 요구, 우선 질문, 최소 완성 기준 |
| 담당자 답변 후 | `PROMPTS.md`의 답변 반영 문구 | 확정된 규칙, 바뀐 구현 계획 |
| 구현 시작 | `task-build` | 실행되는 최소 결과물, 단계별 검증 |
| 데이터 과제인 경우 | `data-audit` | 스키마, 결측, 중복, 이상치, 집계 검증 |
| 규정 및 판정 과제인 경우 | `rule-analysis` | 조항별 판정 근거, 경계값 테스트 |
| 제출 직전 | `task-verify`, `CHECKLIST.md` | 입력 근거와 중간값, 독립 검산, 확정 상태, 요구사항 대조 |

## 5. 반드시 구분할 것

- **Git Clone:** 저장소 파일을 내려받는 작업. Skill 설치나 MCP 연결이 자동으로 되지 않습니다.
- **AGENTS.md:** Codex가 해당 프로젝트에서 지켜야 할 기본 규칙.
- **SKILL.md:** 특정 상황에 선택해 적용하는 반복 작업 지침.
- **MCP:** 별도의 도구 또는 서버 연결. 이 키트에서는 불필요하므로 설정하지 않습니다.
- **WORKLOG_TEMPLATE.md:** 의사결정과 검증 증거를 남기는 빈 양식. 작업 중 스스로 이해한 내용을 기록하되, AI 사용 금지 단계에 AI로 답을 작성하지 않습니다.

## 참고 자료

- Codex Skill 작성: https://learn.chatgpt.com/docs/build-skills
- Codex AGENTS.md: https://learn.chatgpt.com/docs/agent-configuration/agents-md
- 참가자 공개 참고: https://github.com/hamjoon2003/sk-hynix-2nd-harness
- 참가자 공개 참고: https://github.com/B0neh3ad/cofa-toolkit
- 참가자 공개 참고: https://github.com/chichochoi/sk

각 저장소의 준비 방식은 참고했지만 이 키트는 해당 프로젝트를 그대로 복사한 것이 아닙니다. 실제 시험에서 특정 점수나 설치 성공을 보장하지 않습니다.
