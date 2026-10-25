---
id: rule.pr_ban_behavioral_priming
type: Topic
updated: 2026-10-25
confidence: 0.7
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
---
- rule.pr_ban_behavioral_priming - kb_kind - research_rule
- rule.pr_ban_behavioral_priming - orig_id - ban.behavioral_priming
- rule.pr_ban_behavioral_priming - rule_kind - evidence_ban
- rule.pr_ban_behavioral_priming - label - 행동 점화 주장(D등급, 재현 실패)
- rule.pr_ban_behavioral_priming - level - warn
- rule.pr_ban_behavioral_priming - grades - A/D
- rule.pr_ban_behavioral_priming - part_of - concept.persuasion_research
- rule.pr_ban_behavioral_priming - evidence_grade - concept.evidence_grade_a
- rule.pr_ban_behavioral_priming - evidence_grade - concept.evidence_grade_d
- rule.pr_ban_behavioral_priming - detector - {"any": "점화|프라이밍|단어\\s*하나로|이미지만\\s*보여\\s*줘도|돈\\s*사진"}
- rule.pr_ban_behavioral_priming - when - [자료 내용] {"claim": "단어·이미지 점화로 행동을 바꾼다"}
- rule.pr_ban_behavioral_priming - then - [자료 내용] {"action": "근거 D로 표시; 주의 초점(초전설득) 중 재현된 것만 허용"}
- rule.pr_ban_behavioral_priming - source - src:DOYEN2012 (https://doi.org/10.1371/journal.pone.0029081) [등급 D]
- rule.pr_ban_behavioral_priming - source - src:ROHRER2015 (https://doi.org/10.1037/xge0000058) [등급 D]
- rule.pr_ban_behavioral_priming - source - src:KLEIN2014 (https://doi.org/10.1027/1864-9335/a000178) [등급 A]
- rule.pr_ban_behavioral_priming - implemented_by - model.persuasion_engine
> 검색어: 설득 엔진 규칙 ban.behavioral_priming, 행동 점화 주장(D등급, 재현 실패)
