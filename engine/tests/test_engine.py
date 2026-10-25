# -*- coding: utf-8 -*-
"""설득 엔진 정답 심은 단위 테스트. 실행: python3 -m unittest discover -s tests -v"""
import os, sys, json, unittest, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import engine
KB = engine.load_kb()
def EX(n):
    with open(os.path.join(ROOT, "examples", n + ".json"), encoding="utf-8") as f: return json.load(f)
codes = lambda r: {i["code"] for i in r["issues"]}

class TestKnowledgeBase(unittest.TestCase):
    def test_01_kb_from_wiki_complete(self):
        self.assertEqual(len(KB["principles"]), 8)
        self.assertEqual(len(KB["tendencies"]), 25)
        self.assertEqual(sorted(t["number"] for t in KB["tendencies"].values()), list(range(1, 26)))
        for p in KB["principles"].values():          # 모든 triggers 대상이 실제 경향
            for t in p["triggers"]: self.assertIn(t, KB["tendencies"])
            self.assertTrue(p["requires"])           # Tactic -requires-> Fact
        self.assertIn("principle.cialdini_scarcity", KB["tendencies"]["concept.munger_t14_deprivation"]["triggered_by"])
        self.assertGreaterEqual(len(KB["signals"]), 10)

class TestFactGate(unittest.TestCase):
    def test_02_plan_without_facts_blocked(self):
        r = engine.plan(KB, EX("plan_no_facts"))
        self.assertEqual(r["status"], "BLOCKED"); self.assertEqual(r["gate"], "fact"); self.assertEqual(r["quadrant"], "사기꾼")
        self.assertTrue(any(x["kind"] == "core" for x in r["required_facts"]))
    def test_03_unverified_or_sourceless_facts_do_not_count(self):
        inp = {"goal": "직원 설득", "domain": "staff", "facts": [
            {"claim": "준수율 90%", "source": "", "verified": True, "kind": "statistic"},
            {"claim": "다들 좋아함", "source": "느낌", "verified": False}]}
        r = engine.plan(KB, inp)
        self.assertEqual(r["status"], "BLOCKED"); self.assertEqual(len(r["unverified_facts"]), 2)
    def test_04_check_persuasion_text_without_facts_blocked(self):
        r = engine.check(KB, {"text": "대학병원 교수님 추천, 다들 쓰는 제품입니다", "facts": []})
        self.assertEqual(r["verdict"], "BLOCK"); self.assertIn("F0", codes(r))

class TestHospitalConsult(unittest.TestCase):
    def test_05_smuggler_consult_blocked(self):
        r = engine.check(KB, EX("consult_smuggler"))
        self.assertEqual(r["verdict"], "BLOCK"); self.assertEqual(r["persuader_type"], "밀수꾼")
        self.assertTrue({"M1", "M2", "M3", "M8", "F0"} <= codes(r))
    def test_06_detective_consult_passes(self):
        r = engine.check(KB, EX("consult_detective"))
        self.assertEqual(r["verdict"], "PASS", r["issues"]); self.assertEqual(r["persuader_type"], "탐정")
        self.assertFalse(r["lollapalooza"]["suspected"])
    def test_07_plan_consult_with_facts(self):
        r = engine.plan(KB, EX("plan_consult_facts"))
        self.assertEqual(r["status"], "OK"); self.assertEqual(r["quadrant"], "리더")
        self.assertEqual(r["elm"]["route"], "중심 경로")
        self.assertEqual([s["part"] for s in r["message_order"]], ["logos", "ethos", "pathos"])
        self.assertGreater(r["message_order"][0]["weight"], r["message_order"][2]["weight"])
        names = [p["name"] for p in r["principle_combo"]]
        self.assertIn("권위", names); self.assertNotIn("희귀성", names)
        self.assertTrue(any("희귀성" in f for f in r["forbidden_tactics"]))
    def test_08_consult_missing_alternative_revise(self):
        inp = EX("plan_consult_facts"); facts = inp["facts"]
        r = engine.check(KB, {"domain": "hospital_consult", "facts": facts,
            "text": "척추 전문의로 15년 경력입니다. 92%가 6주 안에 복귀했습니다. 수술하시죠."})
        self.assertEqual(r["verdict"], "REVISE"); self.assertTrue({"H1", "H2", "H3"} <= codes(r))

class TestDeviceSales(unittest.TestCase):
    def test_09_device_sales_lollapalooza(self):
        r = engine.analyze(KB, EX("device_sales"))
        names = {p["name"] for p in r["principles"]}
        self.assertTrue({"상호성", "권위", "사회적 증거", "희귀성"} <= names)
        self.assertTrue(r["lollapalooza"]["suspected"]); self.assertEqual(r["lollapalooza"]["level"], "높음")
        self.assertIn("희귀성 멈춤", [d["name"] for d in r["defenses"]])
        self.assertIn("concept.lolla_winners_curse", [c["id"] for c in r["combos"]])
        c = engine.check(KB, EX("device_sales"))
        self.assertEqual(c["verdict"], "BLOCK"); self.assertTrue({"M1", "M6", "M7", "M8"} <= codes(c))
    def test_10_reciprocity_defense_recommended(self):
        r = engine.analyze(KB, {"text": "무료 샘플을 먼저 드렸으니 이번에 한번 써 보세요"})
        self.assertIn("concept.defense_reclassify_gift", [d["id"] for d in r["defenses"]])

class TestInvestment(unittest.TestCase):
    def test_11_investment_spam_blocked(self):
        r = engine.check(KB, EX("investment_spam"))
        self.assertEqual(r["verdict"], "BLOCK"); self.assertTrue({"M4", "M5", "M2", "M1"} <= codes(r))
    def test_12_investment_plan_blocked_even_with_facts(self):
        r = engine.plan(KB, {"goal": "고객이 이 종목을 매수하세요 라고 느끼게", "domain": "investment",
            "facts": [{"claim": "회사 매출 증가", "source": "공시", "verified": True, "kind": "statistic"}]})
        self.assertEqual(r["status"], "BLOCKED"); self.assertEqual(r["gate"], "ethics")
    def test_13_honest_disclaimer_not_flagged(self):
        r = engine.check(KB, {"text": "이 상품은 원금을 보장하지 않습니다. 지금 결정하실 필요는 없습니다.", "facts": []})
        self.assertNotIn("M8", codes(r)); self.assertNotIn("M4", codes(r))

class TestPolitics(unittest.TestCase):
    def test_14_political_hooks_detected(self):
        r = engine.analyze(KB, EX("political_message"))
        for h in ("싸움 구경", "남 안 되는 것", "새로운 것", "남 탓"): self.assertIn(h, r["mass_hooks"])
        self.assertTrue(any("밴드왜건" in k for k in r["mass_hooks"]))
        c = engine.check(KB, EX("political_message"))
        self.assertEqual(c["verdict"], "BLOCK"); self.assertIn("M10", codes(c)); self.assertIn("F0", codes(c))
    def test_15_political_plan_peripheral_route(self):
        r = engine.plan(KB, {"goal": "지역 공약 지지 얻기", "domain": "politics", "audience": {"involvement": "low"},
            "facts": [{"claim": "지역 주민 설문 62%가 교통 개선을 1순위로 꼽음", "source": "지역 설문(예시)", "verified": True, "kind": "statistic"}]})
        self.assertEqual(r["status"], "OK"); self.assertEqual(r["elm"]["route"], "주변 경로")
        self.assertEqual(r["quadrant"], "리더"); self.assertTrue(any("남 탓" in w for w in r["warnings"]))

class TestStaff(unittest.TestCase):
    def test_16_staff_plan_and_draft(self):
        r = engine.plan(KB, EX("staff_plan"))
        self.assertEqual(r["status"], "OK")
        self.assertEqual(r["principle_combo"][0]["name"], "연대감")
        self.assertEqual(r["draft_check"]["verdict"], "PASS", r["draft_check"]["issues"])
    def test_17_scholar_type_warning(self):
        r = engine.plan(KB, {"goal": "직원 교육 참여 늘리기", "domain": "staff",
            "facts": [{"claim": "교육 참여율 40%", "source": "교육팀 집계", "verified": True, "kind": "outcome_data"}]})
        self.assertEqual(r["status"], "OK"); self.assertEqual(r["quadrant"], "학자형")
        self.assertTrue(r["on_hold"])

class TestNeuralValidation(unittest.TestCase):
    def test_18_llm_cue_validation(self):
        r = engine.analyze(KB, {"text": "지금 신청하시면 사은품을 드립니다", "cues": [
            {"principle": "reciprocity", "evidence": "사은품을 드립니다"},
            {"principle": "authority", "evidence": "교수님이 추천"},
            {"tendency": "#99", "evidence": "지금 신청"}]})
        self.assertEqual(r["llm_cues"]["accepted"], 1)
        reasons = [x["reason"] for x in r["llm_cues"]["rejected"]]
        self.assertTrue(any("환각" in x for x in reasons)); self.assertTrue(any("없는" in x for x in reasons))
    def test_19_ungrounded_number(self):
        f = [{"claim": "재입원율 3%", "source": "QI", "verified": True, "kind": "outcome_data"}]
        r1 = engine.check(KB, {"text": "재입원율은 3%입니다.", "facts": f})
        r2 = engine.check(KB, {"text": "재입원율은 1%입니다.", "facts": f})
        self.assertNotIn("F1", codes(r1)); self.assertIn("F1", codes(r2))
    def test_20_real_scarcity_allowed_with_fact(self):
        f = [{"claim": "독감 백신 잔여 20도즈", "source": "약제부 재고", "verified": True, "kind": "real_limit"}]
        r = engine.check(KB, {"text": "백신 남은 수량이 20도즈라 예약 순서대로 접종합니다.", "facts": f})
        self.assertNotIn("M1", codes(r))

class TestCLI(unittest.TestCase):
    def test_21_cli_exit_codes(self):
        run = lambda m, n: subprocess.run([sys.executable, os.path.join(ROOT, "engine.py"), m, "--input", os.path.join(ROOT, "examples", n + ".json")], capture_output=True, text=True)
        self.assertEqual(run("plan", "plan_no_facts").returncode, 2)
        p = run("plan", "plan_consult_facts"); self.assertEqual(p.returncode, 0); self.assertEqual(json.loads(p.stdout)["status"], "OK")
        self.assertEqual(run("check", "consult_detective").returncode, 0)

if __name__ == "__main__":
    unittest.main()
