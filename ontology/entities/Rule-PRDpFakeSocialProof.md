---
id: rule.pr_dp_fake_social_proof
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_dp_fake_social_proof - kb_kind - research_rule
- rule.pr_dp_fake_social_proof - orig_id - dp.fake_social_proof
- rule.pr_dp_fake_social_proof - rule_kind - manipulation_detection
- rule.pr_dp_fake_social_proof - label - 다크패턴: 가짜 후기·가짜 구매 알림
- rule.pr_dp_fake_social_proof - level - block
- rule.pr_dp_fake_social_proof - grades - B
- rule.pr_dp_fake_social_proof - part_of - concept.persuasion_research
- rule.pr_dp_fake_social_proof - evidence_grade - concept.evidence_grade_b
- rule.pr_dp_fake_social_proof - detector - {"any": "방금\\s*[^.!?\\n]{0,12}님이\\s*(?:구매|예약|신청)|지금\\s*\\d+\\s*명이\\s*(?:보고|구매)|실시간\\s*(?:구매|예약)", "unless_fact": "statistic"}
- rule.pr_dp_fake_social_proof - when - [자료 내용] {"pattern": "가짜 후기·가짜 구매 알림"}
- rule.pr_dp_fake_social_proof - then - [자료 내용] {"verdict": "manipulation", "action": "BLOCK + 대안(투명 표시) 제시"}
- rule.pr_dp_fake_social_proof - severity - high
- rule.pr_dp_fake_social_proof - source - src:MATHUR2019 (https://doi.org/10.1145/3359183) [등급 B]
- rule.pr_dp_fake_social_proof - source - src:GRAY2018 (https://doi.org/10.1145/3173574.3174108) [등급 B]
- rule.pr_dp_fake_social_proof - source - src:LUGURI2021 (https://doi.org/10.1093/jla/laaa006) [등급 B]
- rule.pr_dp_fake_social_proof - source - src:FTC2022 (https://www.ftc.gov/reports/bringing-dark-patterns-light) [등급 B]
- rule.pr_dp_fake_social_proof - source - src:DSA2022 (https://eur-lex.europa.eu/eli/reg/2022/2065/oj) [등급 B]
- rule.pr_dp_fake_social_proof - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 dp.fake_social_proof, 다크패턴: 가짜 후기·가짜 구매 알림
