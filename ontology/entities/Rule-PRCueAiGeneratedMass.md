---
id: rule.pr_cue_ai_generated_mass
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_ai_generated_mass - kb_kind - research_rule
- rule.pr_cue_ai_generated_mass - orig_id - cue.ai_generated_mass
- rule.pr_cue_ai_generated_mass - rule_kind - cue_detection
- rule.pr_cue_ai_generated_mass - label - AI 고밀도 주장 → 무작위 3개 표본 사실검증
- rule.pr_cue_ai_generated_mass - level - warn
- rule.pr_cue_ai_generated_mass - grades - B
- rule.pr_cue_ai_generated_mass - part_of - concept.persuasion_research
- rule.pr_cue_ai_generated_mass - evidence_grade - concept.evidence_grade_b
- rule.pr_cue_ai_generated_mass - detector - {"input": "ai_generated", "numbers_min": 5}
- rule.pr_cue_ai_generated_mass - when - [자료 내용] {"signal": "짧은 시간에 대량·고밀도 주장, 출처 다수지만 검증 불가"}
- rule.pr_cue_ai_generated_mass - then - [자료 내용] {"flag": "ai_information_flood", "action": "무작위 3개 주장 표본 사실검증"}
- rule.pr_cue_ai_generated_mass - source - src:HACKEN2025B (https://doi.org/10.1126/science.aea3884) [등급 B]
- rule.pr_cue_ai_generated_mass - source - src:LIN2025 (https://doi.org/10.1038/s41586%2D025%2D09771%2D9) [등급 B]
- rule.pr_cue_ai_generated_mass - source - src:GOLDSTEIN2024 (https://doi.org/10.1093/pnasnexus/pgae034) [등급 B]
- rule.pr_cue_ai_generated_mass - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.ai_generated_mass, AI 고밀도 주장 → 무작위 3개 표본 사실검증
