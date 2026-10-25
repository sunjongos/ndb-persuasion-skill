---
id: rule.pr_man_impersonation
type: Topic
updated: 2026-10-25
confidence: 0.7
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_man_impersonation - kb_kind - research_rule
- rule.pr_man_impersonation - orig_id - man.impersonation
- rule.pr_man_impersonation - rule_kind - manipulation_detection
- rule.pr_man_impersonation - label - 사칭(가짜 정체성)
- rule.pr_man_impersonation - level - block
- rule.pr_man_impersonation - grades - B/C
- rule.pr_man_impersonation - part_of - concept.persuasion_research
- rule.pr_man_impersonation - evidence_grade - concept.evidence_grade_b
- rule.pr_man_impersonation - evidence_grade - concept.evidence_grade_c
- rule.pr_man_impersonation - detector - {"any": "(?:환자|피해자|전문가|의사|간호사)인\\s*척|행세", "input": "persona_verified=false"}
- rule.pr_man_impersonation - when - [자료 내용] {"signal": "가짜 정체성·사칭(피해자·전문가 행세)"}
- rule.pr_man_impersonation - then - [자료 내용] {"verdict": "manipulation", "action": "BLOCK"}
- rule.pr_man_impersonation - severity - critical
- rule.pr_man_impersonation - source - src:CMV2025 (https://www.science.org/content/article/unethical-ai-research-reddit-under-fire) [등급 C]
- rule.pr_man_impersonation - source - src:SUSSER2019 (https://doi.org/10.14763/2019.2.1410) [등급 B]
- rule.pr_man_impersonation - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 man.impersonation, 사칭(가짜 정체성)
