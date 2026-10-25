---
id: rule.pr_dp_preselected_default
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_dp_preselected_default - kb_kind - research_rule
- rule.pr_dp_preselected_default - orig_id - dp.preselected_default
- rule.pr_dp_preselected_default - rule_kind - manipulation_detection
- rule.pr_dp_preselected_default - label - 다크패턴: 불리한 사전 선택
- rule.pr_dp_preselected_default - level - block
- rule.pr_dp_preselected_default - grades - B
- rule.pr_dp_preselected_default - part_of - concept.persuasion_research
- rule.pr_dp_preselected_default - evidence_grade - concept.evidence_grade_b
- rule.pr_dp_preselected_default - detector - {"any": "미리\\s*체크|자동\\s*동의|기본으로\\s*선택|체크되어\\s*있|자동\\s*가입|자동\\s*연장"}
- rule.pr_dp_preselected_default - when - [자료 내용] {"pattern": "불리한 사전 선택"}
- rule.pr_dp_preselected_default - then - [자료 내용] {"verdict": "manipulation", "action": "BLOCK + 대안(투명 표시) 제시"}
- rule.pr_dp_preselected_default - severity - high
- rule.pr_dp_preselected_default - source - src:MATHUR2019 (https://doi.org/10.1145/3359183) [등급 B]
- rule.pr_dp_preselected_default - source - src:GRAY2018 (https://doi.org/10.1145/3173574.3174108) [등급 B]
- rule.pr_dp_preselected_default - source - src:LUGURI2021 (https://doi.org/10.1093/jla/laaa006) [등급 B]
- rule.pr_dp_preselected_default - source - src:FTC2022 (https://www.ftc.gov/reports/bringing-dark-patterns-light) [등급 B]
- rule.pr_dp_preselected_default - source - src:DSA2022 (https://eur-lex.europa.eu/eli/reg/2022/2065/oj) [등급 B]
- rule.pr_dp_preselected_default - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 dp.preselected_default, 다크패턴: 불리한 사전 선택
