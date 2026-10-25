---
id: rule.pr_cue_reciprocity_gift
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_reciprocity_gift - kb_kind - research_rule
- rule.pr_cue_reciprocity_gift - orig_id - cue.reciprocity_gift
- rule.pr_cue_reciprocity_gift - rule_kind - cue_detection
- rule.pr_cue_reciprocity_gift - label - 선물·양보 단서(상호성)
- rule.pr_cue_reciprocity_gift - level - info
- rule.pr_cue_reciprocity_gift - grades - A/B
- rule.pr_cue_reciprocity_gift - part_of - concept.persuasion_research
- rule.pr_cue_reciprocity_gift - evidence_grade - concept.evidence_grade_a
- rule.pr_cue_reciprocity_gift - evidence_grade - concept.evidence_grade_b
- rule.pr_cue_reciprocity_gift - detector - {"any": "무료로\\s*드|선물|특별히\\s*해\\s*드|먼저\\s*양보"}
- rule.pr_cue_reciprocity_gift - when - [자료 내용] {"any_regex": ["무료로 드", "선물", "특별히 해드", "먼저 양보"]}
- rule.pr_cue_reciprocity_gift - then - [자료 내용] {"flag": "reciprocity", "map": ["Cialdini:상호성", "Munger:#9"], "action": "선물과 요청을 분리 평가"}
- rule.pr_cue_reciprocity_gift - maps_to - principle.cialdini_reciprocity
- rule.pr_cue_reciprocity_gift - maps_to - concept.munger_t09_reciprocity
- rule.pr_cue_reciprocity_gift - source - src:CIAL2004 (https://doi.org/10.1146/annurev.psych.55.090902.142015) [등급 A]
- rule.pr_cue_reciprocity_gift - source - src:FEELEY2012 (https://doi.org/10.1080/03637751.2012.697631) [등급 B]
- rule.pr_cue_reciprocity_gift - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.reciprocity_gift, 선물·양보 단서(상호성)
