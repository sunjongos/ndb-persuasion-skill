---
id: rule.pr_cue_authority
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_authority - kb_kind - research_rule
- rule.pr_cue_authority - orig_id - cue.authority
- rule.pr_cue_authority - rule_kind - cue_detection
- rule.pr_cue_authority - label - 권위 단서
- rule.pr_cue_authority - level - info
- rule.pr_cue_authority - grades - B
- rule.pr_cue_authority - part_of - concept.persuasion_research
- rule.pr_cue_authority - evidence_grade - concept.evidence_grade_b
- rule.pr_cue_authority - detector - {"any": "교수|전문의|박사|권위자|하버드|논문에\\s*따르면"}
- rule.pr_cue_authority - when - [자료 내용] {"any_regex": ["교수", "전문의", "박사", "권위자", "하버드", "논문에 따르면"]}
- rule.pr_cue_authority - then - [자료 내용] {"flag": "authority", "map": ["Cialdini:권위", "Munger:#22"], "action": "전문 분야 일치·이해상충·원문 확인"}
- rule.pr_cue_authority - maps_to - principle.cialdini_authority
- rule.pr_cue_authority - maps_to - concept.munger_t22_authority
- rule.pr_cue_authority - source - src:PORNPIT2004 (https://doi.org/10.1111/j.1559-1816.2004.tb02547.x) [등급 B]
- rule.pr_cue_authority - source - src:BURGER2009 (https://doi.org/10.1037/a0010932) [등급 B]
- rule.pr_cue_authority - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.authority, 권위 단서
