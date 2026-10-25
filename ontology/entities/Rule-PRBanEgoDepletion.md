---
id: rule.pr_ban_ego_depletion
type: Topic
updated: 2026-10-25
confidence: 0.7
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_ban_ego_depletion - kb_kind - research_rule
- rule.pr_ban_ego_depletion - orig_id - ban.ego_depletion
- rule.pr_ban_ego_depletion - rule_kind - evidence_ban
- rule.pr_ban_ego_depletion - label - 자아 고갈 이용 주장(D등급)
- rule.pr_ban_ego_depletion - level - block
- rule.pr_ban_ego_depletion - grades - D
- rule.pr_ban_ego_depletion - part_of - concept.persuasion_research
- rule.pr_ban_ego_depletion - evidence_grade - concept.evidence_grade_d
- rule.pr_ban_ego_depletion - detector - {"any": "(?:피곤할|지쳤을|지친|퇴근\\s*직전|진\\s*빠졌을)[^.!?\\n]{0,15}(?:때|틈)[^.!?\\n]{0,20}(?:설득|권유|제안|사인|서명|결정|계약)|의지력(?:이)?\\s*(?:고갈|바닥)"}
- rule.pr_ban_ego_depletion - when - [자료 내용] {"claim": "피곤할 때 설득하라/의지력 고갈 이용"}
- rule.pr_ban_ego_depletion - then - [자료 내용] {"action": "BLOCK(근거 D)"}
- rule.pr_ban_ego_depletion - source - src:HAGGER2016 (https://doi.org/10.1177/1745691616652873) [등급 D]
- rule.pr_ban_ego_depletion - source - src:VOHS2021 (https://doi.org/10.1177/0956797621989733) [등급 D]
- rule.pr_ban_ego_depletion - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 ban.ego_depletion, 자아 고갈 이용 주장(D등급)
