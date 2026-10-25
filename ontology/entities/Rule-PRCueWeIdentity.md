---
id: rule.pr_cue_we_identity
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_we_identity - kb_kind - research_rule
- rule.pr_cue_we_identity - orig_id - cue.we_identity
- rule.pr_cue_we_identity - rule_kind - cue_detection
- rule.pr_cue_we_identity - label - '우리' 정체성 단서(연대감)
- rule.pr_cue_we_identity - level - info
- rule.pr_cue_we_identity - grades - A/B
- rule.pr_cue_we_identity - part_of - concept.persuasion_research
- rule.pr_cue_we_identity - evidence_grade - concept.evidence_grade_a
- rule.pr_cue_we_identity - evidence_grade - concept.evidence_grade_b
- rule.pr_cue_we_identity - detector - {"any": "우리(?!\\s*병원)\\s|우리가|같은\\s*편|한\\s*식구|동문|고향"}
- rule.pr_cue_we_identity - when - [자료 내용] {"any_regex": ["우리 ", "우리가", "같은 편", "한 식구", "동문", "고향"]}
- rule.pr_cue_we_identity - then - [자료 내용] {"flag": "unity", "map": ["Cialdini:연대감"], "action": "공유 정체성이 실제인지 확인"}
- rule.pr_cue_we_identity - maps_to - principle.cialdini_unity
- rule.pr_cue_we_identity - source - src:CIAL2021 (https://www.harpercollins.com/products/influence-new-and-expanded-robert-b-cialdini) [등급 B]
- rule.pr_cue_we_identity - source - src:MOGAN2017 (https://doi.org/10.1016/j.jesp.2017.03.009) [등급 A]
- rule.pr_cue_we_identity - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.we_identity, '우리' 정체성 단서(연대감)
