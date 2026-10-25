# NDB 설득 스킬 (ndb-persuasion-skill)

**팩트 위에 세우는 설득.** 설득 메시지를 만들거나(진료 상담·직원·협력·정치 메시지), 받은 광고·영업·투자 권유에 휘말리는지 점검할 때 쓰는 에이전트 스킬과 설득 온톨로지, 뉴로심볼릭 엔진, 심층보고서 「NDB 설득의 심리학」을 한곳에 모은 공개 저장소입니다.

> 최상위 원칙: 팩트 없는 설득은 사기꾼, 팩트 위의 설득은 리더(사업가·학자·정치인). "사실은 엔진, 심리는 변속기."

## 무엇을 하나
- **방어(analyze)**: 받은 문구에 어떤 설득 원칙과 오판 경향이 겹쳤는지(롤라팔루자) 찾고 위험 점수를 냅니다.
- **계획(plan)**: 검증된 팩트로 청중 상태별 전략, logos→ethos→pathos 순서, 행동 목표면 BYAF·실행 계획 순서를 짭니다. 검증 팩트가 0개면 계획을 만들지 않습니다.
- **윤리 점검(check)**: 가짜 희귀성, 조작된 사회적 증거, 공포 압박, 설명 동의 건너뛰기, 다크패턴 7종, 투자·수익 보장 문구를 찾아 BLOCK/WARN/PASS를 냅니다.

## 프레임워크
- **치알디니 7+1 원칙**(상호성·일관성·사회적 증거·호감·권위·희귀성·연대감 + 초전 설득) × **멍거 오판의 25경향**(롤라팔루자 포함)
- **근거 등급 A~D**: 출처 149편(sources.csv)을 등급화. D등급(재현 실패: 자아 고갈, 행동·돈 점화, "정정하면 역효과")은 추천하지 않습니다.
- **심층연구 규칙 50개**: 탐지·청중 전략·조작 탐지·다크패턴·금지 기법·팩트 규칙. 엔진 출력에 근거 등급이 붙습니다.
- **뉴로심볼릭 엔진**: 신경 계층(LLM)이 문장에서 단서를 뽑고 초안을 쓰면, 기호 계층(이 엔진, 파이썬 표준 라이브러리만)이 단서를 검증하고 규칙을 발화하며 팩트·윤리 게이트로 차단합니다.
- **윤리·의료법 점검**: 설명 동의(제24조의2), 치료경험담 광고 금지·비교/과장/중요정보 누락 금지·비급여 할인 광고 금지(제56조), 의료광고 심의(제57조), 비급여 진료비용 고지(제45조), 환자 유인 금지(제27조 제3항).

## 구조
```
SKILL.md        에이전트 스킬 정의 (/persuasion)
ontology/       설득 온톨로지 위키 (entities/ 개체 220개, notes/ 허브 WIKI-CODE-020·021·022)
engine/         뉴로심볼릭 엔진 (engine.py, rules_ext.py, knowledge.json, build_kb.py, tools/, examples/, tests/)
research/       심층연구 자료 (dossier.md, sources.csv, ontology_additions.json, engine_rules_additions.json)
report/         「NDB 설득의 심리학」 심층보고서 (HTML 원본, PDF, figures/)
CHANGELOG.md    변경 기록
```

## 사용법
파이썬 3.10 이상, 외부 패키지 없음.

```bash
cd engine
python3 engine.py analyze --input examples/device_sales.json      # 방어 분석
python3 engine.py plan    --input examples/plan_consult_facts.json # 설득 계획
python3 engine.py check   --input examples/check_dark_pattern.json # 윤리 점검
python3 -m unittest discover -s tests -v                          # 테스트 42개
```

입력 형식은 `engine/SCHEMA.md`에 있습니다. 핵심은 `facts: [{claim, source, verified, kind}]`(출처 없는 주장은 `verified:false`로 두면 '의견'으로 분리), `audience`(청중 상태), `cues`(LLM이 뽑은 원칙·경향 단서, 원문 구절 그대로), `draft`(점검할 초안)입니다.

지식 갱신: 온톨로지(`ontology/entities/`)가 정본이고 `engine/knowledge.json`은 파생물입니다.
```bash
cd engine
python3 tools/build_research.py   # research/ → ontology 개체·규칙·노트 (멱등)
python3 build_kb.py               # ontology → knowledge.json
```

에이전트에서 쓸 때는 `SKILL.md`의 절차(팩트 확인 → LLM 단서 추출 → 엔진 실행 → 해석, 고친 초안은 다시 check로 PASS 확인)와 보고 형식을 따릅니다.

## 보고서
`report/NDB-설득의심리학-심층보고서.html`이 원본이고 PDF(30쪽)는 같은 원본에서 만든 인쇄본입니다. 2026-10-25 품질 검토의 필수 수정 M1~M6이 HTML과 PDF 모두에 반영되어 있습니다(`CHANGELOG.md` 참고).

## 면책
이 저장소는 **정보 제공용**입니다. 특정 진료·투자·투표를 권하지 않으며, 의학적·법률적 자문을 대신하지 않습니다. 의료법 조문(특히 제56조 제2항의 세부 호 번호)은 적용 전에 국가법령정보센터의 최신 원문으로 다시 확인하세요. 효과 크기는 대부분 논문 초록 기준이며, 미게재 원고(프리프린트)는 C등급으로 표시했습니다. 엔진은 초안과 점검까지만 하며, 외부 발송·게시는 사람이 승인한 뒤에만 하세요.

## 라이선스
별도 라이선스 파일이 없습니다. 저작권은 작성자에게 있으며, 이용 조건은 저장소 소유자에게 문의하세요.
