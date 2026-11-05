# Codex에 그대로 붙여넣는 짧은 프롬프트

> 기준: `git clone https://github.com/KimGyeongLock/ai-skill-tool.git /tmp/ai-skill-tool` 완료. 아래 경로가 다르면 실제 Clone 경로로 바꾸세요. 같은 Codex 세션에서 계속 진행한다면 이전 분석 결과를 이어서 참고할 수 있습니다.

## 1. 처음 과제 분석 (한 번)

```text
/tmp/ai-skill-tool/AGENTS.md와 /tmp/ai-skill-tool/agents/skills/task-intake/SKILL.md를 읽고 현재 과제를 분석해줘. 공식 근거, 필수 제약, 목적함수, 담당자 질문, 구현 순서와 검증 계획을 체크리스트로 정리해. 아직 수정하지 마.
```

## 2. 담당자 답변을 받았다면 (해당할 때만)

```text
담당자 실제 답변: [받은 답변]. 확정/미확정 조건과 계획에 반영하고 바뀐 부분만 체크해줘. 없는 답변을 만들지 마.
```

## 3. 구현

```text
/tmp/ai-skill-tool/agents/skills/task-build/SKILL.md를 읽고 앞서 분석한 요구사항에 따라 구현해줘. 기능별 실행과 테스트 결과를 체크리스트로 보여줘.
```

## 4. 데이터 분석이 필요할 때

```text
/tmp/ai-skill-tool/agents/skills/data-audit/SKILL.md를 읽고 실제 데이터를 분석하고 검산해줘. 핵심 건수·근거와 미확인 사항만 정리해줘.
```

## 5. 규정/문서 분석이 필요할 때

```text
/tmp/ai-skill-tool/agents/skills/rule-analysis/SKILL.md를 읽고 원문 근거로 조건과 예외를 분석해줘. 애매한 항목은 질문으로 분리해줘.
```

## 6. 최적화 목표가 있을 때 (유효 결과 확보 후)

```text
/tmp/ai-skill-tool/agents/skills/task-optimize/SKILL.md를 읽고 현재 결과를 기준선으로 보존한 뒤 최적화해줘. 개선 전후 지표와 제약 검증을 표로 보여줘.
```

## 7. 최종 검증 (끝날 때 반드시)

```text
/tmp/ai-skill-tool/agents/skills/task-verify/SKILL.md를 읽고 최종 결과를 독립 검증해줘. 요구사항별 체크리스트와 미확인·실패 항목을 보여줘.
```

**검증 단계 상세 지침은 `task-verify/SKILL.md` 안에 이미 포함되어 있습니다.** 입력 근거, 핵심 중간값, 정상·경계·실패 사례, 다른 방법의 검산, 목적함수와 제약조건, 미확인 표시, 제출 차단 문제까지 자동으로 점검하도록 작성했습니다. 긴 문장을 외우지 않아도 됩니다.

## 8. 실제 작업의 AI 판단 기록 (AI 사용 허용 단계에만)

```text
WORKLOG_TEMPLATE.md 형식으로 실제 AI 제안, 내 수용/수정/거절 판단과 이유, 실행 근거, 한계를 정리해줘. 지어내지 마.
```

## 9. 새 세션을 열었다면

```text
/tmp/ai-skill-tool/AGENTS.md와 현재 공식 README, 작업 기록을 다시 읽어줘. 확정 조건과 변경된 파일, 실제 테스트 결과를 확인한 다음 이어가자.
```

**주의:** 과제에서 AI 사용이 금지된 단계에서는 사용하지 않습니다. 외부 전송이나 Git Push는 하지 않습니다.
