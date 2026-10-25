---
id: rule.pr_cue_outgroup_hostility
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_outgroup_hostility - kb_kind - research_rule
- rule.pr_cue_outgroup_hostility - orig_id - cue.outgroup_hostility
- rule.pr_cue_outgroup_hostility - rule_kind - cue_detection
- rule.pr_cue_outgroup_hostility - label - 외집단 적대 표현(정서적 양극화)
- rule.pr_cue_outgroup_hostility - level - warn
- rule.pr_cue_outgroup_hostility - grades - B
- rule.pr_cue_outgroup_hostility - part_of - concept.persuasion_research
- rule.pr_cue_outgroup_hostility - evidence_grade - concept.evidence_grade_b
- rule.pr_cue_outgroup_hostility - detector - {"any": "저쪽|저들|배신자|적폐|빨갱이|토착왜구"}
- rule.pr_cue_outgroup_hostility - when - [자료 내용] {"any_regex": ["저쪽", "저들", "배신자", "적폐", "빨갱이", "토착왜구"]}
- rule.pr_cue_outgroup_hostility - then - [자료 내용] {"flag": "affective_polarization", "action": "정체성 공격 표시; 사실 주장과 분리"}
- rule.pr_cue_outgroup_hostility - source - src:IYENGAR2012 (https://doi.org/10.1093/poq/nfs038) [등급 B]
- rule.pr_cue_outgroup_hostility - source - src:IYENGAR2019 (https://doi.org/10.1146/annurev-polisci-051117-073034) [등급 B]
- rule.pr_cue_outgroup_hostility - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.outgroup_hostility, 외집단 적대 표현(정서적 양극화)
