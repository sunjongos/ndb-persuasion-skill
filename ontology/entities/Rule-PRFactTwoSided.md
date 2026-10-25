---
id: rule.pr_fact_two_sided
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_fact_two_sided - kb_kind - research_rule
- rule.pr_fact_two_sided - orig_id - fact.two_sided
- rule.pr_fact_two_sided - rule_kind - fact_gate
- rule.pr_fact_two_sided - label - 고관여: 반대 근거 1개 이상 제시+반박
- rule.pr_fact_two_sided - level - warn
- rule.pr_fact_two_sided - grades - A
- rule.pr_fact_two_sided - part_of - concept.persuasion_research
- rule.pr_fact_two_sided - evidence_grade - concept.evidence_grade_a
- rule.pr_fact_two_sided - detector - {"counter": "반면|단점|부작용|위험도|다만|그러나|대안", "fact_kinds": "alternative|comparison|counterargument"}
- rule.pr_fact_two_sided - when - [자료 내용] {"signal": "고관여·결정 중대"}
- rule.pr_fact_two_sided - then - [자료 내용] {"require": "주요 반대 근거 1개 이상 제시+반박"}
- rule.pr_fact_two_sided - source - src:OKEEFE1999 (https://doi.org/10.1080/23808985.1999.11678963) [등급 A]
- rule.pr_fact_two_sided - source - src:STACEY2024 (https://doi.org/10.1002/14651858.CD001431.pub6) [등급 A]
- rule.pr_fact_two_sided - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 fact.two_sided, 고관여: 반대 근거 1개 이상 제시+반박
