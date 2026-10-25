---
id: rule.pr_dp_roach_motel
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_dp_roach_motel - kb_kind - research_rule
- rule.pr_dp_roach_motel - orig_id - dp.roach_motel
- rule.pr_dp_roach_motel - rule_kind - manipulation_detection
- rule.pr_dp_roach_motel - label - 다크패턴: 가입 쉽고 해지 어려움
- rule.pr_dp_roach_motel - level - block
- rule.pr_dp_roach_motel - grades - B
- rule.pr_dp_roach_motel - part_of - concept.persuasion_research
- rule.pr_dp_roach_motel - evidence_grade - concept.evidence_grade_b
- rule.pr_dp_roach_motel - detector - {"any": "(?:해지|탈퇴|환불|취소)[^.!?\\n]{0,20}(?:방문해야|직접\\s*방문|전화로만|서면으로만|불가)"}
- rule.pr_dp_roach_motel - when - [자료 내용] {"pattern": "가입 쉽고 해지 어려움"}
- rule.pr_dp_roach_motel - then - [자료 내용] {"verdict": "manipulation", "action": "BLOCK + 대안(투명 표시) 제시"}
- rule.pr_dp_roach_motel - severity - high
- rule.pr_dp_roach_motel - source - src:MATHUR2019 (https://doi.org/10.1145/3359183) [등급 B]
- rule.pr_dp_roach_motel - source - src:GRAY2018 (https://doi.org/10.1145/3173574.3174108) [등급 B]
- rule.pr_dp_roach_motel - source - src:LUGURI2021 (https://doi.org/10.1093/jla/laaa006) [등급 B]
- rule.pr_dp_roach_motel - source - src:FTC2022 (https://www.ftc.gov/reports/bringing-dark-patterns-light) [등급 B]
- rule.pr_dp_roach_motel - source - src:DSA2022 (https://eur-lex.europa.eu/eli/reg/2022/2065/oj) [등급 B]
- rule.pr_dp_roach_motel - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 dp.roach_motel, 다크패턴: 가입 쉽고 해지 어려움
