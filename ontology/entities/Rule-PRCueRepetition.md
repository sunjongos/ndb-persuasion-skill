---
id: rule.pr_cue_repetition
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_repetition - kb_kind - research_rule
- rule.pr_cue_repetition - orig_id - cue.repetition
- rule.pr_cue_repetition - rule_kind - cue_detection
- rule.pr_cue_repetition - label - 반복 단서(환상적 진실 효과)
- rule.pr_cue_repetition - level - info
- rule.pr_cue_repetition - grades - A
- rule.pr_cue_repetition - part_of - concept.persuasion_research
- rule.pr_cue_repetition - evidence_grade - concept.evidence_grade_a
- rule.pr_cue_repetition - detector - {"any": "반복|계속\\s*말|다들\\s*알다시피|몇\\s*번이고", "same_claim_min": 3}
- rule.pr_cue_repetition - when - [자료 내용] {"any_regex": ["반복", "계속 말", "다들 알다시피", "몇 번이고"], "or_signal": "동일 주장 3회 이상 반복"}
- rule.pr_cue_repetition - then - [자료 내용] {"flag": "illusory_truth", "map": ["Munger:#18 가용성", "Munger:#10 단순 연관"], "action": "반복 횟수와 근거 수를 분리 표시"}
- rule.pr_cue_repetition - maps_to - concept.munger_t18_availability
- rule.pr_cue_repetition - maps_to - concept.munger_t10_association
- rule.pr_cue_repetition - source - src:DECHENE2010 (https://doi.org/10.1177/1088868309352251) [등급 A]
- rule.pr_cue_repetition - source - src:FAZIO2015 (https://doi.org/10.1037/xge0000098) [등급 A]
- rule.pr_cue_repetition - source - src:HASSAN2021 (https://doi.org/10.1186/s41235%2D021%2D00301%2D5) [등급 A]
- rule.pr_cue_repetition - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.repetition, 반복 단서(환상적 진실 효과)
