# 설득 엔진 입출력 JSON 스키마 (v1.1)

공통: UTF-8 JSON 파일 하나를 `--input`으로 넘깁니다. 출력은 표준출력 JSON입니다.
종료 코드: 0 = 정상(PASS·REVISE·OK·analyze), 2 = 차단(check BLOCK 또는 plan BLOCKED), 1 = 입력 오류.

## 공통 타입

### Fact (팩트)
| 필드 | 타입 | 필수 | 뜻 |
|---|---|---|---|
| claim | string | 예 | 사실 문장. 숫자는 그대로 적습니다(숫자 근거 대조 F1에 쓰임) |
| source | string | 예 | 출처. 비어 있으면 검증 안 된 것으로 봅니다 |
| verified | bool | 예 | 사람이 확인했는지. `true` + `source` 있음 = 검증 팩트 |
| kind | enum | 권장 | `outcome_data` `statistic` `credential` `real_limit` `favor` `shared_identity` `shared_trait` `commitment` `reason` `alternative` `comparison` |

`kind` 별로 쓸 수 있는 원칙이 정해집니다(Tactic -requires-> Fact). 예: 희귀성은 `real_limit`가, 권위는 `credential`이 있어야 합니다.

### Cue (LLM이 뽑은 단서, 선택)
```json
{"principle": "authority | principle.cialdini_authority", "tendency": "#22 | concept.munger_t22_authority", "evidence": "입력 text 안에 실제로 있는 구절"}
```
엔진은 R0 규칙으로 검증합니다. KB에 없는 id → 거절, evidence가 text에 없음 → '환각' 거절.

### domain
`hospital_consult` `device_sales` `politics` `staff` `investment` `general`(기본)

## analyze (방어 모드) 입력
```json
{"text": "분석할 문장(필수)", "domain": "general", "facts": [Fact], "cues": [Cue]}
```
출력 주요 필드
- `principles[]`: `{id, name, fact_backed, evidence[]}` 탐지된 치알디니 원칙
- `tendencies[]`: `{id, number, name}` 활성화된 멍거 경향(직접 단서 + Principle-triggers->Tendency)
- `mass_hooks{}`: 대중 반응 고리(싸움 구경·남 안 되는 것·새로운 것·남 탓·밴드왜건) → 매칭 단어
- `combos[]`: `{id, name, valence, matched[], broken_by[]}` 롤라팔루자 조합
- `amplifications[]`: Tendency-amplifies->Tendency 연결
- `signals[]`: 윤리 신호(M1–M10) 매칭
- `lollapalooza`: `{score 0–100, level 낮음|주의|높음, suspected, tendency_count, fact_backed_tendencies, advice}`
- `defenses[]`: `{id, name, how}` 추천 방어 도구(최대 6)
- `llm_cues`: `{accepted, rejected[{cue, reason}]}`
- `research_flags[] {rule, id, level(info|warn|block|ok), grade, label, match, note, sources[]}`: 심층연구 규칙(WIKI-CODE-022) 탐지. info 단서는 위험 점수에 넣지 않음
- `rules_fired[]`: 발화한 규칙. PDF 규칙(R0–R7)은 끝에 `[근거: PDF 「설득과 오판」]`, 연구 규칙은 `rule.pr_<id> [근거 A/B] 설명 — 메모 (출처: ID…)`

## check (윤리 점검) 입력
```json
{"text": "점검할 초안(필수)", "domain": "hospital_consult", "facts": [Fact],
 "techniques": ["선택: 쓰려는 기법 이름·id"], "ai_generated": false, "optimized": false, "accuracy_rechecked": false,
 "conflict_of_interest": false, "persona_verified": true}
```
출력: `verdict` (BLOCK | REVISE | PASS), `issues[] {code, level(block|warn), name, match}`, `persuader_type` (밀수꾼|탐정|중립), `facts{verified, unverified}`, `lollapalooza`, `external_send`, 그리고 v1.1: `info_flags[]`(판정에 영향 없는 단서), `suggestions[]`(BYAF 등, 판정 불변), `tares{truthfulness, authenticity, respect, equity, social_responsibility}`, `mastery{level 하수|중수|고수, how, result, why, maxim}`, `rules_fired[]`.
연구 규칙 코드(issues.code에 원본 id, `grade`·`rule_id` 포함): `dp.*` 다크패턴 7종(block), `man.*` 조작(사칭·동의 우회 block, 이해상충·반복·TARES·경향 3개 이상 warn), `ban.*` D등급·과장 주장, `fact.*` 출처·AI 공개·정확도 재검사·양면 제시, `cue.*` warn 단서(공포만·사례만·외집단 적대·AI 대량 수치).
mastery: F0 → 하수, PASS → 고수, 그 밖 → 중수.
코드: M1 가짜 희귀성, M2 조작된 사회적 증거, M3 약점 압박, M4 수익·원금 보장, M5 투자 권유, M6 자격 부풀리기, M7 대조 착시, M8 즉석 결정 요구, M9 가짜 '우리'(영업 맥락), M10 근거 없는 남 탓 / F0 팩트 0개인데 설득 단서 있음, F1 팩트에 없는 숫자 / H1 대안 없음, H2 이유 없음, H3 결정 시간 없음(진료 상담).
같은 종류의 검증 팩트가 있으면 해당 M 신호는 통과합니다(예: 실제 재고 `real_limit` → M1 해제). 부정문("지금 결정하실 필요는 없습니다")은 신호에서 뺍니다.

## plan (공격 모드) 입력
```json
{"goal": "설득 목표(필수)", "domain": "staff",
 "audience": {"involvement": "high|low|unknown", "role": "청중",
   "prior_attitude": "opposed|undecided|supportive|unknown", "identity_threat": "high|low", "state": "ambivalent|hesitant|",
   "culture": "collectivist(기본)|individualist", "goal_type": "behavior|attitude(생략 시 목표 문장에서 추정)", "timing": "late|", "proposal": ""},
 "techniques": ["선택: 쓰려는 기법(D등급이면 차단 목록으로)"], "ai_generated": false,
 "facts": [Fact], "draft": "선택: 초안이 있으면 check까지 함께 실행"}
```
출력
- 차단 시: `status: BLOCKED`, `gate: ethics|fact`, `quadrant: 사기꾼`(팩트 게이트), `reason`, `required_facts[] {kind, need}`, `unverified_facts[]`, `next_step`
- 통과 시: `status: OK`, `quadrant: 리더|학자형`, `elm {involvement, route 중심 경로|주변 경로|혼합, guidance}`, `principle_combo[] {id, name, how, fact[]}`, `on_hold[] {id, name, missing_fact[]}`, `message_order[] {step, part logos|ethos|pathos, weight, content[], rule}`, `forbidden_tactics[]`, `warnings[]`, `draft_check`(draft가 있을 때), v1.1: `strategy{goal_type, audience, selected_rules[], prefer[] {technique, name, grade, by}, avoid[], blocked_techniques[], behavior_sequence[](행동 목표), byaf{recommended, phrase, why}, opinion_only[](출처 없는 팩트), notes[]}`, `mastery`, `rules_fired[]`

게이트 순서: ① 윤리 게이트(domain=investment 또는 목표·초안에 M4/M5) → ② 팩트 게이트(검증 팩트 0개 = 사기꾼, 계획 없음) → ③ ELM → ④ 원칙 선택(팩트 없는 원칙은 on_hold) → ⑤ 순서·금지 기법.
