---
id: rule.pr_cue_fear_without_efficacy
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_cue_fear_without_efficacy - kb_kind - research_rule
- rule.pr_cue_fear_without_efficacy - orig_id - cue.fear_without_efficacy
- rule.pr_cue_fear_without_efficacy - rule_kind - cue_detection
- rule.pr_cue_fear_without_efficacy - label - 공포만 있고 실행 방법(효능감) 없음
- rule.pr_cue_fear_without_efficacy - level - warn
- rule.pr_cue_fear_without_efficacy - grades - A
- rule.pr_cue_fear_without_efficacy - part_of - concept.persuasion_research
- rule.pr_cue_fear_without_efficacy - evidence_grade - concept.evidence_grade_a
- rule.pr_cue_fear_without_efficacy - detector - {"threat": "위험|사망|죽|큰일|돌이킬\\s*수\\s*없|실명|마비|악화|치명", "efficacy": "방법|막(?:기|을|아|습니다)|지킬\\s*수|하시면\\s*됩니다|예방할\\s*수|줄일\\s*수|낮출\\s*수|치료할\\s*수|단계|계획|예약|할\\s*수\\s*있"}
- rule.pr_cue_fear_without_efficacy - when - [자료 내용] {"signal": "위협 강조 있음 AND 구체적 실행 방법 없음"}
- rule.pr_cue_fear_without_efficacy - then - [자료 내용] {"flag": "fear_no_efficacy", "action": "효능감 정보 추가 요구"}
- rule.pr_cue_fear_without_efficacy - source - src:WITTE2000 (https://doi.org/10.1177/109019810002700506) [등급 A]
- rule.pr_cue_fear_without_efficacy - source - src:TANNEN2015 (https://doi.org/10.1037/a0039729) [등급 A]
- rule.pr_cue_fear_without_efficacy - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 cue.fear_without_efficacy, 공포만 있고 실행 방법(효능감) 없음
