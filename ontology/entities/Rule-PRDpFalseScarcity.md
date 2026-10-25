---
id: rule.pr_dp_false_scarcity
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_dp_false_scarcity - kb_kind - research_rule
- rule.pr_dp_false_scarcity - orig_id - dp.false_scarcity
- rule.pr_dp_false_scarcity - rule_kind - manipulation_detection
- rule.pr_dp_false_scarcity - label - 다크패턴: 가짜 희소성·카운트다운
- rule.pr_dp_false_scarcity - level - block
- rule.pr_dp_false_scarcity - grades - B
- rule.pr_dp_false_scarcity - part_of - concept.persuasion_research
- rule.pr_dp_false_scarcity - evidence_grade - concept.evidence_grade_b
- rule.pr_dp_false_scarcity - detector - {"any": "카운트다운|\\d+\\s*분\\s*후\\s*(?:종료|마감)|품절\\s*임박|마감\\s*임박|\\d+\\s*개\\s*남|오늘만|이번\\s*달까지만", "unless_fact": "real_limit"}
- rule.pr_dp_false_scarcity - when - [자료 내용] {"pattern": "가짜 희소성·카운트다운"}
- rule.pr_dp_false_scarcity - then - [자료 내용] {"verdict": "manipulation", "action": "BLOCK + 대안(투명 표시) 제시"}
- rule.pr_dp_false_scarcity - severity - high
- rule.pr_dp_false_scarcity - source - src:MATHUR2019 (https://doi.org/10.1145/3359183) [등급 B]
- rule.pr_dp_false_scarcity - source - src:GRAY2018 (https://doi.org/10.1145/3173574.3174108) [등급 B]
- rule.pr_dp_false_scarcity - source - src:LUGURI2021 (https://doi.org/10.1093/jla/laaa006) [등급 B]
- rule.pr_dp_false_scarcity - source - src:FTC2022 (https://www.ftc.gov/reports/bringing-dark-patterns-light) [등급 B]
- rule.pr_dp_false_scarcity - source - src:DSA2022 (https://eur-lex.europa.eu/eli/reg/2022/2065/oj) [등급 B]
- rule.pr_dp_false_scarcity - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 dp.false_scarcity, 다크패턴: 가짜 희소성·카운트다운
