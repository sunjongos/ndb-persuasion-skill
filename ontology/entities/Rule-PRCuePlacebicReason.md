---
id: rule.pr_cue_placebic_reason
type: Topic
updated: 2026-10-25
confidence: 0.7
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_placebic_reason - kb_kind - research_rule
- rule.pr_cue_placebic_reason - orig_id - cue.placebic_reason
- rule.pr_cue_placebic_reason - rule_kind - cue_detection
- rule.pr_cue_placebic_reason - label - 빈 이유(요청 반복형 '때문에')
- rule.pr_cue_placebic_reason - level - info
- rule.pr_cue_placebic_reason - grades - C
- rule.pr_cue_placebic_reason - part_of - concept.persuasion_research
- rule.pr_cue_placebic_reason - evidence_grade - concept.evidence_grade_c
- rule.pr_cue_placebic_reason - detector - {"any": "(?:해야|하셔야)\\s*(?:하기\\s*때문|해서|하니까)|(?:규정|원래)\\s*그렇(?:기\\s*때문|거든)"}
- rule.pr_cue_placebic_reason - when - [자료 내용] {"any_regex": ["왜냐하면", "때문에"], "and": "이유 내용이 요청을 반복할 뿐"}
- rule.pr_cue_placebic_reason - then - [자료 내용] {"flag": "placebic_reason", "map": ["Munger:#24 이유 존중"], "action": "이유의 실질 내용 평가"}
- rule.pr_cue_placebic_reason - maps_to - concept.munger_t24_reason
- rule.pr_cue_placebic_reason - source - src:LANGER1978 (https://doi.org/10.1037/0022-3514.36.6.635) [등급 C]
- rule.pr_cue_placebic_reason - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.placebic_reason, 빈 이유(요청 반복형 '때문에')
