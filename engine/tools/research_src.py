# -*- coding: utf-8 -*-
"""설득심리학 심층연구(WIKI-CODE-022) 원천 정의.
입력: research/{ontology_additions.json, engine_rules_additions.json, sources.csv, dossier.md}
여기에는 (1) 이름 참조 → 위키 실제 id 매핑, (2) 도시에 문구 그대로의 수치(효과 크기는 '초록 기준'),
(3) 엔진 탐지식(정규식, [해석] 구현), (4) 핵심 발견 7·찬반 증거·대표님 3단계(하수·중수·고수)를 둔다."""

import os as _os
RESEARCH_DIR = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "research")
HUB = "concept.persuasion_research"
HUB_CODE = "WIKI-CODE-022"

GRADE_ID = {g: f"concept.evidence_grade_{g.lower()}" for g in "ABCD"}
GRADE_DEF = {
 "A": "메타분석 또는 대규모 재현으로 확인", "B": "다수 연구로 지지(재현 일부)",
 "C": "소수 연구·논쟁 중·동료심사 전 원고", "D": "재현 실패(엔진 추천 금지)"}
GRADE_CONF = {"A": 0.85, "B": 0.8, "C": 0.7, "D": 0.75}
REPL_FAILED = "concept.replication_failed"

def wid(orig):
    """연구 개체 원래 id(theory.elm 등) → 위키 id(concept.theory_elm). 위키 C2 참조 검사(ID_RE)가 잡을 수 있게 concept. 접두어."""
    pre, name = orig.split(".", 1)
    return f"concept.{pre}_{name}"

def camel(s): return "".join(p[:1].upper() + p[1:] for p in s.replace(".", "_").split("_"))
def wfile(orig): return f"Concept-PR{camel(orig)}.md"
def rid(orig): return "rule.pr_" + orig.replace(".", "_").lower()
def rfile(orig): return f"Rule-PR{camel(orig)}.md"

T = "concept.munger_"
TEND = {1: "t01_reward", 2: "t02_liking", 3: "t03_disliking", 4: "t04_doubt", 5: "t05_inconsistency", 6: "t06_curiosity",
        7: "t07_fairness", 8: "t08_envy", 9: "t09_reciprocity", 10: "t10_association", 11: "t11_denial", 12: "t12_self_regard",
        13: "t13_optimism", 14: "t14_deprivation", 15: "t15_social_proof", 16: "t16_contrast", 17: "t17_stress", 18: "t18_availability",
        19: "t19_use_it", 20: "t20_drug", 21: "t21_senescence", 22: "t22_authority", 23: "t23_twaddle", 24: "t24_reason", 25: "t25_lollapalooza"}
CIAL = {"권위": "authority", "사회적 증거": "social_proof", "상호성": "reciprocity", "연대감": "unity", "일관성": "consistency",
        "호감": "liking", "희귀성": "scarcity"}
# 이름 참조 매핑에서 정확히 맞지 않은 것(보고용)
UNMAPPED_NOTES = {
 "Munger:#3 호감·#2 혐오": "번호·이름 뒤바뀜: 위키는 #2 호감(t02_liking)·#3 혐오(t03_disliking). 둘 다 연결",
 "Munger:#13 소유 효과": "번호·이름 불일치: 위키 #13은 과도한 낙관. 소유물 상실 반응은 #14 박탈 초반응에 해당해 t14로 근사 연결",
 "Defense:방어 프로토콜": "단일 개체 없음: PDF 통합 방어 프로토콜은 허브(concept.persuasion_misjudgment)와 롤라팔루자 체크리스트로 근사 연결",
 "Cialdini:초전 설득(주의)": "초전 설득 중 '주의 초점'만 해당(점화 부분은 D등급). principle.cialdini_presuasion에 한정 주석",
}
APPROX = {}

def map_ref(ref):
    """이름 참조 → [위키 id]. 없으면 []"""
    import re
    r = ref.strip()
    if r.startswith("Cialdini:"):
        n = r.split(":", 1)[1]
        if n.startswith("초전"): return ["principle.cialdini_presuasion"]
        for k, v in CIAL.items():
            if n.startswith(k): return [f"principle.cialdini_{v}"]
        return []
    if r.startswith("Munger:"):
        if "#3 호감·#2 혐오" in r: return [T + TEND[2], T + TEND[3]]
        if "#13 소유" in r: return [T + TEND[14]]
        m = re.match(r"Munger:#(\d+)", r)
        return [T + TEND[int(m.group(1))]] if m else []
    if r == "Defense:5W": return ["concept.defense_5w"]
    if r == "Defense:두 트랙": return ["concept.defense_two_track"]
    if r == "Defense:반발 완화": return ["concept.defense_reactance_soften"]
    if r == "Defense:방어 프로토콜": return ["concept.persuasion_misjudgment", "concept.defense_lolla_checklist"]
    if r == "PDF:read-back": return ["concept.defense_readback"]
    if r == "FactGate": return ["rule.persuasion_fact_gate"]
    if r in GRADE_ID: return [GRADE_ID[r]]
    m = re.match(r"^(theory|technique|study|bias|defense|case)\.([a-z0-9_]+)", r)
    if m: return [wid(m.group(0))]
    return []

# 효과 크기: 도시에(dossier.md) 문구 그대로만. 모두 원문 표 미대조 → '초록 기준'
EFFECT = {
 "theory.prospect": "손실회피 계수 평균 약 2 안팎, 연구마다 편차 큼",
 "theory.spiral_silence": "소(r≈0.05~0.1)",
 "theory.illusory_truth": "d≈0.4~0.5",
 "theory.minimal_effects": "본선거 막판 접촉 설득 효과 평균 ≈0 (49개 현장 실험)",
 "theory.nudge": "학술 논문 평균 8.7%p → 현장 넛지팀 1.4%p",
 "technique.deep_canvassing": "10분 대화로 효과가 몇 달 지속",
 "technique.byaf": "승낙 확률 약 2배(메타분석)",
 "defense.correction": "정정 d≈1.14, 잔존 d≈0.75 (CHAN2017)",
 "study.ego_depletion": "d≈0.04~0.06",
 "study.replication": "100편 중 약 36%만 유의 재현, 효과 크기 절반",
 "study.milgram_rep": "150V 지점에서 70% 계속(부분 재현)",
 "study.ai_petition_2026": "청원 서명 약 19.7%p 증가",
 "case.opower": "전력 약 2% 절감",
 "technique.default": "d≈0.68",
 "technique.fear_efficacy": "d≈0.29",
}
# 도시에에 없는 수치를 지운 요약(그 외는 원문 요약 사용)
SUMMARY_FIX = {
 "theory.framing": "같은 사실도 표현 방식에 따라 선택이 달라짐.",
 "theory.nudge": "학술 논문 효과(8.7%p)보다 현장 규모 효과(1.4%p)가 훨씬 작음. 출판 편향 보정 시 효과 소멸 주장도.",
 "technique.byaf": "요청 끝에 자유를 강조하면(\"선택은 자유입니다\") 승낙 확률 약 2배(메타분석).",
 "technique.microtargeting": "개인 맞춤 메시지의 추가 효과는 작거나 불확실. 정보 질 개선이 더 큼. 과대평가 주의.",
 "case.cmv_zurich": "취리히대 연구진이 동의 없이 AI 댓글로 레딧 이용자를 설득: 정체성 사칭·개인정보 추론 → 윤리 위반.",
 "case.flu_megastudy": "여러 독감 백신 문자 메시지를 한 번에 비교한 메가연구. \"백신이 예약되어 있습니다\" 표현이 가장 효과적.",
}
DROP_TRIPLES = [("theory.reactance", "counters", "technique.byaf")]  # 방향 역전 의심: technique.byaf counters theory.reactance 만 유지

# ---------- 엔진 탐지식 ([해석] 구현) ----------
# level: info(표시만) / warn(수정 권고) / block(차단) / strategy(plan 전략)
DETECT = {
 "cue.repetition": ("info", {"any": r"반복|계속\s*말|다들\s*알다시피|몇\s*번이고", "same_claim_min": 3}, "반복 단서(환상적 진실 효과)"),
 "cue.we_identity": ("info", {"any": r"우리(?!\s*병원)\s|우리가|같은\s*편|한\s*식구|동문|고향"}, "'우리' 정체성 단서(연대감)"),
 "cue.outgroup_hostility": ("warn", {"any": r"저쪽|저들|배신자|적폐|빨갱이|토착왜구"}, "외집단 적대 표현(정서적 양극화)"),
 "cue.deadline_scarcity": ("info", {"any": r"오늘만|마감\s*임박|한정|남은\s*수량|지금\s*아니면"}, "기한·희소성 단서"),
 "cue.everyone_does": ("info", {"any": r"다들|대부분|%가\s*선택|1위|많은\s*분들이"}, "다수 단서(사회적 증거)"),
 "cue.authority": ("info", {"any": r"교수|전문의|박사|권위자|하버드|논문에\s*따르면"}, "권위 단서"),
 "cue.placebic_reason": ("info", {"any": r"(?:해야|하셔야)\s*(?:하기\s*때문|해서|하니까)|(?:규정|원래)\s*그렇(?:기\s*때문|거든)"}, "빈 이유(요청 반복형 '때문에')"),
 "cue.reciprocity_gift": ("info", {"any": r"무료로\s*드|선물|특별히\s*해\s*드|먼저\s*양보"}, "선물·양보 단서(상호성)"),
 "cue.fear_without_efficacy": ("warn", {"threat": r"위험|사망|죽|큰일|돌이킬\s*수\s*없|실명|마비|악화|치명",
     "efficacy": r"방법|막(?:기|을|아|습니다)|지킬\s*수|하시면\s*됩니다|예방할\s*수|줄일\s*수|낮출\s*수|치료할\s*수|단계|계획|예약|할\s*수\s*있"}, "공포만 있고 실행 방법(효능감) 없음"),
 "cue.narrative": ("warn", {"story": r"한\s*환자분|어떤\s*분이|제가\s*아는|실제로\s*한|저희\s*어머니|사연|경험담|후기를\s*보면", "number": r"\d"}, "사례 이야기 중심·통계 없음"),
 "cue.commitment_ladder": ("info", {"any": r"(?:일단|우선|먼저)[^.!?\n]{0,25}만[^\n]{0,60}?(?:그럼|그러면|이제|이왕)"}, "작은 동의 → 큰 요청(문간에 발)"),
 "cue.ai_generated_mass": ("warn", {"input": "ai_generated", "numbers_min": 5}, "AI 고밀도 주장 → 무작위 3개 표본 사실검증"),
 "aud.high_involvement": ("strategy", {}, "고관여: 증거·양면 반박"),
 "aud.low_involvement": ("strategy", {}, "저관여: 신뢰 출처·간결한 핵심 사실(팩트 게이트 필수)"),
 "aud.opposed_identity": ("strategy", {}, "반대+정체성 위협: 도덕 재구성·심층 대화·BYAF"),
 "aud.opposed_low_identity": ("strategy", {}, "반대+정체성 위협 낮음: 증거·상세 정정"),
 "aud.undecided": ("strategy", {}, "중립: 양면 반박·공유 의사결정"),
 "aud.goal_behavior": ("strategy", {}, "행동 목표: 직접 요청·실행 의도·알림 문자"),
 "aud.goal_attitude": ("strategy", {}, "태도 목표: 증거·정보 밀도"),
 "aud.patient_ambivalent": ("strategy", {}, "양가감정 환자: MI·되말하기·SDM"),
 "aud.staff_change": ("strategy", {}, "직원 관행 변화: 동료 비교 피드백·기본값"),
 "aud.collectivist": ("strategy", {}, "집단주의 문화: 동조 압력↑ → 익명 반대 채널"),
 "aud.campaign_late": ("strategy", {}, "선거 막판: 설득 효과≈0 → 동원 집중"),
 "aud.no_microtarget_overclaim": ("strategy", {"any": r"마이크로\s*타기팅|개인\s*맞춤|맞춤형\s*메시지|타기팅"}, "개인 맞춤 효과 과대평가 경고"),
 "dp.false_scarcity": ("block", {"any": r"카운트다운|\d+\s*분\s*후\s*(?:종료|마감)|품절\s*임박|마감\s*임박|\d+\s*개\s*남|오늘만|이번\s*달까지만", "unless_fact": "real_limit"}, "다크패턴: 가짜 희소성·카운트다운"),
 "dp.confirmshaming": ("block", {"any": r"(?:아니요|아니오|괜찮아요|됐어요)[,\s]*(?:저는|전|나는)?[^.!?\n]{0,25}(?:포기|싫어|필요\s*없|원하지\s*않|손해\s*볼게)"}, "다크패턴: 거절 수치심 문구"),
 "dp.roach_motel": ("block", {"any": r"(?:해지|탈퇴|환불|취소)[^.!?\n]{0,20}(?:방문해야|직접\s*방문|전화로만|서면으로만|불가)"}, "다크패턴: 가입 쉽고 해지 어려움"),
 "dp.sneak_into_basket": ("block", {"any": r"자동으로\s*추가|자동\s*포함|별도\s*고지\s*없이|숨은\s*비용|결제\s*(?:단계|시)\s*추가"}, "다크패턴: 몰래 추가·숨은 비용"),
 "dp.nagging": ("block", {"any": r"동의하실\s*때까지|계속\s*(?:알림|팝업|연락)|하루에도\s*여러\s*번|매번\s*(?:묻|팝업)"}, "다크패턴: 반복 강요(잔소리)"),
 "dp.preselected_default": ("block", {"any": r"미리\s*체크|자동\s*동의|기본으로\s*선택|체크되어\s*있|자동\s*가입|자동\s*연장"}, "다크패턴: 불리한 사전 선택"),
 "dp.fake_social_proof": ("block", {"any": r"방금\s*[^.!?\n]{0,12}님이\s*(?:구매|예약|신청)|지금\s*\d+\s*명이\s*(?:보고|구매)|실시간\s*(?:구매|예약)", "unless_fact": "statistic"}, "다크패턴: 가짜 후기·가짜 구매 알림"),
 "man.impersonation": ("block", {"any": r"(?:환자|피해자|전문가|의사|간호사)인\s*척|행세", "input": "persona_verified=false"}, "사칭(가짜 정체성)"),
 "man.hidden_influence": ("warn", {"input": "conflict_of_interest", "disclosure": r"이해관계|후원|광고|협찬|수수료|제휴|저희\s*(?:제품|회사)"}, "영향 의도·이해상충 비공개"),
 "man.repetition_without_evidence": ("warn", {"needs": "cue.repetition & 검증 팩트 0"}, "근거 추가 없이 같은 주장 반복"),
 "man.consent_bypass": ("block", {"any": r"서명만|사인만|설명은\s*(?:생략|나중에)|형식적인\s*(?:거|절차)|읽어\s*보실\s*필요\s*(?:없|는\s*없)", "context": "clinic"}, "설명 동의 우회(의료법 제24조의2·Montgomery)"),
 "man.tares_fail": ("warn", {"computed": "TARES 5항목"}, "TARES 실패 항목 있음"),
 "man.lollapalooza_count": ("warn", {"computed": "경향 3개 이상"}, "플래그 3개 이상 → 정지·검토"),
 "ban.grade_D": ("block", {"technique_grade": "D"}, "D등급(재현 실패) 기법 추천 금지"),
 "ban.ego_depletion": ("block", {"any": r"(?:피곤할|지쳤을|지친|퇴근\s*직전|진\s*빠졌을)[^.!?\n]{0,15}(?:때|틈)[^.!?\n]{0,20}(?:설득|권유|제안|사인|서명|결정|계약)|의지력(?:이)?\s*(?:고갈|바닥)"}, "자아 고갈 이용 주장(D등급)"),
 "ban.behavioral_priming": ("warn", {"any": r"점화|프라이밍|단어\s*하나로|이미지만\s*보여\s*줘도|돈\s*사진"}, "행동 점화 주장(D등급, 재현 실패)"),
 "ban.backfire_excuse": ("block", {"any": r"(?:정정|반박|바로잡)[^.!?\n]{0,15}(?:역효과|더\s*믿)", "except": r"드물|드뭅|없|아니|않"}, "'정정하면 역효과' 핑계(D등급 근거)"),
 "ban.loss_frame_always": ("warn", {"any": r"손실\s*(?:프레임|표현|메시지)[^.!?\n]{0,20}(?:항상|무조건|언제나|반드시)|(?:항상|무조건|언제나)[^.!?\n]{0,15}손실\s*(?:프레임|표현)"}, "'손실 프레임이 항상 강하다'(근거 부족)"),
 "ban.nudge_overclaim": ("warn", {"any": r"(?:논문|연구)[^.!?\n]{0,30}(?:그대로|똑같이)[^.!?\n]{0,20}(?:효과|기대|나올)|넛지[^.!?\n]{0,20}(?:확실|보장|무조건)"}, "논문 효과를 현장에 그대로 기대([해석] 8.7%p→1.4%p, 약 1/6)"),
 "fact.claims_sourced": ("warn", {"facts": "source 없음 → 의견"}, "출처 없는 사실 주장은 '의견'으로 표시"),
 "fact.accuracy_after_optimization": ("warn", {"input": "ai_generated|optimized, accuracy_rechecked"}, "설득력 최적화 후 정확도 재검사 필요"),
 "fact.no_fact_no_persuade": ("block", {"computed": "F0/팩트 게이트"}, "팩트 없는 설득(사기꾼 모드)"),
 "fact.base_rate_for_story": ("warn", {"needs": "cue.narrative"}, "사례 이야기에 대표성·기저율 병기"),
 "fact.disclose_ai": ("warn", {"input": "ai_generated", "disclosure": r"AI|인공지능|생성형"}, "AI 생성 메시지: AI 사용 공개"),
 "fact.two_sided": ("warn", {"counter": r"반면|단점|부작용|위험도|다만|그러나|대안", "fact_kinds": "alternative|comparison|counterargument"}, "고관여: 반대 근거 1개 이상 제시+반박"),
 "fact.behavior_ask_after_facts": ("strategy", {"request": r"해\s*주세요|하세요|하시죠|해\s*주시기|부탁드립니다|신청하|예약하|서명해",
     "byaf": r"선택은[^.!?\n]{0,15}(?:몫|자유)|결정은[^.!?\n]{0,15}(?:몫|자유|하셔도)|안\s*하셔도\s*(?:괜찮|됩니다)|거절하셔도|자유롭게\s*(?:결정|선택)"},
     "행동 요청 순서: 사실 → 자율 강조(BYAF) → 구체 요청 → 실행계획"),
}

# ---------- 핵심 발견 7 (도시에 1절, 수치 그대로) ----------
FINDINGS = [
 ("fact_density", "사실을 많이 줄수록 설득된다, 단 정확도와 맞바꾸는 함정",
  "7.7만 명·AI 19종 실험: 설득력은 정보 밀도에서 나오고, 설득력을 끌어올리는 방법은 하나같이 사실 정확도를 떨어뜨렸다. 사실 근거를 막으면 효과가 크게 줄고, '사실 없이 설득하라' 조건은 효과 73% 감소",
  ["HACKEN2025B", "LIN2025", "COSTELLO2025"], "B", ["concept.bias_persuasion_accuracy_tradeoff", "concept.technique_evidence", "rule.persuasion_fact_gate"], "supports"),
 ("attitude_behavior", "태도와 행동은 다른 엔진",
  "영국 약 1.5만 명 실험: AI 대화가 청원 서명을 약 19.7%p 늘렸으나 태도 변화와 행동 변화 효과는 상관이 없었다. 태도는 정보, 행동은 직접 요청·실행 계획·약속 단계 높이기",
  ["HACKEN2026"], "B", ["concept.bias_attitude_behavior_gap", "concept.technique_direct_ask", "concept.technique_implementation_intention", "principle.cialdini_consistency"], "qualifies"),
 ("campaign_late", "선거 막판 설득은 거의 효과가 없다",
  "49개 현장 실험: 본선거 막판 대면·전화 접촉 설득 효과 평균 0에 가까움; 정치 광고 효과도 아주 작음; 심층 대화는 10분으로 몇 달 지속",
  ["KALLA2018", "COPPOCK2020", "BROOCKMAN2016", "KALLA2020"], "A", ["concept.theory_minimal_effects", "concept.technique_deep_canvassing"], "qualifies"),
 ("parallel", "사람들은 정보에 합리적으로 반응한다(평행 설득)",
  "지지자·반대자가 같은 방향·비슷한 크기로 움직임; 정정 역효과(backfire)는 대규모 재현에서 거의 없음 → 원연구 D등급",
  ["COPPOCK2023", "WOOD2019", "NYHAN2021"], "A", ["concept.theory_persuasion_parallel", "concept.study_backfire_2010"], "supports"),
 ("illusory_truth", "반복은 사실을 이긴다(환상적 진실 효과)",
  "반복해 들은 말은 더 참처럼 느껴짐(d≈0.4~0.5, 초록 기준); 정답을 알아도 완전히 막지 못함",
  ["DECHENE2010", "FAZIO2015"], "A", ["concept.theory_illusory_truth", "concept.munger_t18_availability"], "supports_psychology"),
 ("nudge_weak", "넛지·손실 프레임은 통념보다 약하다",
  "학술 논문 평균 8.7%p 넛지 효과가 현장 넛지팀 실험에서 1.4%p; 출판 편향 보정 시 효과 없다는 분석도; 건강 메시지 손실/이득 프레임 차이 거의 없음; 사회 규범 비교 피드백은 현장 재현",
  ["DELLAV2022", "MAIER2022", "OKEEFE2007", "OKEEFE2009", "ALLCOTT2011", "HALLS2016"], "A", ["concept.theory_nudge", "concept.technique_loss_frame", "concept.technique_social_norms"], "qualifies"),
 ("replication", "PDF 근거 일부는 재현 위기",
  "자아 고갈(d≈0.04~0.06, 초록 기준)·행동/돈 점화는 D등급; 초전 설득의 '주의 초점'은 생존, 점화 주장은 엔진 금지; BYAF는 메타분석에서 승낙 확률 약 2배",
  ["HAGGER2016", "VOHS2021", "DOYEN2012", "ROHRER2015", "CARPENTER2013"], "A", ["concept.study_ego_depletion", "concept.study_behavioral_priming", "concept.technique_byaf", "principle.cialdini_presuasion"], "qualifies"),
]
PRO = [("반복이 진실감을 만들고 지식으로도 막지 못한다", ["DECHENE2010", "FAZIO2015", "HASSAN2021"]),
       ("정체성·감정이 먼저 움직인다(상대 당 혐오 > 정책 차이; 과학 지식이 많을수록 기후 인식이 더 갈라짐)", ["IYENGAR2012", "IYENGAR2019", "KAHAN2012"]),
       ("행동은 정보로 움직이지 않는다(직접 요청·약속, 사회 규범 비교, 이야기 교환)", ["HACKEN2026", "ALLCOTT2011", "HALLS2017", "KALLA2020"])]
CON = [("사실·정보 밀도가 설득의 주된 엔진; 사실을 막으면 설득이 무너진다", ["HACKEN2025B", "LIN2025", "COSTELLO2025"]),
       ("반대 진영 정보에도 같은 방향으로 움직이고 역효과는 드물다", ["COPPOCK2023", "WOOD2019", "GUESS2020", "TAPPIN2023"]),
       ("심리 기술 캠페인 효과는 작다(막판 접촉≈0, 네거티브는 신뢰만 하락, 맞춤 타기팅 추가 효과 미미)", ["KALLA2018", "LAU2007", "HACKEN2025B", "HACKEN2024"])]
CONCLUSION = "행동·정체성·반복의 영역에서는 심리가 강하지만, 태도를 바꾸는 엔진은 팩트다. 설득-정확도 상충은 팩트 게이트의 실증 근거다"
SYNTH = "사실은 엔진, 심리는 변속기"

# ---------- 대표님 새 격언(2026-10-25): 하수·중수·고수 ----------
MASTERY_ID = "principle.ceo_mastery_levels"
MAXIM = "하수는 팩트 없이 말하고, 중수는 팩트보다 설득에 기대고, 고수는 팩트 위에서 설득해 행동과 결과를 만든다."
LEVELS = [("하수", "팩트 없음", "남는 것 없음"),
          ("중수", "팩트보다 심리 기술", "일시적 효과, 검증 시 붕괴"),
          ("고수", "팩트+심리+행동 설계", "신뢰·행동·결과")]
STEPS = ["팩트 쌓기", "심리로 전달", "행동 설계: 구체적 요청·실행 계획·BYAF", "결과로 증명(결과가 다음 설득의 팩트)"]
