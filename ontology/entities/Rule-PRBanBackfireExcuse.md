---
id: rule.pr_ban_backfire_excuse
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_ban_backfire_excuse - kb_kind - research_rule
- rule.pr_ban_backfire_excuse - orig_id - ban.backfire_excuse
- rule.pr_ban_backfire_excuse - rule_kind - evidence_ban
- rule.pr_ban_backfire_excuse - label - '정정하면 역효과' 핑계(D등급 근거)
- rule.pr_ban_backfire_excuse - level - block
- rule.pr_ban_backfire_excuse - grades - A
- rule.pr_ban_backfire_excuse - part_of - concept.persuasion_research
- rule.pr_ban_backfire_excuse - evidence_grade - concept.evidence_grade_a
- rule.pr_ban_backfire_excuse - detector - {"any": "(?:정정|반박|바로잡)[^.!?\\n]{0,15}(?:역효과|더\\s*믿)", "except": "드물|드뭅|없|아니|않"}
- rule.pr_ban_backfire_excuse - when - [자료 내용] {"claim": "정정하면 역효과라 사실을 말하지 말자"}
- rule.pr_ban_backfire_excuse - then - [자료 내용] {"action": "BLOCK; 정정은 대체로 효과"}
- rule.pr_ban_backfire_excuse - source - src:WOOD2019 (https://doi.org/10.1007/s11109%2D018%2D9443%2Dy) [등급 A]
- rule.pr_ban_backfire_excuse - source - src:NYHAN2021 (https://doi.org/10.1073/pnas.1912440117) [등급 A]
- rule.pr_ban_backfire_excuse - source - src:WALTER2018 (https://doi.org/10.1080/03637751.2018.1467564) [등급 A]
- rule.pr_ban_backfire_excuse - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 ban.backfire_excuse, '정정하면 역효과' 핑계(D등급 근거)
