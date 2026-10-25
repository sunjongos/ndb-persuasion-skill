---
id: rule.pr_man_lollapalooza_count
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_man_lollapalooza_count - kb_kind - research_rule
- rule.pr_man_lollapalooza_count - orig_id - man.lollapalooza_count
- rule.pr_man_lollapalooza_count - rule_kind - manipulation_detection
- rule.pr_man_lollapalooza_count - label - 플래그 3개 이상 → 정지·검토
- rule.pr_man_lollapalooza_count - level - warn
- rule.pr_man_lollapalooza_count - grades - A/B
- rule.pr_man_lollapalooza_count - part_of - concept.persuasion_research
- rule.pr_man_lollapalooza_count - evidence_grade - concept.evidence_grade_a
- rule.pr_man_lollapalooza_count - evidence_grade - concept.evidence_grade_b
- rule.pr_man_lollapalooza_count - detector - {"computed": "경향 3개 이상"}
- rule.pr_man_lollapalooza_count - when - [자료 내용] {"signal": "동시에 활성화된 원칙/경향 플래그 ≥3"}
- rule.pr_man_lollapalooza_count - then - [자료 내용] {"verdict": "stop_and_review", "action": "PDF 체크리스트(3개 이상 → 정지) 실행"}
- rule.pr_man_lollapalooza_count - source - src:CIAL2004 (https://doi.org/10.1146/annurev.psych.55.090902.142015) [등급 A]
- rule.pr_man_lollapalooza_count - source - src:LUGURI2021 (https://doi.org/10.1093/jla/laaa006) [등급 B]
- rule.pr_man_lollapalooza_count - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 man.lollapalooza_count, 플래그 3개 이상 → 정지·검토
