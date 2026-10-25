---
id: rule.pr_cue_commitment_ladder
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_commitment_ladder - kb_kind - research_rule
- rule.pr_cue_commitment_ladder - orig_id - cue.commitment_ladder
- rule.pr_cue_commitment_ladder - rule_kind - cue_detection
- rule.pr_cue_commitment_ladder - label - 작은 동의 → 큰 요청(문간에 발)
- rule.pr_cue_commitment_ladder - level - info
- rule.pr_cue_commitment_ladder - grades - B
- rule.pr_cue_commitment_ladder - part_of - concept.persuasion_research
- rule.pr_cue_commitment_ladder - evidence_grade - concept.evidence_grade_b
- rule.pr_cue_commitment_ladder - detector - {"any": "(?:일단|우선|먼저)[^.!?\\n]{0,25}만[^\\n]{0,60}?(?:그럼|그러면|이제|이왕)"}
- rule.pr_cue_commitment_ladder - when - [자료 내용] {"signal": "작은 동의 요청 후 큰 요청"}
- rule.pr_cue_commitment_ladder - then - [자료 내용] {"flag": "fitd_commitment", "map": ["Cialdini:일관성", "Munger:#5"], "action": "각 단계 독립 판단"}
- rule.pr_cue_commitment_ladder - maps_to - principle.cialdini_consistency
- rule.pr_cue_commitment_ladder - maps_to - concept.munger_t05_inconsistency
- rule.pr_cue_commitment_ladder - source - src:BURGER1999 (https://doi.org/10.1207/s15327957pspr0304_2) [등급 B]
- rule.pr_cue_commitment_ladder - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.commitment_ladder, 작은 동의 → 큰 요청(문간에 발)
