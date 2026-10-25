---
id: rule.pr_man_consent_bypass
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_man_consent_bypass - kb_kind - research_rule
- rule.pr_man_consent_bypass - orig_id - man.consent_bypass
- rule.pr_man_consent_bypass - rule_kind - manipulation_detection
- rule.pr_man_consent_bypass - label - 설명 동의 우회(의료법 제24조의2·Montgomery)
- rule.pr_man_consent_bypass - level - block
- rule.pr_man_consent_bypass - grades - B
- rule.pr_man_consent_bypass - part_of - concept.persuasion_research
- rule.pr_man_consent_bypass - evidence_grade - concept.evidence_grade_b
- rule.pr_man_consent_bypass - detector - {"any": "서명만|사인만|설명은\\s*(?:생략|나중에)|형식적인\\s*(?:거|절차)|읽어\\s*보실\\s*필요\\s*(?:없|는\\s*없)", "context": "clinic"}
- rule.pr_man_consent_bypass - when - [자료 내용] {"context": "clinic", "signal": "위험 설명 생략·서명만 받기"}
- rule.pr_man_consent_bypass - then - [자료 내용] {"verdict": "manipulation+legal_risk", "action": "BLOCK; 의료법 제24조의2·Montgomery 기준 설명"}
- rule.pr_man_consent_bypass - severity - critical
- rule.pr_man_consent_bypass - source - src:KRMEDLAW (https://law.go.kr/LSW/lsLawLinkInfo.do?chrClsCd=010202&lsId=001788&lsJoLnkSeq=1000180469&print=print) [등급 B]
- rule.pr_man_consent_bypass - source - src:MONTGOMERY2015 (https://www.supremecourt.uk/cases/uksc-2013-0136) [등급 B]
- rule.pr_man_consent_bypass - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 man.consent_bypass, 설명 동의 우회(의료법 제24조의2·Montgomery)
