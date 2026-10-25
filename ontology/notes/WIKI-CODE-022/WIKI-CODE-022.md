---
wiki_id: WIKI-CODE-022
title: "설득심리학 심층연구: 근거 등급·재현성·엔진 규칙"
entity: concept.persuasion_research
source: 설득심리학 심층연구 도시에 2026-10-25 (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)
created_at: 2026-10-25
note: 도시에 문구·수치 그대로 [자료 내용], 위키 연결·엔진 구현은 [해석]. 정치인 실명은 넣지 않았다(bot.politics). 외집단 적대 정규식의 정치 비하어는 탐지 패턴으로만 쓴다.
---
## 1. 본질
- [자료 내용] 사실은 엔진, 심리는 변속기.
- [해석] 행동·정체성·반복의 영역에서는 심리가 강하지만, 태도를 바꾸는 엔진은 팩트다. 설득-정확도 상충은 팩트 게이트의 실증 근거다.
- [해석] WIKI-CODE-020(PDF 도구)을 근거 등급으로 다시 거르고, WIKI-CODE-021(대표님 철학)에 찬반 증거를 붙인다.

## 2. 핵심 발견 7
1. **사실을 많이 줄수록 설득된다, 단 정확도와 맞바꾸는 함정** [자료 내용] 7.7만 명·AI 19종 실험: 설득력은 정보 밀도에서 나오고, 설득력을 끌어올리는 방법은 하나같이 사실 정확도를 떨어뜨렸다. 사실 근거를 막으면 효과가 크게 줄고, '사실 없이 설득하라' 조건은 효과 73% 감소 [HACKEN2025B][LIN2025][COSTELLO2025] — 등급 B → concept.pr_finding_fact_density
2. **태도와 행동은 다른 엔진** [자료 내용] 영국 약 1.5만 명 실험: AI 대화가 청원 서명을 약 19.7%p 늘렸으나 태도 변화와 행동 변화 효과는 상관이 없었다. 태도는 정보, 행동은 직접 요청·실행 계획·약속 단계 높이기 [HACKEN2026] — 등급 B → concept.pr_finding_attitude_behavior
3. **선거 막판 설득은 거의 효과가 없다** [자료 내용] 49개 현장 실험: 본선거 막판 대면·전화 접촉 설득 효과 평균 0에 가까움; 정치 광고 효과도 아주 작음; 심층 대화는 10분으로 몇 달 지속 [KALLA2018][COPPOCK2020][BROOCKMAN2016][KALLA2020] — 등급 A → concept.pr_finding_campaign_late
4. **사람들은 정보에 합리적으로 반응한다(평행 설득)** [자료 내용] 지지자·반대자가 같은 방향·비슷한 크기로 움직임; 정정 역효과(backfire)는 대규모 재현에서 거의 없음 → 원연구 D등급 [COPPOCK2023][WOOD2019][NYHAN2021] — 등급 A → concept.pr_finding_parallel
5. **반복은 사실을 이긴다(환상적 진실 효과)** [자료 내용] 반복해 들은 말은 더 참처럼 느껴짐(d≈0.4~0.5, 초록 기준); 정답을 알아도 완전히 막지 못함 [DECHENE2010][FAZIO2015] — 등급 A → concept.pr_finding_illusory_truth
6. **넛지·손실 프레임은 통념보다 약하다** [자료 내용] 학술 논문 평균 8.7%p 넛지 효과가 현장 넛지팀 실험에서 1.4%p; 출판 편향 보정 시 효과 없다는 분석도; 건강 메시지 손실/이득 프레임 차이 거의 없음; 사회 규범 비교 피드백은 현장 재현 [DELLAV2022][MAIER2022][OKEEFE2007][OKEEFE2009][ALLCOTT2011][HALLS2016] — 등급 A → concept.pr_finding_nudge_weak
7. **PDF 근거 일부는 재현 위기** [자료 내용] 자아 고갈(d≈0.04~0.06, 초록 기준)·행동/돈 점화는 D등급; 초전 설득의 '주의 초점'은 생존, 점화 주장은 엔진 금지; BYAF는 메타분석에서 승낙 확률 약 2배 [HAGGER2016][VOHS2021][DOYEN2012][ROHRER2015][CARPENTER2013] — 등급 A → concept.pr_finding_replication

## 3. 근거 등급
| 등급 | 뜻 | 개수 |
|---|---|---|
| A | 메타분석 또는 대규모 재현으로 확인 | 29 |
| B | 다수 연구로 지지(재현 일부) | 30 |
| C | 소수 연구·논쟁 중·동료심사 전 원고 | 7 |
| D | 재현 실패(엔진 추천 금지) | 3 |

D등급(재현 실패): concept.study_backfire_2010, concept.study_ego_depletion, concept.study_behavioral_priming → 엔진 추천 금지(ban.grade_D).

## 4. 개체 (이론·기법·연구·방어·편향·사례)
효과 크기는 모두 도시에 문구 그대로이며 원문 표와 대조하지 않았다(초록 기준).

| 이름 | 위키 id | 등급 | 효과 크기 | 출처 id |
|---|---|---|---|---|
| 정교화 가능성 모델 | concept.theory_elm | B | - | PETTY1986, PETTY1981 |
| 휴리스틱-체계 모델 | concept.theory_hsm | B | - | CHAIKEN1980 |
| 전망 이론 | concept.theory_prospect | A | 손실회피 계수 평균 약 2 안팎, 연구마다 편차 큼 (초록 기준) | KT1979, RUGGERI2020, BROWN2024 |
| 프레이밍 효과 | concept.theory_framing | A | - | TK1981 |
| 휴리스틱과 편향 | concept.theory_heuristics | A | - | TK1974, KLEIN2014 |
| 설득 지식 모델 | concept.theory_pkm | B | - | FRIESTAD1994 |
| 접종 이론·사전반박 | concept.theory_inoculation | A | - | MCGUIRE1961, BANAS2010, VDL2017, ROOZ2022, MODIR2023 |
| 서사 몰입(이동) 이론 | concept.theory_transportation | A | - | GREEN2000, VANLAER2014, BRADDOCK2016 |
| 도덕 기반 이론 | concept.theory_mft | B | - | GRAHAM2009 |
| 동기화된 추론 | concept.theory_motivated_reasoning | B | - | KUNDA1990, KAHAN2012, KAHAN2017, TAPPIN2020 |
| 정서적 양극화 | concept.theory_affective_polarization | B | - | IYENGAR2012, IYENGAR2019, VOELKEL2023, BROOCKMAN2023 |
| 심리적 반발 | concept.theory_reactance | A | - | BREHM1966, RAINS2013 |
| 동조 | concept.theory_conformity | A | - | ASCH1956, BOND1996, CIAL2004 |
| 침묵의 나선 | concept.theory_spiral_silence | B | 소(r≈0.05~0.1) (초록 기준) | NOELLE1974, GLYNN1997, MATTHES2018 |
| 환상적 진실 효과(반복=진실감) | concept.theory_illusory_truth | A | d≈0.4~0.5 (초록 기준) | DECHENE2010, FAZIO2015, HASSAN2021 |
| 선거 캠페인 최소 효과 | concept.theory_minimal_effects | A | 본선거 막판 접촉 설득 효과 평균 ≈0 (49개 현장 실험) (초록 기준) | KALLA2018, COPPOCK2020, HEWITT2024 |
| 평행 설득 | concept.theory_persuasion_parallel | A | - | COPPOCK2023, TAPPIN2023, GUESS2020, WOOD2019 |
| 포그 행동 모델(B=MAP) | concept.theory_fogg | C | - | FOGG2009 |
| 넛지·선택 설계 | concept.theory_nudge | B | 학술 논문 평균 8.7%p → 현장 넛지팀 1.4%p (초록 기준) | THALER2008, MERTENS2022, MAIER2022, DELLAV2022 |
| 조작의 정의 | concept.theory_manipulation_def | B | - | SUSSER2019, SUNSTEIN2016 |
| TARES 윤리 검사 | concept.theory_tares | B | - | BAKER2001 |
| 연대감(우리) | concept.technique_unity | B | - | CIAL2021, MOGAN2017 |
| 심층 대화(판단 없는 이야기 교환) | concept.technique_deep_canvassing | B | 10분 대화로 효과가 몇 달 지속 (초록 기준) | BROOCKMAN2016, KALLA2020, KALLA2023 |
| 도덕 재구성 | concept.technique_moral_reframing | B | - | FEINBERG2015, FEINBERG2019 |
| 양면 반박 메시지 | concept.technique_two_sided_refutational | A | - | OKEEFE1999 |
| 증거·정보 밀도 | concept.technique_evidence | A | - | REINARD1988, HACKEN2025B, LIN2025, COSTELLO2025 |
| "선택은 자유입니다" | concept.technique_byaf | A | 승낙 확률 약 2배(메타분석) (초록 기준) | CARPENTER2013 |
| 큰 요청 후 작은 요청 | concept.technique_ditf | B | - | FEELEY2012 |
| 작은 요청 후 큰 요청 | concept.technique_fitd | B | - | BURGER1999 |
| 이유 대기 | concept.technique_reason_because | C | - | LANGER1978 |
| 사회 규범 피드백 | concept.technique_social_norms | A | - | ALLCOTT2011, HALLS2017, HALLS2016 |
| 기본값 설정 | concept.technique_default | A | d≈0.68 (초록 기준) | JACHIM2019, JOHNSON2003 |
| 실행 의도("언제·어디서·어떻게") | concept.technique_implementation_intention | A | - | SHEERAN2025, HACKEN2026 |
| 직접 요청·약속 단계 높이기 | concept.technique_direct_ask | B | - | HACKEN2026 |
| 문자 알림(예약됨 표현) | concept.technique_reminder_text | A | - | MILKMAN2021, SACCARDO2024 |
| 동기강화상담 | concept.technique_mi | A | - | MILLER2023, LUNDAHL2010, LUNDAHL2013, RUBAK2005 |
| 공유 의사결정·결정보조도구 | concept.technique_sdm | A | - | ELWYN2012, STACEY2024 |
| 되말하기 확인 | concept.technique_teach_back | B | - | SCHILL2003, TALEVSKI2020 |
| 공감적 진료 소통 | concept.technique_empathic_comm | B | - | ZOLNIEREK2009, HOWICK2018, KELLEY2014 |
| 공포 소구+실행 가능성 | concept.technique_fear_efficacy | A | d≈0.29 (초록 기준) | TANNEN2015, WITTE2000 |
| 손실/이득 프레임(건강) | concept.technique_loss_frame | A | - | OKEEFE2007, OKEEFE2009, GAL2018 |
| 정확성 환기 | concept.technique_accuracy_prompt | B | - | PENNY2021 |
| 감정 이름 붙이기 | concept.technique_affect_labeling | B | - | LIEBERMAN2007, VOSS2016 |
| 관점 수용 | concept.technique_perspective_taking | B | - | GALINSKY2008, GALINSKY2001, FISHER1981 |
| 전략적 모방 | concept.technique_mimicry | C | - | MADDUX2008 |
| AI 대화 설득 | concept.technique_ai_dialogue | B | - | COSTELLO2024, BOISSIN2025, SALVI2025, BAI2025, HACKEN2025A, HACKEN2026B, SCHOEN2025, GOLDSTEIN2024 |
| 마이크로타기팅 | concept.technique_microtargeting | C | - | HACKEN2024, TAPPIN2023B, SIMCHON2024, MATZ2024, HACKEN2025B |
| 코터 8단계 변화관리 | concept.technique_kotter | C | - | KOTTER1995, APPEL2012 |
| 설득-정확도 상충 | concept.bias_persuasion_accuracy_tradeoff | B | - | HACKEN2025B, LIN2025, SCHOEN2025 |
| 태도-행동 간극 | concept.bias_attitude_behavior_gap | B | - | HACKEN2026 |
| 밴드왜건 효과 | concept.bias_bandwagon | C | - | BARNFIELD2020, ROTHSCHILD2014 |
| 네거티브 캠페인 | concept.bias_negativity_campaign | A | - | LAU2007 |
| 사전 반박 | concept.defense_prebunk | A | - | ROOZ2022, BANAS2010, MODIR2023 |
| 사후 정정 | concept.defense_correction | A | 정정 d≈1.14, 잔존 d≈0.75 (CHAN2017) (초록 기준) | WALTER2018, CHAN2017, ECKER2022, NYHAN2021 |
| 반발 완화 | concept.defense_reactance_soften | A | - | RAINS2013, CARPENTER2013 |
| 다크패턴 점검 | concept.defense_dark_pattern_audit | B | - | MATHUR2019, GRAY2018, LUGURI2021, FTC2022, DSA2022 |
| 설명 동의 기준 | concept.defense_informed_consent | B | - | MONTGOMERY2015, KRMEDLAW, BLUMEN2012 |
| 정정 역효과 원연구 | concept.study_backfire_2010 | D | - | NYHAN2010, WOOD2019, SWIRE2020 |
| 자아 고갈 | concept.study_ego_depletion | D | d≈0.04~0.06 (초록 기준) | HAGGER2016, VOHS2021 |
| 행동·돈 점화 | concept.study_behavioral_priming | D | - | DOYEN2012, ROHRER2015, KLEIN2014 |
| 재현 프로젝트 | concept.study_replication | A | 100편 중 약 36%만 유의 재현, 효과 크기 절반 (초록 기준) | OSC2015, KLEIN2014, KLEIN2018 |
| 밀그램 부분 재현 | concept.study_milgram_rep | B | 150V 지점에서 70% 계속(부분 재현) (초록 기준) | BURGER2009 |
| AI 정치 행동 설득 | concept.study_ai_petition_2026 | B | 청원 서명 약 19.7%p 증가 (초록 기준) | HACKEN2026 |
| AI 설득의 지렛대 | concept.study_ai_levers_2025 | B | - | HACKEN2025B |
| AI 대화와 유권자 | concept.study_ai_voters_2025 | B | - | LIN2025 |
| 취리히대 무동의 AI 레딧 실험 | concept.case_cmv_zurich | C | - | CMV2025 |
| 오파워 에너지 보고서 | concept.case_opower | A | 전력 약 2% 절감 (초록 기준) | ALLCOTT2011 |
| 영국 항생제 처방 편지 | concept.case_uk_antibiotics | A | - | HALLS2016 |
| 독감 백신 문자 메가연구 | concept.case_flu_megastudy | A | - | MILKMAN2021 |

## 5. 엔진 규칙 50 (rule.pr_*)
| 규칙 | 종류 | 수준 | 등급 | 설명 |
|---|---|---|---|---|
| cue.repetition | cue_detection | info | A | 반복 단서(환상적 진실 효과) |
| cue.we_identity | cue_detection | info | A/B | '우리' 정체성 단서(연대감) |
| cue.outgroup_hostility | cue_detection | warn | B | 외집단 적대 표현(정서적 양극화) |
| cue.deadline_scarcity | cue_detection | info | A/B | 기한·희소성 단서 |
| cue.everyone_does | cue_detection | info | A/C | 다수 단서(사회적 증거) |
| cue.authority | cue_detection | info | B | 권위 단서 |
| cue.placebic_reason | cue_detection | info | C | 빈 이유(요청 반복형 '때문에') |
| cue.reciprocity_gift | cue_detection | info | A/B | 선물·양보 단서(상호성) |
| cue.fear_without_efficacy | cue_detection | warn | A | 공포만 있고 실행 방법(효능감) 없음 |
| cue.narrative | cue_detection | warn | A/C | 사례 이야기 중심·통계 없음 |
| cue.commitment_ladder | cue_detection | info | B | 작은 동의 → 큰 요청(문간에 발) |
| cue.ai_generated_mass | cue_detection | warn | B | AI 고밀도 주장 → 무작위 3개 표본 사실검증 |
| aud.high_involvement | strategy_selection | strategy | A/B | 고관여: 증거·양면 반박 |
| aud.low_involvement | strategy_selection | strategy | A/B | 저관여: 신뢰 출처·간결한 핵심 사실(팩트 게이트 필수) |
| aud.opposed_identity | strategy_selection | strategy | A/B | 반대+정체성 위협: 도덕 재구성·심층 대화·BYAF |
| aud.opposed_low_identity | strategy_selection | strategy | A | 반대+정체성 위협 낮음: 증거·상세 정정 |
| aud.undecided | strategy_selection | strategy | A | 중립: 양면 반박·공유 의사결정 |
| aud.goal_behavior | strategy_selection | strategy | A/B | 행동 목표: 직접 요청·실행 의도·알림 문자 |
| aud.goal_attitude | strategy_selection | strategy | B | 태도 목표: 증거·정보 밀도 |
| aud.patient_ambivalent | strategy_selection | strategy | A/B | 양가감정 환자: MI·되말하기·SDM |
| aud.staff_change | strategy_selection | strategy | A | 직원 관행 변화: 동료 비교 피드백·기본값 |
| aud.collectivist | strategy_selection | strategy | A | 집단주의 문화: 동조 압력↑ → 익명 반대 채널 |
| aud.campaign_late | strategy_selection | strategy | A | 선거 막판: 설득 효과≈0 → 동원 집중 |
| aud.no_microtarget_overclaim | strategy_selection | strategy | B | 개인 맞춤 효과 과대평가 경고 |
| dp.false_scarcity | manipulation_detection | block | B | 다크패턴: 가짜 희소성·카운트다운 |
| dp.confirmshaming | manipulation_detection | block | B | 다크패턴: 거절 수치심 문구 |
| dp.roach_motel | manipulation_detection | block | B | 다크패턴: 가입 쉽고 해지 어려움 |
| dp.sneak_into_basket | manipulation_detection | block | B | 다크패턴: 몰래 추가·숨은 비용 |
| dp.nagging | manipulation_detection | block | B | 다크패턴: 반복 강요(잔소리) |
| dp.preselected_default | manipulation_detection | block | B | 다크패턴: 불리한 사전 선택 |
| dp.fake_social_proof | manipulation_detection | block | B | 다크패턴: 가짜 후기·가짜 구매 알림 |
| man.impersonation | manipulation_detection | block | B/C | 사칭(가짜 정체성) |
| man.hidden_influence | manipulation_detection | warn | B | 영향 의도·이해상충 비공개 |
| man.repetition_without_evidence | manipulation_detection | warn | A | 근거 추가 없이 같은 주장 반복 |
| man.consent_bypass | manipulation_detection | block | B | 설명 동의 우회(의료법 제24조의2·Montgomery) |
| man.tares_fail | manipulation_detection | warn | B | TARES 실패 항목 있음 |
| man.lollapalooza_count | manipulation_detection | warn | A/B | 플래그 3개 이상 → 정지·검토 |
| ban.grade_D | evidence_ban | block | A | D등급(재현 실패) 기법 추천 금지 |
| ban.ego_depletion | evidence_ban | block | D | 자아 고갈 이용 주장(D등급) |
| ban.behavioral_priming | evidence_ban | warn | A/D | 행동 점화 주장(D등급, 재현 실패) |
| ban.backfire_excuse | evidence_ban | block | A | '정정하면 역효과' 핑계(D등급 근거) |
| ban.loss_frame_always | evidence_ban | warn | A | '손실 프레임이 항상 강하다'(근거 부족) |
| ban.nudge_overclaim | evidence_ban | warn | A/C | 논문 효과를 현장에 그대로 기대([해석] 8.7%p→1.4%p, 약 1/6) |
| fact.claims_sourced | fact_gate | warn | B | 출처 없는 사실 주장은 '의견'으로 표시 |
| fact.accuracy_after_optimization | fact_gate | warn | B/C | 설득력 최적화 후 정확도 재검사 필요 |
| fact.no_fact_no_persuade | fact_gate | block | B/C | 팩트 없는 설득(사기꾼 모드) |
| fact.base_rate_for_story | fact_gate | warn | A/C | 사례 이야기에 대표성·기저율 병기 |
| fact.disclose_ai | fact_gate | warn | B/C | AI 생성 메시지: AI 사용 공개 |
| fact.two_sided | fact_gate | warn | A | 고관여: 반대 근거 1개 이상 제시+반박 |
| fact.behavior_ask_after_facts | fact_gate | strategy | A/B | 행동 요청 순서: 사실 → 자율 강조(BYAF) → 구체 요청 → 실행계획 |

## 6. 이름 참조 매핑 주의
- Munger:#3 호감·#2 혐오: 번호·이름 뒤바뀜: 위키는 #2 호감(t02_liking)·#3 혐오(t03_disliking). 둘 다 연결
- Munger:#13 소유 효과: 번호·이름 불일치: 위키 #13은 과도한 낙관. 소유물 상실 반응은 #14 박탈 초반응에 해당해 t14로 근사 연결
- Defense:방어 프로토콜: 단일 개체 없음: PDF 통합 방어 프로토콜은 허브(concept.persuasion_misjudgment)와 롤라팔루자 체크리스트로 근사 연결
- Cialdini:초전 설득(주의): 초전 설득 중 '주의 초점'만 해당(점화 부분은 D등급). principle.cialdini_presuasion에 한정 주석
- theory.reactance counters technique.byaf: 방향 역전 의심 → 생략(technique.byaf counters theory.reactance만 유지)

## 7. 한계
- [자료 내용] 효과 크기 일부는 초록·기존 지식에서 가져옴 → 원문 표 대조 권장.
- [자료 내용] COSTELLO2025·HACKEN2026B·SCHOEN2025·ELSAYED2024는 동료심사 전 원고(C).
- [자료 내용] 대부분 WEIRD 표본, 한국 재현 부족.

## 8. 연결
- 위: concept.ceo_persuasion_philosophy (WIKI-CODE-021), principle.ceo_mastery_levels
- 확장 대상: concept.persuasion_misjudgment (WIKI-CODE-020)
- 출처: ref.persuasion_research_sources (149개, id·DOI)
- 실행: model.persuasion_engine (engine, v1.1)
