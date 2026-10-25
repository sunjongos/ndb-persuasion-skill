---
id: rule.pr_fact_disclose_ai
type: Topic
updated: 2026-10-25
confidence: 0.7
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_fact_disclose_ai - kb_kind - research_rule
- rule.pr_fact_disclose_ai - orig_id - fact.disclose_ai
- rule.pr_fact_disclose_ai - rule_kind - fact_gate
- rule.pr_fact_disclose_ai - label - AI 생성 메시지: AI 사용 공개
- rule.pr_fact_disclose_ai - level - warn
- rule.pr_fact_disclose_ai - grades - B/C
- rule.pr_fact_disclose_ai - part_of - concept.persuasion_research
- rule.pr_fact_disclose_ai - evidence_grade - concept.evidence_grade_b
- rule.pr_fact_disclose_ai - evidence_grade - concept.evidence_grade_c
- rule.pr_fact_disclose_ai - detector - {"input": "ai_generated", "disclosure": "AI|인공지능|생성형"}
- rule.pr_fact_disclose_ai - when - [자료 내용] {"signal": "AI 생성 설득 메시지"}
- rule.pr_fact_disclose_ai - then - [자료 내용] {"require": "AI 사용 공개 및 사칭 금지", "why": "라벨 공개해도 효과 유지 → 숨길 이유 없음"}
- rule.pr_fact_disclose_ai - source - src:BOISSIN2025 (https://doi.org/10.1093/pnasnexus/pgaf325) [등급 B]
- rule.pr_fact_disclose_ai - source - src:CMV2025 (https://www.science.org/content/article/unethical-ai-research-reddit-under-fire) [등급 C]
- rule.pr_fact_disclose_ai - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 fact.disclose_ai, AI 생성 메시지: AI 사용 공개
