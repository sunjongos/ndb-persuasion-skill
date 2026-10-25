---
id: rule.pr_cue_everyone_does
type: Topic
updated: 2026-10-25
confidence: 0.7
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_everyone_does - kb_kind - research_rule
- rule.pr_cue_everyone_does - orig_id - cue.everyone_does
- rule.pr_cue_everyone_does - rule_kind - cue_detection
- rule.pr_cue_everyone_does - label - 다수 단서(사회적 증거)
- rule.pr_cue_everyone_does - level - info
- rule.pr_cue_everyone_does - grades - A/C
- rule.pr_cue_everyone_does - part_of - concept.persuasion_research
- rule.pr_cue_everyone_does - evidence_grade - concept.evidence_grade_a
- rule.pr_cue_everyone_does - evidence_grade - concept.evidence_grade_c
- rule.pr_cue_everyone_does - detector - {"any": "다들|대부분|%가\\s*선택|1위|많은\\s*분들이"}
- rule.pr_cue_everyone_does - when - [자료 내용] {"any_regex": ["다들", "대부분", "%가 선택", "1위", "많은 분들이"]}
- rule.pr_cue_everyone_does - then - [자료 내용] {"flag": "social_proof", "map": ["Cialdini:사회적 증거", "Munger:#15"], "action": "다수 수치 출처 확인"}
- rule.pr_cue_everyone_does - maps_to - principle.cialdini_social_proof
- rule.pr_cue_everyone_does - maps_to - concept.munger_t15_social_proof
- rule.pr_cue_everyone_does - source - src:CIAL2004 (https://doi.org/10.1146/annurev.psych.55.090902.142015) [등급 A]
- rule.pr_cue_everyone_does - source - src:ALLCOTT2011 (https://doi.org/10.1016/j.jpubeco.2011.03.003) [등급 A]
- rule.pr_cue_everyone_does - source - src:BARNFIELD2020 (https://doi.org/10.1177/1478929919870691) [등급 C]
- rule.pr_cue_everyone_does - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.everyone_does, 다수 단서(사회적 증거)
