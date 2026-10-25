---
id: rule.pr_dp_nagging
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_dp_nagging - kb_kind - research_rule
- rule.pr_dp_nagging - orig_id - dp.nagging
- rule.pr_dp_nagging - rule_kind - manipulation_detection
- rule.pr_dp_nagging - label - 다크패턴: 반복 강요(잔소리)
- rule.pr_dp_nagging - level - block
- rule.pr_dp_nagging - grades - B
- rule.pr_dp_nagging - part_of - concept.persuasion_research
- rule.pr_dp_nagging - evidence_grade - concept.evidence_grade_b
- rule.pr_dp_nagging - detector - {"any": "동의하실\\s*때까지|계속\\s*(?:알림|팝업|연락)|하루에도\\s*여러\\s*번|매번\\s*(?:묻|팝업)"}
- rule.pr_dp_nagging - when - [자료 내용] {"pattern": "반복 팝업 강요"}
- rule.pr_dp_nagging - then - [자료 내용] {"verdict": "manipulation", "action": "BLOCK + 대안(투명 표시) 제시"}
- rule.pr_dp_nagging - severity - high
- rule.pr_dp_nagging - source - src:MATHUR2019 (https://doi.org/10.1145/3359183) [등급 B]
- rule.pr_dp_nagging - source - src:GRAY2018 (https://doi.org/10.1145/3173574.3174108) [등급 B]
- rule.pr_dp_nagging - source - src:LUGURI2021 (https://doi.org/10.1093/jla/laaa006) [등급 B]
- rule.pr_dp_nagging - source - src:FTC2022 (https://www.ftc.gov/reports/bringing-dark-patterns-light) [등급 B]
- rule.pr_dp_nagging - source - src:DSA2022 (https://eur-lex.europa.eu/eli/reg/2022/2065/oj) [등급 B]
- rule.pr_dp_nagging - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 dp.nagging, 다크패턴: 반복 강요(잔소리)
