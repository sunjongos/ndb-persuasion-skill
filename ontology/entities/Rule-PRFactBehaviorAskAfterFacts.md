---
id: rule.pr_fact_behavior_ask_after_facts
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_fact_behavior_ask_after_facts - kb_kind - research_rule
- rule.pr_fact_behavior_ask_after_facts - orig_id - fact.behavior_ask_after_facts
- rule.pr_fact_behavior_ask_after_facts - rule_kind - fact_gate
- rule.pr_fact_behavior_ask_after_facts - label - 행동 요청 순서: 사실 → 자율 강조(BYAF) → 구체 요청 → 실행계획
- rule.pr_fact_behavior_ask_after_facts - level - strategy
- rule.pr_fact_behavior_ask_after_facts - grades - A/B
- rule.pr_fact_behavior_ask_after_facts - part_of - concept.persuasion_research
- rule.pr_fact_behavior_ask_after_facts - evidence_grade - concept.evidence_grade_a
- rule.pr_fact_behavior_ask_after_facts - evidence_grade - concept.evidence_grade_b
- rule.pr_fact_behavior_ask_after_facts - detector - {"request": "해\\s*주세요|하세요|하시죠|해\\s*주시기|부탁드립니다|신청하|예약하|서명해", "byaf": "선택은[^.!?\\n]{0,15}(?:몫|자유)|결정은[^.!?\\n]{0,15}(?:몫|자유|하셔도)|안\\s*하셔도\\s*(?:괜찮|됩니다)|거절하셔도|자유롭게\\s*(?:결정|선택)"}
- rule.pr_fact_behavior_ask_after_facts - when - [자료 내용] {"goal": "behavior"}
- rule.pr_fact_behavior_ask_after_facts - then - [자료 내용] {"order": ["사실 제시", "자율 강조(BYAF)", "구체 요청", "실행계획"], "why": "정보는 태도, 요청은 행동 — 둘 다 필요, 사실이 먼저"}
- rule.pr_fact_behavior_ask_after_facts - source - src:HACKEN2026 (https://doi.org/10.1073/pnas.2611368123) [등급 B]
- rule.pr_fact_behavior_ask_after_facts - source - src:CARPENTER2013 (https://doi.org/10.1080/10510974.2012.727941) [등급 A]
- rule.pr_fact_behavior_ask_after_facts - source - src:SHEERAN2025 (https://doi.org/10.1080/10463283.2024.2334563) [등급 A]
- rule.pr_fact_behavior_ask_after_facts - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 fact.behavior_ask_after_facts, 행동 요청 순서: 사실 → 자율 강조(BYAF) → 구체 요청 → 실행계획
