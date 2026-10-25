---
id: rule.pr_dp_sneak_into_basket
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_dp_sneak_into_basket - kb_kind - research_rule
- rule.pr_dp_sneak_into_basket - orig_id - dp.sneak_into_basket
- rule.pr_dp_sneak_into_basket - rule_kind - manipulation_detection
- rule.pr_dp_sneak_into_basket - label - 다크패턴: 몰래 추가·숨은 비용
- rule.pr_dp_sneak_into_basket - level - block
- rule.pr_dp_sneak_into_basket - grades - B
- rule.pr_dp_sneak_into_basket - part_of - concept.persuasion_research
- rule.pr_dp_sneak_into_basket - evidence_grade - concept.evidence_grade_b
- rule.pr_dp_sneak_into_basket - detector - {"any": "자동으로\\s*추가|자동\\s*포함|별도\\s*고지\\s*없이|숨은\\s*비용|결제\\s*(?:단계|시)\\s*추가"}
- rule.pr_dp_sneak_into_basket - when - [자료 내용] {"pattern": "몰래 추가·숨은 비용"}
- rule.pr_dp_sneak_into_basket - then - [자료 내용] {"verdict": "manipulation", "action": "BLOCK + 대안(투명 표시) 제시"}
- rule.pr_dp_sneak_into_basket - severity - high
- rule.pr_dp_sneak_into_basket - source - src:MATHUR2019 (https://doi.org/10.1145/3359183) [등급 B]
- rule.pr_dp_sneak_into_basket - source - src:GRAY2018 (https://doi.org/10.1145/3173574.3174108) [등급 B]
- rule.pr_dp_sneak_into_basket - source - src:LUGURI2021 (https://doi.org/10.1093/jla/laaa006) [등급 B]
- rule.pr_dp_sneak_into_basket - source - src:FTC2022 (https://www.ftc.gov/reports/bringing-dark-patterns-light) [등급 B]
- rule.pr_dp_sneak_into_basket - source - src:DSA2022 (https://eur-lex.europa.eu/eli/reg/2022/2065/oj) [등급 B]
- rule.pr_dp_sneak_into_basket - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 dp.sneak_into_basket, 다크패턴: 몰래 추가·숨은 비용
