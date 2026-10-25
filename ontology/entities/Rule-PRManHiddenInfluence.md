---
id: rule.pr_man_hidden_influence
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_man_hidden_influence - kb_kind - research_rule
- rule.pr_man_hidden_influence - orig_id - man.hidden_influence
- rule.pr_man_hidden_influence - rule_kind - manipulation_detection
- rule.pr_man_hidden_influence - label - 영향 의도·이해상충 비공개
- rule.pr_man_hidden_influence - level - warn
- rule.pr_man_hidden_influence - grades - B
- rule.pr_man_hidden_influence - part_of - concept.persuasion_research
- rule.pr_man_hidden_influence - evidence_grade - concept.evidence_grade_b
- rule.pr_man_hidden_influence - detector - {"input": "conflict_of_interest", "disclosure": "이해관계|후원|광고|협찬|수수료|제휴|저희\\s*(?:제품|회사)"}
- rule.pr_man_hidden_influence - when - [자료 내용] {"signal": "영향 의도·이해상충을 숨김"}
- rule.pr_man_hidden_influence - then - [자료 내용] {"verdict": "manipulation", "action": "의도·이해관계 공개 요구"}
- rule.pr_man_hidden_influence - severity - high
- rule.pr_man_hidden_influence - source - src:SUSSER2019 (https://doi.org/10.14763/2019.2.1410) [등급 B]
- rule.pr_man_hidden_influence - source - src:SUNSTEIN2016 (https://doi.org/10.1561/107.00000014) [등급 B]
- rule.pr_man_hidden_influence - source - src:FRIESTAD1994 (https://doi.org/10.1086/209380) [등급 B]
- rule.pr_man_hidden_influence - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 man.hidden_influence, 영향 의도·이해상충 비공개
