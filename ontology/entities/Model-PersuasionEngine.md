---
id: model.persuasion_engine
type: Decision
updated: 2026-10-25
confidence: 0.8
source: 어시스턴트 구현 2026-10-25 (engine, 위키 밖 작업 폴더)
---
- model.persuasion_engine - kb_kind - engine
- model.persuasion_engine - is_a - model.ndb (뉴로심볼릭: LLM이 단서 추출·문장 초안, 기호 규칙이 검증·점수·차단)
- model.persuasion_engine - path - engine/engine.py (analyze 방어 / plan 공격 / check 윤리)
- model.persuasion_engine - knowledge_from - 이 위키의 설득 개체 → build_kb.py → knowledge.json
- model.persuasion_engine - implements - rule.persuasion_fact_gate
- model.persuasion_engine - implements - rule.persuasion_ethics_gate
- model.persuasion_engine - implements - concept.ceo_persuasion_philosophy
- model.persuasion_engine - uses - concept.persuasion_misjudgment
- model.persuasion_engine - limit - [해석] 키워드·정규식 기반이라 문맥을 놓칠 수 있다; LLM 단서와 사람 판단으로 보완
- model.persuasion_engine - version - 1.1 (2026-10-25: 심층연구 규칙 50·근거 등급 표시·청중 상태 전략·다크패턴·D등급 금지·하수/중수/고수 라벨)
- model.persuasion_engine - implements - concept.persuasion_research
- model.persuasion_engine - implements - principle.ceo_mastery_levels
> 검색어: 설득 엔진, 뉴로심볼릭, 설득 점검
