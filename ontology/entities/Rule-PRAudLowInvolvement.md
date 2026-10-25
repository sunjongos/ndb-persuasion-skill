---
id: rule.pr_aud_low_involvement
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_aud_low_involvement - kb_kind - research_rule
- rule.pr_aud_low_involvement - orig_id - aud.low_involvement
- rule.pr_aud_low_involvement - rule_kind - strategy_selection
- rule.pr_aud_low_involvement - label - 저관여: 신뢰 출처·간결한 핵심 사실(팩트 게이트 필수)
- rule.pr_aud_low_involvement - level - strategy
- rule.pr_aud_low_involvement - grades - A/B
- rule.pr_aud_low_involvement - part_of - concept.persuasion_research
- rule.pr_aud_low_involvement - evidence_grade - concept.evidence_grade_a
- rule.pr_aud_low_involvement - evidence_grade - concept.evidence_grade_b
- rule.pr_aud_low_involvement - detector - {}
- rule.pr_aud_low_involvement - when - [자료 내용] {"audience.involvement": "low"}
- rule.pr_aud_low_involvement - then - [자료 내용] {"prefer": ["신뢰 출처 명시", "간결한 핵심 사실", "기본값(이익 일치 시)"], "require": "FactGate 통과", "why": "주변경로 단서 영향 큼 — 단서도 진실해야"}
- rule.pr_aud_low_involvement - prefer - 신뢰 출처 명시
- rule.pr_aud_low_involvement - prefer - 간결한 핵심 사실
- rule.pr_aud_low_involvement - prefer - 기본값(이익 일치 시)
- rule.pr_aud_low_involvement - source - src:PETTY1986 (https://doi.org/10.1016/S0065-2601(08)60214-2) [등급 B]
- rule.pr_aud_low_involvement - source - src:CHAIKEN1980 (https://doi.org/10.1037/0022-3514.39.5.752) [등급 B]
- rule.pr_aud_low_involvement - source - src:JACHIM2019 (https://doi.org/10.1017/bpp.2018.43) [등급 A]
- rule.pr_aud_low_involvement - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 aud.low_involvement, 저관여: 신뢰 출처·간결한 핵심 사실(팩트 게이트 필수)
