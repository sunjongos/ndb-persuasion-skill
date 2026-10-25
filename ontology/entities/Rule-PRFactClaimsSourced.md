---
id: rule.pr_fact_claims_sourced
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_fact_claims_sourced - kb_kind - research_rule
- rule.pr_fact_claims_sourced - orig_id - fact.claims_sourced
- rule.pr_fact_claims_sourced - rule_kind - fact_gate
- rule.pr_fact_claims_sourced - label - 출처 없는 사실 주장은 '의견'으로 표시
- rule.pr_fact_claims_sourced - level - warn
- rule.pr_fact_claims_sourced - grades - B
- rule.pr_fact_claims_sourced - part_of - concept.persuasion_research
- rule.pr_fact_claims_sourced - evidence_grade - concept.evidence_grade_b
- rule.pr_fact_claims_sourced - detector - {"facts": "source 없음 → 의견"}
- rule.pr_fact_claims_sourced - when - [자료 내용] {"every_factual_claim": true}
- rule.pr_fact_claims_sourced - then - [자료 내용] {"require": "1차 출처(DOI/URL) 또는 내부 데이터; 없으면 \"의견\"으로 표시", "block_if_missing": true}
- rule.pr_fact_claims_sourced - source - src:REINARD1988 (https://doi.org/10.1111/j.1468-2958.1988.tb00170.x) [등급 B]
- rule.pr_fact_claims_sourced - source - src:BAKER2001 (https://doi.org/10.1207/S15327728JMME1602&3_6) [등급 B]
- rule.pr_fact_claims_sourced - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 fact.claims_sourced, 출처 없는 사실 주장은 '의견'으로 표시
