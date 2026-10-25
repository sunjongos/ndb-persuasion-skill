---
id: rule.persuasion_fact_gate
type: Decision
updated: 2026-10-25
confidence: 0.9
source: 대표님 말씀 2026-10-25 대화 (설득 철학) + 웹 확인 2026-10-25: Stanford Encyclopedia of Philosophy 'Aristotle's Rhetoric', Petty & Cacioppo 1986 ELM (doi 10.1016/S0065-2601(08)60214-2) + 대표님 제공 PDF 「설득과 오판: 영향력의 과학 × 오판의 심리학」(NDB 남양주백병원 직원 교육자료, 16쪽, 2026-10) 2026-10-25 수신
---
- rule.persuasion_fact_gate - kb_kind - gate
- rule.persuasion_fact_gate - part_of - concept.ceo_persuasion_philosophy
- rule.persuasion_fact_gate - rule - 설득 계획 전에 검증된 팩트(출처·확인 여부)를 먼저 확인한다. 검증 팩트가 0개면 '사기꾼 영역'으로 차단하고 필요한 팩트를 요구한다
- rule.persuasion_fact_gate - rule - 각 설득 원칙은 자기 근거 팩트 종류가 확인될 때만 쓸 수 있다 (Tactic -requires- Fact)
- rule.persuasion_fact_gate - rule - 초안에 나온 수치는 검증 팩트 안에 있어야 한다. 없으면 '근거 없는 수치'로 수정 요구
- rule.persuasion_fact_gate - derived_from - principle.fact_before_persuasion
- rule.persuasion_fact_gate - derived_from - principle.fact_persuasion_matrix
- rule.persuasion_fact_gate - implemented_by - model.persuasion_engine
- rule.persuasion_fact_gate - fact_kind - fact:outcome_data (우리 병원·조직의 실제 결과 데이터)
- rule.persuasion_fact_gate - fact_kind - fact:statistic (비슷한 사람들의 실제 통계·사례(검증 가능))
- rule.persuasion_fact_gate - fact_kind - fact:credential (실제 전문 분야·경력·자격)
- rule.persuasion_fact_gate - fact_kind - fact:real_limit (실제 수량·기한·자원 제한)
- rule.persuasion_fact_gate - fact_kind - fact:favor (상대에게 먼저 준 실제 도움·가치)
- rule.persuasion_fact_gate - fact_kind - fact:shared_identity (실제 공유하는 소속·정체성·목표)
- rule.persuasion_fact_gate - fact_kind - fact:shared_trait (실제 공통점·진심 어린 인정 근거)
- rule.persuasion_fact_gate - fact_kind - fact:commitment (상대가 자발적으로 한 이전 약속·목표(본인 말))
- rule.persuasion_fact_gate - fact_kind - fact:reason (제안의 실제 이유(왜))
- rule.persuasion_fact_gate - fact_kind - fact:alternative (대안(비수술·경과 관찰 포함)과 장단점)
- rule.persuasion_fact_gate - fact_kind - fact:comparison (정직한 비교 기준(실제 가격·조건))
- rule.persuasion_fact_gate - grounded_by - concept.bias_persuasion_accuracy_tradeoff (설득력↑ → 정확도↓: 팩트 게이트의 실증 근거)
- rule.persuasion_fact_gate - fact_kind - fact:counterargument (주요 반대 근거와 그 반박(고관여·중대 결정))
- rule.persuasion_fact_gate - checklist - [자료 내용] 사업가 vs 사기꾼 판정표 7: 출처·최적화 후 정확도 재검사·반대 근거·의도/이해관계/AI 공개·BYAF·다크패턴 7종·D등급 기법 금지
- rule.persuasion_fact_gate - extended_by - concept.persuasion_research
> 검색어: 팩트 게이트, 사기꾼 차단, 근거 확인
