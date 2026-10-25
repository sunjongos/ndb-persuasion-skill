---
id: rule.pr_dp_confirmshaming
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_dp_confirmshaming - kb_kind - research_rule
- rule.pr_dp_confirmshaming - orig_id - dp.confirmshaming
- rule.pr_dp_confirmshaming - rule_kind - manipulation_detection
- rule.pr_dp_confirmshaming - label - 다크패턴: 거절 수치심 문구
- rule.pr_dp_confirmshaming - level - block
- rule.pr_dp_confirmshaming - grades - B
- rule.pr_dp_confirmshaming - part_of - concept.persuasion_research
- rule.pr_dp_confirmshaming - evidence_grade - concept.evidence_grade_b
- rule.pr_dp_confirmshaming - detector - {"any": "(?:아니요|아니오|괜찮아요|됐어요)[,\\s]*(?:저는|전|나는)?[^.!?\\n]{0,25}(?:포기|싫어|필요\\s*없|원하지\\s*않|손해\\s*볼게)"}
- rule.pr_dp_confirmshaming - when - [자료 내용] {"pattern": "거절 시 수치심 문구"}
- rule.pr_dp_confirmshaming - then - [자료 내용] {"verdict": "manipulation", "action": "BLOCK + 대안(투명 표시) 제시"}
- rule.pr_dp_confirmshaming - severity - high
- rule.pr_dp_confirmshaming - source - src:MATHUR2019 (https://doi.org/10.1145/3359183) [등급 B]
- rule.pr_dp_confirmshaming - source - src:GRAY2018 (https://doi.org/10.1145/3173574.3174108) [등급 B]
- rule.pr_dp_confirmshaming - source - src:LUGURI2021 (https://doi.org/10.1093/jla/laaa006) [등급 B]
- rule.pr_dp_confirmshaming - source - src:FTC2022 (https://www.ftc.gov/reports/bringing-dark-patterns-light) [등급 B]
- rule.pr_dp_confirmshaming - source - src:DSA2022 (https://eur-lex.europa.eu/eli/reg/2022/2065/oj) [등급 B]
- rule.pr_dp_confirmshaming - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 dp.confirmshaming, 다크패턴: 거절 수치심 문구
