# 설득 뉴로심볼릭 엔진 (persuasion-engine)

근거: 「설득과 오판: 영향력의 과학 × 오판의 심리학」(NDB 직원 교육, 2026-10) + 대표님 설득 원칙(WIKI-CODE-021, 최상위) + 설득심리학 심층연구(WIKI-CODE-022, 출처 149·규칙 50·근거 등급 A~D).
지식은 온톨로지 위키(`ontology`, WIKI-CODE-020·021·022)에서 나옵니다.

## 구조
- 신경 계층(엔진 밖, LLM): 문장에서 단서(cues) 뽑기, 초안 쓰기
- 기호 계층(이 엔진, 표준 라이브러리만): 단서 검증, 규칙 발화, 위험 점수, 팩트·윤리 게이트 차단

## 파일
- `rules_ext.py`: v1.1 연구 규칙 50 실행(탐지·청중 전략·TARES·하수/중수/고수)
- `engine.py`: CLI `python3 engine.py analyze|plan|check --input file.json`
- `knowledge.json`: 위키에서 만든 KB (`python3 build_kb.py`로 다시 생성)
- `build_kb.py`: 위키 entities의 `kb_kind` 트리플 → knowledge.json
- `tools/ontology_src.py`, `tools/build_wiki.py`: 위키 개체 작성 원본(재생성용)
- `tools/research_src.py`, `tools/build_research.py`: 심층연구 → WIKI-CODE-022 개체·규칙·노트 생성(멱등)
- `SCHEMA.md`: 입출력 JSON 스키마
- `examples/`: 진료 상담(밀수꾼·탐정), 계획(팩트 있음·없음), 의료기기 영업, 투자 스팸, 정치 메시지, 직원 설득, 다크패턴 점검(`check_dark_pattern.json`), 반대 청중 행동 계획(`plan_opposed_behavior.json`)
- `tests/test_engine.py`(21) + `tests/test_research.py`(21, 규칙 50개 subTest 포함): 42개 테스트 `python3 -m unittest discover -s tests -v`

## 갱신 순서
연구 자료 수정 시 `python3 tools/build_research.py` → 위키 수정 → `python3 build_kb.py` → 테스트 → 위키 nsm·lint·secscan 통과 확인.
