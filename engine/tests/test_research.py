# -*- coding: utf-8 -*-
"""심층연구 규칙 50(WIKI-CODE-022) 테스트: 규칙마다 1개 이상 + 의미 테스트. 실행: python3 -m unittest discover -s tests -v"""
import os, sys, re, json, unittest
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import engine
KB = engine.load_kb()
def EX(n):
    with open(os.path.join(ROOT, "examples", n + ".json"), encoding="utf-8") as f: return json.load(f)
F = lambda claim, kind, src="병원 EMR 2026 상반기": dict(claim=claim, source=src, verified=True, kind=kind)
FACTS = [F("검진 대상자 중 2026년 수검률은 61%", "statistic"), F("비수술 관리도 선택지입니다", "alternative")]
P = lambda goal, domain="general", **aud: dict(goal=goal, domain=domain, facts=FACTS, audience=aud)
C = lambda text, domain="general", **kw: dict(text=text, domain=domain, **kw)
GRADE_TAG = re.compile(r"^rule\.pr_\S+ \[근거 [A-D](?:/[A-D])*\] ")

# 규칙 id → (모드, 입력)
CASES = {
 "cue.repetition": ("check", C("이 약은 안전합니다. 이 약은 안전합니다. 이 약은 안전합니다.")),
 "cue.we_identity": ("check", C("우리가 함께 지켜 온 동네입니다.")),
 "cue.outgroup_hostility": ("check", C("저쪽 사람들은 배신자입니다.")),
 "cue.deadline_scarcity": ("check", C("오늘만 가능합니다.")),
 "cue.everyone_does": ("check", C("많은 분들이 이 검사를 받으십니다.")),
 "cue.authority": ("check", C("전문의가 권하는 검사입니다.")),
 "cue.placebic_reason": ("check", C("규정이 원래 그렇거든요.")),
 "cue.reciprocity_gift": ("check", C("작은 선물을 준비했습니다.")),
 "cue.fear_without_efficacy": ("check", C("방치하면 실명될 수 있습니다.")),
 "cue.narrative": ("check", C("한 환자분이 이 치료로 좋아지셨어요.")),
 "cue.commitment_ladder": ("check", C("일단 상담만 받아 보세요. 그럼 다음에 정하시면 돼요.")),
 "cue.ai_generated_mass": ("check", C("수치는 1, 2, 3, 4, 5입니다. AI로 작성했습니다.", ai_generated=True, accuracy_rechecked=True)),
 "aud.high_involvement": ("plan", P("무릎 수술 여부 상담", "hospital_consult")),
 "aud.low_involvement": ("plan", P("건강 캠페인 인식 개선", involvement="low")),
 "aud.opposed_identity": ("plan", P("정책 이해 높이기", prior_attitude="opposed", identity_threat="high")),
 "aud.opposed_low_identity": ("plan", P("정책 이해 높이기", prior_attitude="opposed", identity_threat="low")),
 "aud.undecided": ("plan", P("정책 이해 높이기", prior_attitude="undecided")),
 "aud.goal_behavior": ("plan", P("검진 예약 늘리기")),
 "aud.goal_attitude": ("plan", P("정책 이해 높이기")),
 "aud.patient_ambivalent": ("plan", P("치료 결정 상담", "hospital_consult", state="ambivalent")),
 "aud.staff_change": ("plan", P("이중 확인 지키기", "staff")),
 "aud.collectivist": ("plan", P("정책 이해 높이기", culture="collectivist")),
 "aud.campaign_late": ("plan", P("지지층 투표 참여", "politics", timing="late")),
 "aud.no_microtarget_overclaim": ("plan", P("개인 맞춤 메시지로 인식 개선")),
 "dp.false_scarcity": ("check", C("이번 달까지만 할인됩니다.")),
 "dp.confirmshaming": ("check", C("아니요, 저는 건강을 포기할게요.")),
 "dp.roach_motel": ("check", C("해지는 직접 방문해야 합니다.")),
 "dp.sneak_into_basket": ("check", C("보험이 자동으로 추가됩니다.")),
 "dp.nagging": ("check", C("동의하실 때까지 계속 연락드립니다.")),
 "dp.preselected_default": ("check", C("마케팅 수신이 미리 체크되어 있습니다.")),
 "dp.fake_social_proof": ("check", C("방금 김OO님이 예약했습니다.")),
 "man.impersonation": ("check", C("환자인 척 후기를 남기세요.")),
 "man.hidden_influence": ("check", C("이 기기를 추천합니다.", conflict_of_interest=True)),
 "man.repetition_without_evidence": ("check", C("이 약은 안전합니다. 이 약은 안전합니다. 이 약은 안전합니다.")),
 "man.consent_bypass": ("check", C("여기 서명만 해 주세요.", "hospital_consult")),
 "man.tares_fail": ("check", C("해지는 직접 방문해야 합니다.")),
 "man.lollapalooza_count": ("check", EX("consult_smuggler")),
 "ban.grade_D": ("check", C("상담 대본입니다.", techniques=["study.ego_depletion"])),
 "ban.ego_depletion": ("check", C("퇴근 직전 지쳤을 때 계약을 제안하세요.")),
 "ban.behavioral_priming": ("check", C("돈 사진을 보여 주면 더 이기적이 됩니다.")),
 "ban.backfire_excuse": ("check", C("정정하면 역효과가 나니 그냥 둡시다.")),
 "ban.loss_frame_always": ("check", C("손실 프레임이 항상 더 효과적입니다.")),
 "ban.nudge_overclaim": ("check", C("논문에서 나온 효과가 그대로 나올 겁니다.")),
 "fact.claims_sourced": ("check", C("검진을 권합니다.", facts=[dict(claim="효과 90%", source="", verified=False, kind="statistic")])),
 "fact.accuracy_after_optimization": ("check", C("AI로 다듬은 안내문입니다.", optimized=True)),
 "fact.no_fact_no_persuade": ("check", EX("consult_smuggler")),
 "fact.base_rate_for_story": ("check", C("한 환자분이 이 치료로 좋아지셨어요.")),
 "fact.disclose_ai": ("check", C("검진 안내문입니다.", ai_generated=True, accuracy_rechecked=True)),
 "fact.two_sided": ("plan", dict(goal="무릎 수술 여부 상담", domain="hospital_consult", facts=[F("MRI상 연골 손상 3도", "outcome_data")])),
 "fact.behavior_ask_after_facts": ("check", C("검진을 예약해 주세요.")),
}

def run(mode, inp): return getattr(engine, mode)(KB, json.loads(json.dumps(inp)))

class TestEveryRule(unittest.TestCase):
    def test_r00_all_50_rules_have_case(self):
        self.assertEqual(len(KB["research_rules"]), 50)
        self.assertEqual(set(CASES), set(KB["research_rules"]))
    def test_r01_each_rule_fires_with_grade(self):
        for orig, (mode, inp) in CASES.items():
            with self.subTest(rule=orig):
                rid = KB["research_rules"][orig]["id"]
                r = run(mode, inp)
                hit = [x for x in r["rules_fired"] if x.startswith(rid + " ")]
                self.assertTrue(hit, f"{orig} 미발동: {r['rules_fired']}")
                self.assertRegex(hit[0], GRADE_TAG)
                self.assertIn(f"[근거 {KB['research_rules'][orig]['grades']}]", hit[0])
                self.assertIn("(출처: ", hit[0])

class TestKBResearch(unittest.TestCase):
    def test_r02_kb_counts_and_sources(self):
        self.assertEqual(len(KB["research_items"]), 69); self.assertEqual(sorted(KB["grades"]), list("ABCD"))
        self.assertEqual(len(KB["findings"]), 7); self.assertEqual(len(KB["sources"]), 149)
        for r in KB["research_rules"].values():
            for s in r["sources"]: self.assertIn(s, KB["sources"])
        self.assertTrue(all(it["replication_failed"] for it in KB["research_items"].values() if it["grade"] == "D"))
        self.assertTrue(all("-" in s["url"] or "http" in s["url"] for s in KB["sources"].values()))
    def test_r03_old_rules_tagged_pdf(self):
        r = engine.analyze(KB, EX("consult_smuggler"))
        old = [x for x in r["rules_fired"] if not x.startswith("rule.pr_")]
        self.assertTrue(old); self.assertTrue(all(x.endswith("[근거: PDF 「설득과 오판」]") for x in old))

class TestGradeD(unittest.TestCase):
    def test_r04_d_grade_technique_blocked_in_check(self):
        r = run("check", C("상담 대본입니다.", techniques=["자아 고갈"]))
        self.assertEqual(r["verdict"], "BLOCK"); self.assertIn("ban.grade_D", {i["code"] for i in r["issues"]})
    def test_r05_d_grade_technique_removed_in_plan(self):
        r = run("plan", dict(P("검진 예약 늘리기"), techniques=["study.behavioral_priming", "technique.byaf"]))
        self.assertEqual(r["status"], "OK")
        bl = {b["technique"] for b in r["strategy"]["blocked_techniques"]}
        self.assertIn("concept.study_behavioral_priming", bl)
        self.assertNotIn("concept.study_behavioral_priming", {p["technique"] for p in r["strategy"]["prefer"]})
        self.assertTrue(any("D등급" in f for f in r["forbidden_tactics"]))
    def test_r06_ego_depletion_and_priming_claims(self):
        self.assertEqual(run("check", C("퇴근 직전 지쳤을 때 계약을 제안하세요."))["verdict"], "BLOCK")
        r = run("check", C("정정해도 역효과는 드뭅니다."))
        self.assertNotIn("ban.backfire_excuse", {i["code"] for i in r["issues"]})

class TestStrategy(unittest.TestCase):
    def pref(self, r): return {p["technique"] for p in r["strategy"]["prefer"]}
    def test_r07_opposed_high_identity(self):
        r = run("plan", P("정책 이해 높이기", prior_attitude="opposed", identity_threat="high"))
        self.assertTrue({"concept.technique_moral_reframing", "concept.technique_deep_canvassing", "concept.technique_byaf"} <= self.pref(r))
        self.assertTrue(r["strategy"]["byaf"]["recommended"]); self.assertIn("조롱", r["strategy"]["avoid"])
    def test_r08_opposed_low_identity_uses_evidence(self):
        r = run("plan", P("정책 이해 높이기", prior_attitude="opposed", identity_threat="low"))
        self.assertIn("rule.pr_aud_opposed_low_identity", r["strategy"]["selected_rules"])
        self.assertNotIn("rule.pr_aud_opposed_identity", r["strategy"]["selected_rules"])
    def test_r09_goal_type_inferred(self):
        b = run("plan", P("검진 예약 늘리기")); a = run("plan", P("정책 이해 높이기"))
        self.assertEqual(b["strategy"]["goal_type"], "behavior"); self.assertEqual(a["strategy"]["goal_type"], "attitude")
        self.assertEqual(b["strategy"]["behavior_sequence"][1], "자율 강조(BYAF)")
        self.assertNotIn("behavior_sequence", a["strategy"])
    def test_r10_campaign_late_and_collectivist_default(self):
        r = run("plan", P("지지층 투표 참여", "politics", timing="late"))
        self.assertIn("rule.pr_aud_campaign_late", r["strategy"]["selected_rules"])
        self.assertIn("rule.pr_aud_collectivist", r["strategy"]["selected_rules"])
        self.assertEqual(r["strategy"]["audience"]["culture"], "collectivist")
    def test_r11_staff_and_patient(self):
        s = run("plan", P("이중 확인 지키기", "staff")); h = run("plan", P("치료 결정 상담", "hospital_consult", state="ambivalent"))
        self.assertIn("rule.pr_aud_staff_change", s["strategy"]["selected_rules"])
        self.assertIn("rule.pr_aud_patient_ambivalent", h["strategy"]["selected_rules"])
        self.assertIn("rule.pr_aud_high_involvement", h["strategy"]["selected_rules"])

class TestDarkPatterns(unittest.TestCase):
    def test_r12_each_dark_pattern_blocks(self):
        for orig, (mode, inp) in CASES.items():
            if not orig.startswith("dp."): continue
            with self.subTest(rule=orig):
                r = run(mode, inp); self.assertEqual(r["verdict"], "BLOCK"); self.assertIn(orig, {i["code"] for i in r["issues"]})
                self.assertFalse(r["tares"]["respect"] and r["tares"]["equity"] and r["tares"]["truthfulness"])
    def test_r13_real_limit_allows_scarcity(self):
        r = run("check", C("이번 달까지만 할인됩니다.", facts=[F("할인은 2026-10-31 종료(공지 확정)", "real_limit")]))
        self.assertNotIn("dp.false_scarcity", {i["code"] for i in r["issues"]})

class TestBYAF(unittest.TestCase):
    def test_r14_request_without_byaf_suggests(self):
        r = run("check", C("검진을 예약해 주세요."))
        self.assertTrue(any("BYAF" in s for s in r["suggestions"])); self.assertEqual(r["verdict"], "PASS")
    def test_r15_request_with_byaf_no_suggestion(self):
        r = run("check", C("검진을 예약해 주세요. 결정은 환자분 몫이고 안 하셔도 괜찮습니다."))
        self.assertEqual(r["suggestions"], [])
    def test_r16_plan_hospital_recommends_byaf(self):
        r = run("plan", EX("plan_consult_facts")); self.assertTrue(r["strategy"]["byaf"]["recommended"])

class TestIllusoryTruth(unittest.TestCase):
    def test_r17_repetition_warns_without_facts(self):
        r = run("check", C("이 약은 안전합니다. 이 약은 안전합니다. 이 약은 안전합니다."))
        self.assertIn("cue.repetition", {i["code"] for i in r["info_flags"]})
        self.assertIn("man.repetition_without_evidence", {i["code"] for i in r["issues"]})
        self.assertNotEqual(r["verdict"], "PASS")
    def test_r18_repetition_with_facts_only_info(self):
        r = run("check", C("이 약은 안전합니다. 이 약은 안전합니다. 이 약은 안전합니다.", facts=[F("3상 시험 중대 이상반응 0.1%", "outcome_data")]))
        self.assertNotIn("man.repetition_without_evidence", {i["code"] for i in r["issues"]})
        self.assertIn("cue.repetition", {i["code"] for i in r["info_flags"]})

class TestMastery(unittest.TestCase):
    def test_r19_levels(self):
        self.assertEqual(run("check", EX("consult_smuggler"))["mastery"]["level"], "하수")
        d = run("check", EX("consult_detective")); self.assertEqual(d["verdict"], "PASS"); self.assertEqual(d["mastery"]["level"], "고수")
        self.assertEqual(run("check", C("한 환자분이 이 치료로 좋아지셨어요.", facts=FACTS))["mastery"]["level"], "중수")
        self.assertEqual(run("plan", EX("plan_no_facts"))["mastery"]["level"], "하수")
        self.assertEqual(run("plan", EX("plan_consult_facts"))["mastery"]["level"], "고수")
        self.assertIn("고수는 팩트 위에서 설득", d["mastery"]["maxim"])
    def test_r20_info_cues_do_not_change_verdict(self):
        r = run("check", C("우리가 함께 지켜 온 동네입니다.", facts=FACTS)); self.assertEqual(r["verdict"], "PASS", r["issues"])
        self.assertIn("cue.we_identity", {i["code"] for i in r["info_flags"]})
        a = engine.analyze(KB, C("규정이 원래 그렇거든요."))   # 연구 단서(info)만 있고 PDF 단서는 없음
        self.assertIn("cue.placebic_reason", {f["rule"] for f in a["research_flags"]})
        self.assertEqual(a["lollapalooza"]["score"], 0)

if __name__ == "__main__": unittest.main()
