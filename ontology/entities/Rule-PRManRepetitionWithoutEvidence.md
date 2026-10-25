---
id: rule.pr_man_repetition_without_evidence
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_man_repetition_without_evidence - kb_kind - research_rule
- rule.pr_man_repetition_without_evidence - orig_id - man.repetition_without_evidence
- rule.pr_man_repetition_without_evidence - rule_kind - manipulation_detection
- rule.pr_man_repetition_without_evidence - label - 근거 추가 없이 같은 주장 반복
- rule.pr_man_repetition_without_evidence - level - warn
- rule.pr_man_repetition_without_evidence - grades - A
- rule.pr_man_repetition_without_evidence - part_of - concept.persuasion_research
- rule.pr_man_repetition_without_evidence - evidence_grade - concept.evidence_grade_a
- rule.pr_man_repetition_without_evidence - detector - {"needs": "cue.repetition & 검증 팩트 0"}
- rule.pr_man_repetition_without_evidence - when - [자료 내용] {"signal": "근거 추가 없이 같은 주장 반복"}
- rule.pr_man_repetition_without_evidence - then - [자료 내용] {"verdict": "warning", "action": "반복 대신 근거 1개 추가 요구"}
- rule.pr_man_repetition_without_evidence - source - src:DECHENE2010 (https://doi.org/10.1177/1088868309352251) [등급 A]
- rule.pr_man_repetition_without_evidence - source - src:FAZIO2015 (https://doi.org/10.1037/xge0000098) [등급 A]
- rule.pr_man_repetition_without_evidence - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 man.repetition_without_evidence, 근거 추가 없이 같은 주장 반복
