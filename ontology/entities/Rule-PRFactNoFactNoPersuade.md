---
id: rule.pr_fact_no_fact_no_persuade
type: Topic
updated: 2026-10-25
confidence: 0.7
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_fact_no_fact_no_persuade - kb_kind - research_rule
- rule.pr_fact_no_fact_no_persuade - orig_id - fact.no_fact_no_persuade
- rule.pr_fact_no_fact_no_persuade - rule_kind - fact_gate
- rule.pr_fact_no_fact_no_persuade - label - 팩트 없는 설득(사기꾼 모드)
- rule.pr_fact_no_fact_no_persuade - level - block
- rule.pr_fact_no_fact_no_persuade - grades - B/C
- rule.pr_fact_no_fact_no_persuade - part_of - concept.persuasion_research
- rule.pr_fact_no_fact_no_persuade - evidence_grade - concept.evidence_grade_b
- rule.pr_fact_no_fact_no_persuade - evidence_grade - concept.evidence_grade_c
- rule.pr_fact_no_fact_no_persuade - detector - {"computed": "F0/팩트 게이트"}
- rule.pr_fact_no_fact_no_persuade - when - [자료 내용] {"signal": "근거 없이 심리 기법만으로 결론 유도"}
- rule.pr_fact_no_fact_no_persuade - then - [자료 내용] {"verdict": "사기꾼 모드 → BLOCK", "why": "사실을 빼면 AI 설득 효과도 크게 감소: 사실이 정당한 설득의 엔진"}
- rule.pr_fact_no_fact_no_persuade - source - src:COSTELLO2025 (https://doi.org/10.31234/osf.io/h7n8u_v2) [등급 C]
- rule.pr_fact_no_fact_no_persuade - source - src:LIN2025 (https://doi.org/10.1038/s41586%2D025%2D09771%2D9) [등급 B]
- rule.pr_fact_no_fact_no_persuade - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 fact.no_fact_no_persuade, 팩트 없는 설득(사기꾼 모드)
