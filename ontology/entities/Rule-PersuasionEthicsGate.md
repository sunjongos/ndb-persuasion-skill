---
id: rule.persuasion_ethics_gate
type: Decision
updated: 2026-10-25
confidence: 0.9
source: 대표님 말씀 2026-10-25 대화 (설득 철학) + 웹 확인 2026-10-25: Stanford Encyclopedia of Philosophy 'Aristotle's Rhetoric', Petty & Cacioppo 1986 ELM (doi 10.1016/S0065-2601(08)60214-2) + 대표님 제공 PDF 「설득과 오판: 영향력의 과학 × 오판의 심리학」(NDB 남양주백병원 직원 교육자료, 16쪽, 2026-10) 2026-10-25 수신
---
- rule.persuasion_ethics_gate - kb_kind - gate
- rule.persuasion_ethics_gate - part_of - concept.ceo_persuasion_philosophy
- rule.persuasion_ethics_gate - part_of - concept.persuasion_misjudgment
- rule.persuasion_ethics_gate - rule - 탐정만 허용, 밀수꾼 금지: 가짜 희귀성·조작된 사회적 증거·약점 압박·결정 시간 박탈 금지
- rule.persuasion_ethics_gate - rule - 투자 권유·수익 보장 문구는 어떤 경우에도 차단
- rule.persuasion_ethics_gate - rule - 외부 발송(메일·메시지·게시)은 대표님 승인 후에만
- rule.persuasion_ethics_gate - derived_from - concept.persuader_types
- rule.persuasion_ethics_gate - derived_from - principle.fact_before_persuasion
- rule.persuasion_ethics_gate - implemented_by - model.persuasion_engine
- rule.persuasion_ethics_gate - signal - M1 :: 가짜 희귀성(실제 제한 확인 없음) :: block :: 한정|마감|오늘만|선착순|품절|마지막\s*기회|남은\s*수량|카운트다운|까지만|곧\s*종료|단\s*하루 :: real_limit
- rule.persuasion_ethics_gate - signal - M2 :: 조작된 사회적 증거(통계 확인 없음) :: block :: \d[\d,]*\s*(명|분)(이|께서)?\s*(선택|구매|신청|가입|사용)|다들|모두가|대부분의\s*(분|사람)|1위|대세 :: statistic
- rule.persuasion_ethics_gate - signal - M3 :: 약점을 이용한 압박(불안+재촉) :: block :: (불안|두려|위험|큰일|늦으면|후회|악화|마비|평생).{0,40}(지금|오늘|당장|즉시|바로)|(지금|오늘|당장|즉시|바로).{0,40}(불안|큰일|늦으면|후회|악화|마비|평생) :: -
- rule.persuasion_ethics_gate - signal - M4 :: 수익 보장 :: block :: 수익\s*(을\s*)?보장|원금\s*(을\s*)?보장|확정\s*수익|손실\s*(이\s*)?없|무조건\s*(수익|오르|올라)|월\s*\d+\s*%\s*(수익)?|고수익\s*보장|\d+\s*배\s*(수익|상승)\s*(확정|보장) :: -
- rule.persuasion_ethics_gate - signal - M5 :: 투자 권유 :: block :: (매수|투자)\s*(하세요|하십시오|하셔야|추천)|종목\s*추천|리딩방|지금\s*사(세요|야)|급등\s*(예정|종목) :: -
- rule.persuasion_ethics_gate - signal - M6 :: 권위 부풀리기(자격 확인 없음) :: warn :: 국내\s*최고|세계적\s*권위|최고의\s*명의|명의|최고\s*권위자 :: credential
- rule.persuasion_ethics_gate - signal - M7 :: 대조 착시(작아 보이게 하기) :: warn :: 겨우|단돈|밖에\s*안|에\s*비하면 :: comparison
- rule.persuasion_ethics_gate - signal - M8 :: 결정 시간 박탈 :: block :: (오늘|지금|당장)\s*(바로\s*)?(결정|계약|결제|서명)|생각할\s*시간\s*(이\s*)?없 :: -
- rule.persuasion_ethics_gate - signal - M9 :: 가짜 '우리'(영업 맥락) :: warn :: 가족처럼|우리\s*사이에|형님\s*동생 :: shared_identity
- rule.persuasion_ethics_gate - signal - M10 :: 근거 없는 남 탓·싸움 프레임 :: warn :: 탓|책임은\s*(저들|그들)|심판|응징|전쟁|박살|몰락 :: -
> 검색어: 윤리 게이트, 조작 탐지, 다크 패턴, 투자 권유 차단
