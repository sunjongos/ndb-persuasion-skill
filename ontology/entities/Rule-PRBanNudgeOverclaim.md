---
id: rule.pr_ban_nudge_overclaim
type: Topic
updated: 2026-10-25
confidence: 0.7
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_ban_nudge_overclaim - kb_kind - research_rule
- rule.pr_ban_nudge_overclaim - orig_id - ban.nudge_overclaim
- rule.pr_ban_nudge_overclaim - rule_kind - evidence_ban
- rule.pr_ban_nudge_overclaim - label - 논문 효과를 현장에 그대로 기대([해석] 8.7%p→1.4%p, 약 1/6)
- rule.pr_ban_nudge_overclaim - level - warn
- rule.pr_ban_nudge_overclaim - grades - A/C
- rule.pr_ban_nudge_overclaim - part_of - concept.persuasion_research
- rule.pr_ban_nudge_overclaim - evidence_grade - concept.evidence_grade_a
- rule.pr_ban_nudge_overclaim - evidence_grade - concept.evidence_grade_c
- rule.pr_ban_nudge_overclaim - detector - {"any": "(?:논문|연구)[^.!?\\n]{0,30}(?:그대로|똑같이)[^.!?\\n]{0,20}(?:효과|기대|나올)|넛지[^.!?\\n]{0,20}(?:확실|보장|무조건)"}
- rule.pr_ban_nudge_overclaim - when - [자료 내용] {"claim": "학술 논문 효과 크기를 현장에 그대로 기대"}
- rule.pr_ban_nudge_overclaim - then - [자료 내용] {"action": "현장 규모 할인(약 1/6) 경고"}
- rule.pr_ban_nudge_overclaim - source - src:DELLAV2022 (https://doi.org/10.3982/ECTA18709) [등급 A]
- rule.pr_ban_nudge_overclaim - source - src:MAIER2022 (https://doi.org/10.1073/pnas.2200300119) [등급 C]
- rule.pr_ban_nudge_overclaim - source - src:SACCARDO2024 (https://doi.org/10.1038/s41562%2D023%2D01813%2D4) [등급 A]
- rule.pr_ban_nudge_overclaim - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 ban.nudge_overclaim, 논문 효과를 현장에 그대로 기대([해석] 8.7%p→1.4%p, 약 1/6)
