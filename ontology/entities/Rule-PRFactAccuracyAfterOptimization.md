---
id: rule.pr_fact_accuracy_after_optimization
type: Topic
updated: 2026-10-25
confidence: 0.7
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_fact_accuracy_after_optimization - kb_kind - research_rule
- rule.pr_fact_accuracy_after_optimization - orig_id - fact.accuracy_after_optimization
- rule.pr_fact_accuracy_after_optimization - rule_kind - fact_gate
- rule.pr_fact_accuracy_after_optimization - label - 설득력 최적화 후 정확도 재검사 필요
- rule.pr_fact_accuracy_after_optimization - level - warn
- rule.pr_fact_accuracy_after_optimization - grades - B/C
- rule.pr_fact_accuracy_after_optimization - part_of - concept.persuasion_research
- rule.pr_fact_accuracy_after_optimization - evidence_grade - concept.evidence_grade_b
- rule.pr_fact_accuracy_after_optimization - evidence_grade - concept.evidence_grade_c
- rule.pr_fact_accuracy_after_optimization - detector - {"input": "ai_generated|optimized, accuracy_rechecked"}
- rule.pr_fact_accuracy_after_optimization - when - [자료 내용] {"signal": "설득력 최적화 단계(재작성·AI 생성·정보량 증가) 후"}
- rule.pr_fact_accuracy_after_optimization - then - [자료 내용] {"require": "사실 정확도 재검사(주장별 검증)", "why": "설득 레버를 당길수록 정확도 하락"}
- rule.pr_fact_accuracy_after_optimization - source - src:HACKEN2025B (https://doi.org/10.1126/science.aea3884) [등급 B]
- rule.pr_fact_accuracy_after_optimization - source - src:LIN2025 (https://doi.org/10.1038/s41586%2D025%2D09771%2D9) [등급 B]
- rule.pr_fact_accuracy_after_optimization - source - src:SCHOEN2025 (https://arxiv.org/abs/2505.09662) [등급 C]
- rule.pr_fact_accuracy_after_optimization - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 fact.accuracy_after_optimization, 설득력 최적화 후 정확도 재검사 필요
