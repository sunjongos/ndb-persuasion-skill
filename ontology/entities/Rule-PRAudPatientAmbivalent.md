---
id: rule.pr_aud_patient_ambivalent
type: Topic
updated: 2026-10-25
confidence: 0.8
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_aud_patient_ambivalent - kb_kind - research_rule
- rule.pr_aud_patient_ambivalent - orig_id - aud.patient_ambivalent
- rule.pr_aud_patient_ambivalent - rule_kind - strategy_selection
- rule.pr_aud_patient_ambivalent - label - 양가감정 환자: MI·되말하기·SDM
- rule.pr_aud_patient_ambivalent - level - strategy
- rule.pr_aud_patient_ambivalent - grades - A/B
- rule.pr_aud_patient_ambivalent - part_of - concept.persuasion_research
- rule.pr_aud_patient_ambivalent - evidence_grade - concept.evidence_grade_a
- rule.pr_aud_patient_ambivalent - evidence_grade - concept.evidence_grade_b
- rule.pr_aud_patient_ambivalent - detector - {}
- rule.pr_aud_patient_ambivalent - when - [자료 내용] {"context": "clinic", "audience.state": "ambivalent"}
- rule.pr_aud_patient_ambivalent - then - [자료 내용] {"prefer": ["technique.mi", "technique.teach_back", "technique.sdm"], "avoid": ["정답 반사(righting reflex)", "공포만 강조"], "why": "MI 소규모지만 일관된 효과; SDM으로 가치 일치"}
- rule.pr_aud_patient_ambivalent - prefer - concept.technique_mi
- rule.pr_aud_patient_ambivalent - prefer - concept.technique_teach_back
- rule.pr_aud_patient_ambivalent - prefer - concept.technique_sdm
- rule.pr_aud_patient_ambivalent - avoid - 정답 반사(righting reflex)
- rule.pr_aud_patient_ambivalent - avoid - 공포만 강조
- rule.pr_aud_patient_ambivalent - source - src:LUNDAHL2013 (https://doi.org/10.1016/j.pec.2013.07.012) [등급 A]
- rule.pr_aud_patient_ambivalent - source - src:RUBAK2005 (https://pubmed.ncbi.nlm.nih.gov/15826439/) [등급 A]
- rule.pr_aud_patient_ambivalent - source - src:STACEY2024 (https://doi.org/10.1002/14651858.CD001431.pub6) [등급 A]
- rule.pr_aud_patient_ambivalent - source - src:TALEVSKI2020 (https://doi.org/10.1371/journal.pone.0231350) [등급 B]
- rule.pr_aud_patient_ambivalent - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 aud.patient_ambivalent, 양가감정 환자: MI·되말하기·SDM
