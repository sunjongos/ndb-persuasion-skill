---
id: rule.pr_cue_deadline_scarcity
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_deadline_scarcity - kb_kind - research_rule
- rule.pr_cue_deadline_scarcity - orig_id - cue.deadline_scarcity
- rule.pr_cue_deadline_scarcity - rule_kind - cue_detection
- rule.pr_cue_deadline_scarcity - label - 기한·희소성 단서
- rule.pr_cue_deadline_scarcity - level - info
- rule.pr_cue_deadline_scarcity - grades - A/B
- rule.pr_cue_deadline_scarcity - part_of - concept.persuasion_research
- rule.pr_cue_deadline_scarcity - evidence_grade - concept.evidence_grade_a
- rule.pr_cue_deadline_scarcity - evidence_grade - concept.evidence_grade_b
- rule.pr_cue_deadline_scarcity - detector - {"any": "오늘만|마감\\s*임박|한정|남은\\s*수량|지금\\s*아니면"}
- rule.pr_cue_deadline_scarcity - when - [자료 내용] {"any_regex": ["오늘만", "마감 임박", "한정", "남은 수량", "지금 아니면"]}
- rule.pr_cue_deadline_scarcity - then - [자료 내용] {"flag": "scarcity_or_loss_frame", "map": ["Cialdini:희귀성", "Munger:#14 박탈 초반응"], "action": "희소성 사실 여부 검증(재고·마감 근거)"}
- rule.pr_cue_deadline_scarcity - maps_to - principle.cialdini_scarcity
- rule.pr_cue_deadline_scarcity - maps_to - concept.munger_t14_deprivation
- rule.pr_cue_deadline_scarcity - source - src:KT1979 (https://doi.org/10.2307/1914185) [등급 A]
- rule.pr_cue_deadline_scarcity - source - src:MATHUR2019 (https://doi.org/10.1145/3359183) [등급 B]
- rule.pr_cue_deadline_scarcity - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.deadline_scarcity, 기한·희소성 단서
