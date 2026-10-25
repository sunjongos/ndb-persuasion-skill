---
id: rule.pr_cue_narrative
type: Topic
updated: 2026-10-25
confidence: 0.7
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_narrative - kb_kind - research_rule
- rule.pr_cue_narrative - orig_id - cue.narrative
- rule.pr_cue_narrative - rule_kind - cue_detection
- rule.pr_cue_narrative - label - 사례 이야기 중심·통계 없음
- rule.pr_cue_narrative - level - warn
- rule.pr_cue_narrative - grades - A/C
- rule.pr_cue_narrative - part_of - concept.persuasion_research
- rule.pr_cue_narrative - evidence_grade - concept.evidence_grade_a
- rule.pr_cue_narrative - evidence_grade - concept.evidence_grade_c
- rule.pr_cue_narrative - detector - {"story": "한\\s*환자분|어떤\\s*분이|제가\\s*아는|실제로\\s*한|저희\\s*어머니|사연|경험담|후기를\\s*보면", "number": "\\d"}
- rule.pr_cue_narrative - when - [자료 내용] {"signal": "개인 사례 이야기 중심, 통계 없음"}
- rule.pr_cue_narrative - then - [자료 내용] {"flag": "narrative_transport", "action": "사례 대표성(기저율) 확인"}
- rule.pr_cue_narrative - source - src:BRADDOCK2016 (https://doi.org/10.1080/03637751.2015.1128555) [등급 A]
- rule.pr_cue_narrative - source - src:ALLEN1997 (https://doi.org/10.1080/08824099709388654) [등급 C]
- rule.pr_cue_narrative - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.narrative, 사례 이야기 중심·통계 없음
