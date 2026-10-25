#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""설득 뉴로심볼릭 엔진 (기호 계층).
  analyze : 방어 모드 — 쓰인 설득 원칙·오판 경향 탐지, 롤라팔루자 위험 점수, 근거 규칙
  plan    : 공격 모드 — 팩트 게이트 → ELM 관여도 → 원칙 조합 → logos→ethos→pathos 순서 → 금지 기법
  check   : 윤리 점검 — 가짜 희귀성·조작된 사회적 증거·약점 압박·수익 보장·투자 권유 등 탐지
v1.1: 설득심리학 심층연구(WIKI-CODE-022) 규칙 50 — rules_fired에 근거 등급(A~D) 표시, 청중 상태 전략, 다크패턴 7종,
      D등급(재현 실패) 기법 금지, BYAF 제안, 환상적 진실(반복) 경고, TARES, 하수·중수·고수 라벨(principle.ceo_mastery_levels)
LLM(신경 계층)은 엔진 밖에서 단서(cues)와 초안(text)을 만든다. 엔진은 그것을 검증·채점·차단한다.
사용: python3 engine.py analyze|plan|check --input file.json [--kb knowledge.json]
표준 라이브러리만 사용."""
import os, re, sys, json, math, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rules_ext as X

HERE = os.path.dirname(os.path.abspath(__file__))
VERSION = "1.1"

def load_kb(path=None):
    return json.load(open(path or os.path.join(HERE, "knowledge.json"), encoding="utf-8"))

# ---------- 공통 ----------
DOMAIN_DEFAULT_INVOLVEMENT = {"hospital_consult": "high", "device_sales": "high", "investment": "high",
                              "politics": "low", "staff": "unknown", "general": "unknown"}
# 도메인별 추천 원칙(우선순위)과 도메인 금지 원칙
DOMAIN_PRINCIPLES = {
 "hospital_consult": ["authority", "consistency", "social_proof", "liking", "unity"],
 "device_sales":     ["authority", "social_proof", "reciprocity", "liking", "consistency"],
 "politics":         ["social_proof", "unity", "authority", "consistency", "liking"],
 "staff":            ["unity", "reciprocity", "consistency", "social_proof", "authority"],
 "investment":       ["authority", "social_proof"],
 "general":          ["authority", "social_proof", "reciprocity", "liking", "unity", "consistency"],
}
DOMAIN_FORBIDDEN_PRINCIPLES = {"hospital_consult": ["scarcity"], "staff": ["scarcity"]}
BASE_FORBIDDEN = [
 "가짜 희귀성: '이번 달까지만', '마감 임박' 등 실제 제한이 없는 기한·수량 (M1)",
 "조작된 사회적 증거: 근거 없는 '다들', 'N명 선택' (M2)",
 "불안을 키운 뒤 재촉하는 압박 (M3)",
 "수익 보장·원금 보장 문구 (M4)",
 "투자 권유·종목 추천 (M5)",
 "자격·경력 부풀리기 (M6)",
 "큰 금액을 먼저 보여 준 뒤 추가 비용을 작아 보이게 하는 대조 착시 (M7)",
 "그 자리에서 결정·계약을 요구해 생각할 시간을 빼앗기 (M8)",
 "근거 없는 남 탓·싸움 프레임 (M10)",
 "로우볼: 동의를 받은 뒤 조건을 바꾸기",
]
DOMAIN_FORBIDDEN = {
 "hospital_consult": ["대안(비수술·경과 관찰) 빼고 한 가지 치료만 제시", "이유 없이 결정 요구", "집에서 생각할 시간 주지 않기"],
 "politics": ["지지율·여론 수치 부풀리기(밴드왜건 조작)", "사실 확인 안 된 상대 비난"],
 "staff": ["보상·불이익으로만 몰아붙이기(#1 과신)", "이유(왜) 없는 지시"],
 "device_sales": ["상대 결정권자에게 선물·접대로 빚 만들기", "검증 안 된 '대학병원 다 씀' 주장"],
}
NEG_RE = re.compile(r"[^.!?\n]{0,12}?(필요\s*(는\s*)?없|않으셔도|안\s*하셔도|하지\s*마|않습니다|않아도|아닙니다)")
NUM_RE = re.compile(r"(\d+(?:[.,]\d+)*)\s*(%|퍼센트|명|배|건|위|분이|분께서)")
ALT_RE = re.compile(r"대안|비수술|경과\s*관찰|보존적|다른\s*방법|안\s*하는\s*선택")
REASON_RE = re.compile(r"왜냐하면|이유|때문|근거")
TIME_RE = re.compile(r"생각해\s*보|가족과|상의|천천히|다음\s*진료|결정하셔도\s*됩니다|시간을\s*두")

def norm(s): return re.sub(r"\s+", " ", s or "").strip()

class KB:
    def __init__(self, kb):
        self.kb = kb
        self.alias = {}
        for pid, p in kb["principles"].items():
            short = pid.split("cialdini_")[-1]
            for a in (pid, short, p["name"]): self.alias[a.lower()] = pid
        for tid_, t in kb["tendencies"].items():
            n = t["number"]; slug = tid_.split("_", 2)[-1] if "_t" in tid_ else tid_
            for a in (tid_, f"#{n}", f"t{n:02d}", f"t{n}", str(n), slug, t["name"]): self.alias[a.lower()] = tid_
            self.alias[tid_.split(f"t{n:02d}_")[-1].lower()] = tid_
        for pid in list(kb["principles"]): self.alias[pid.split("cialdini_")[-1]] = pid  # 원칙 이름이 경향 slug보다 우선
    def resolve(self, name):
        return self.alias.get(str(name).strip().lower())
    def tnum(self, tid_): return self.kb["tendencies"][tid_]["number"]

def verified_facts(facts):
    ok, bad = [], []
    for f in facts or []:
        if f.get("verified") is True and norm(f.get("source")) and norm(f.get("claim")): ok.append(f)
        else: bad.append(f)
    return ok, bad

def find_cues(text, cues):
    hits = []
    for c in cues:
        if c and c in text:
            i = text.find(c); hits.append((c, norm(text[max(0, i - 15): i + len(c) + 15])))
    return hits

# ---------- 신호(윤리) ----------
def scan_signals(K, text, vfacts):
    kinds = {f.get("kind") for f in vfacts}
    out = []
    for s in K.kb["signals"]:
        m = None
        for mm in re.finditer(s["regex"], text):
            if NEG_RE.match(text[mm.end(): mm.end() + 20]): continue  # "지금 결정하실 필요 없습니다" 같은 부정문 제외
            m = mm; break
        if not m: continue
        level = s["level"]; note = ""
        if s["requires_fact"] and s["requires_fact"] in kinds:
            level = "ok"; note = f"검증 팩트({s['requires_fact']})가 있어 허용(사실대로만 표현)"
        out.append(dict(code=s["code"], name=s["name"], level=level, match=m.group(0), note=note))
    return out

def ungrounded_numbers(text, vfacts):
    blob = " ".join(norm(f.get("claim")) for f in vfacts)
    bad = []
    for m in NUM_RE.finditer(text):
        num = m.group(1)
        if num not in blob: bad.append(m.group(0))
    return bad

# ---------- analyze ----------
def validate_llm_cues(K, text, cues):
    acc, rej = [], []
    for c in cues or []:
        target = c.get("principle") or c.get("tendency") or c.get("id")
        rid = K.resolve(target) if target else None
        ev = norm(c.get("evidence"))
        if not rid: rej.append(dict(cue=c, reason="지식베이스에 없는 원칙·경향")); continue
        if not ev: rej.append(dict(cue=c, reason="근거 문장(evidence) 없음")); continue
        if text and ev not in norm(text): rej.append(dict(cue=c, reason="근거 문장이 원문에 없음(환각 의심)")); continue
        acc.append(dict(id=rid, evidence=ev, by="llm"))
    return acc, rej

def analyze(kb, inp):
    K = KB(kb); text = inp.get("text", ""); rules = []
    vfacts, _ = verified_facts(inp.get("facts"))
    p_hits, t_hits = {}, {}
    for pid, p in kb["principles"].items():
        for c, ev in find_cues(text, p["cues"]):
            p_hits.setdefault(pid, []).append(dict(cue=c, evidence=ev, by="rule")); rules.append(f"R1 단서 '{c}' → {pid}")
    for tid_, t in kb["tendencies"].items():
        for c, ev in find_cues(text, t["cues"]):
            t_hits.setdefault(tid_, []).append(dict(cue=c, evidence=ev, by="rule")); rules.append(f"R2 단서 '{c}' → {tid_}")
    acc, rej = validate_llm_cues(K, text, inp.get("cues"))
    for a in acc:
        tgt = p_hits if a["id"] in kb["principles"] else t_hits
        tgt.setdefault(a["id"], []).append(a); rules.append(f"R0 LLM 단서 승인 → {a['id']}")
    for r in rej: rules.append(f"R0 LLM 단서 거절: {r['reason']}")
    kinds = {f.get("kind") for f in vfacts}
    backed_p = {p for p in p_hits if any(r in kinds for r in kb["principles"][p]["requires"])}
    for p in backed_p: rules.append(f"R6 {p} 근거 팩트 확인 → 사실 기반 사용(위험 가중치 낮춤)")
    active_t = set(t_hits)
    backed_t = set()
    for pid in p_hits:
        for t in kb["principles"][pid]["triggers"]:
            if t not in active_t:
                rules.append(f"R3 {pid} -triggers-> {t}")
                if pid in backed_p: backed_t.add(t)
            active_t.add(t)
    rt = next((k for k, v in kb["tendencies"].items() if v["number"] == 24), None)
    if rt in active_t and "reason" in kinds: backed_t.add(rt)
    active_t.discard(next((k for k, v in kb["tendencies"].items() if v["number"] == 25), None))
    risky_t = active_t - backed_t
    # 대표님 대중 반응 갈고리
    hooks = {}
    for cid, c in kb["ceo_principles"].items():
        for name, cs in c["hooks"].items():
            h = find_cues(text, cs)
            if h: hooks[name if name != "_" else c["name"]] = [x[0] for x in h]
    # 결합(롤라팔루자)
    combos = []
    for cid, c in kb["combos"].items():
        m = [x for x in c["members"] if x in risky_t]
        need = len(c["members"]) if len(c["members"]) <= 3 else max(3, math.ceil(0.75 * len(c["members"])))
        if len(m) >= need:
            combos.append(dict(id=cid, name=c["name"], valence=c["valence"], matched=m, broken_by=c["broken_by"]))
            rules.append(f"R4 결합 {cid}: {len(m)}/{len(c['members'])} 경향 동시 작동")
    amp = [a for a in kb["amplifies"] if a[0] in active_t and a[1] in active_t]
    sig = scan_signals(K, text, vfacts)
    nb = sum(1 for s in sig if s["level"] == "block"); nw = sum(1 for s in sig if s["level"] == "warn")
    n = len(risky_t)
    keep = (0.88 ** n) * (0.97 ** len(backed_t)) * (0.75 ** nb) * (0.9 ** nw)
    risk = 1 - keep
    if n >= 3 or combos: risk = 1 - (1 - risk) ** 1.5; rules.append("R5 경향 3개 이상/결합 → 곱셈 증폭(지수 1.5)")
    score = round(100 * risk)
    level = "높음" if score >= 60 else "주의" if score >= 30 else "낮음"
    lolla = n >= 3 or bool(combos)
    # 방어 추천
    cov = {}
    for t in active_t:
        for d in kb["tendencies"][t]["countered_by"]: cov[d] = cov.get(d, 0) + 1
    for pid in p_hits:
        for d in kb["principles"][pid]["defenses"]: cov[d] = cov.get(d, 0) + 2
    for c in combos:
        for d in c["broken_by"]: cov[d] = cov.get(d, 0) + 2
    rf = X.scan_text(kb, text, inp, vfacts, inp.get("domain", "general")) + X.technique_flags(kb, inp.get("techniques"))
    if n >= 3: rf.append(dict(rule="man.lollapalooza_count", id=kb["research_rules"]["man.lollapalooza_count"]["id"], level="warn",
        grade=kb["research_rules"]["man.lollapalooza_count"]["grades"], label=kb["research_rules"]["man.lollapalooza_count"]["label"],
        match=f"경향 {n}개", note="정지·검토", sources=kb["research_rules"]["man.lollapalooza_count"]["sources"],
        fired=X.tag(kb, "man.lollapalooza_count", f"경향 {n}개")))
    rules = [f"{r} {X.PDF_TAG}" for r in rules] + [f["fired"] for f in rf]
    defs = [dict(id=d, name=kb["defenses"][d]["name"], how=kb["defenses"][d]["how"]) for d, _ in sorted(cov.items(), key=lambda x: -x[1])[:6] if d in kb["defenses"]]
    return dict(mode="analyze", engine_version=VERSION,
        principles=[dict(id=p, name=kb["principles"][p]["name"], fact_backed=p in backed_p, evidence=v) for p, v in p_hits.items()],
        tendencies=sorted([dict(id=t, number=kb["tendencies"][t]["number"], name=kb["tendencies"][t]["name"]) for t in active_t], key=lambda x: x["number"]),
        mass_hooks=hooks, combos=combos, amplifications=amp, signals=sig,
        lollapalooza=dict(score=score, level=level, suspected=lolla, tendency_count=n, fact_backed_tendencies=len(backed_t),
            advice="멈추고 방어 도구를 쓰세요 (경향 3개 이상 = 롤라팔루자 의심)" if lolla else "단일 경향 수준"),
        defenses=defs, llm_cues=dict(accepted=len(acc), rejected=rej),
        research_flags=[{k: v for k, v in f.items() if k != "fired"} for f in rf], rules_fired=rules)

# ---------- check ----------
def check(kb, inp):
    K = KB(kb); text = inp.get("text", ""); domain = inp.get("domain", "general")
    vfacts, ufacts = verified_facts(inp.get("facts"))
    issues = []
    for s in scan_signals(K, text, vfacts):
        if s["level"] != "ok": issues.append(dict(code=s["code"], level=s["level"], name=s["name"], match=s["match"]))
    a = analyze(kb, dict(text=text, facts=inp.get("facts"), cues=inp.get("cues"), domain=domain))
    fired = [r for r in a["rules_fired"] if r.endswith(X.PDF_TAG)]
    if (a["principles"] or a["tendencies"]) and not vfacts:
        issues.append(dict(code="F0", level="block", name="팩트 없는 설득(사기꾼 영역): 설득 단서가 있는데 검증된 팩트가 0개", match=""))
        fired.append(X.tag(kb, "fact.no_fact_no_persuade", "F0"))
    for x in ungrounded_numbers(text, vfacts):
        issues.append(dict(code="F1", level="warn", name="근거 없는 수치(검증 팩트에 없음)", match=x))
    if domain == "hospital_consult":
        if not ALT_RE.search(text): issues.append(dict(code="H1", level="warn", name="대안(비수술·경과 관찰) 언급 없음", match=""))
        if not REASON_RE.search(text): issues.append(dict(code="H2", level="warn", name="이유(왜) 제시 없음 (#24)", match=""))
        if not TIME_RE.search(text): issues.append(dict(code="H3", level="warn", name="결정할 시간 보장 문구 없음", match=""))
    rf = X.scan_text(kb, text, inp, vfacts, domain) + X.technique_flags(kb, inp.get("techniques"))
    if a["lollapalooza"]["tendency_count"] >= 3:
        rf += [f for f in a["research_flags"] if f["rule"] == "man.lollapalooza_count"]
        rf[-1]["fired"] = X.tag(kb, "man.lollapalooza_count", f"경향 {a['lollapalooza']['tendency_count']}개")
    info = []
    for f in rf:
        fired.append(f["fired"])
        if f["level"] in ("warn", "block"):
            issues.append(dict(code=f["rule"], level=f["level"], name=f["label"], match=f["match"], grade=f["grade"], rule_id=f["id"]))
        elif f["level"] == "info": info.append(dict(code=f["rule"], name=f["label"], match=f["match"], grade=f["grade"]))
    if ufacts:
        fired.append(X.tag(kb, "fact.claims_sourced", f"미검증 {len(ufacts)}개 → 의견"))
    tr = X.tares(text, [i["code"] for i in issues], vfacts)
    if not all(tr.values()):
        bad = [k for k, v in tr.items() if not v]
        issues.append(dict(code="man.tares_fail", level="warn", name=kb["research_rules"]["man.tares_fail"]["label"], match=", ".join(bad),
                           grade=kb["research_rules"]["man.tares_fail"]["grades"], rule_id="rule.pr_man_tares_fail"))
        fired.append(X.tag(kb, "man.tares_fail", ", ".join(bad)))
    sug = []
    s = X.request_suggestion(kb, text)
    if s: sug.append(s["suggestion"]); fired.append(s["fired"])
    verdict = "BLOCK" if any(i["level"] == "block" for i in issues) else "REVISE" if issues else "PASS"
    codes = {i["code"] for i in issues}
    if "F0" in codes: ms = X.mastery(kb, "하수", "검증 팩트 없이 설득 단서만 있음")
    elif verdict == "PASS": ms = X.mastery(kb, "고수", "팩트 위에서 설득, 조작·근거 없는 수치 없음" + ("" if not sug else " (BYAF 추가 시 행동 설계 완성)"))
    else: ms = X.mastery(kb, "중수", "팩트보다 설득 기술에 기댄 부분: " + ", ".join(sorted(codes))[:200])
    return dict(mode="check", engine_version=VERSION, verdict=verdict, issues=issues, info_flags=info, suggestions=sug, tares=tr, mastery=ms,
        rules_fired=fired,
        persuader_type="밀수꾼" if verdict == "BLOCK" else "탐정" if verdict == "PASS" else "수정 필요",
        facts=dict(verified=len(vfacts), unverified=len(ufacts)),
        lollapalooza=a["lollapalooza"], external_send="외부 발송·게시는 대표님 승인 후에만")

# ---------- plan ----------
def plan(kb, inp):
    K = KB(kb); goal = inp.get("goal", ""); domain = inp.get("domain", "general")
    aud = inp.get("audience", {}) or {}
    vfacts, ufacts = verified_facts(inp.get("facts"))
    kinds = {f.get("kind") for f in vfacts}
    prefs = [f"principle.cialdini_{p}" for p in DOMAIN_PRINCIPLES.get(domain, DOMAIN_PRINCIPLES["general"])]
    need_kinds = sorted({k for p in prefs for k in kb["principles"][p]["requires"]})
    out = dict(mode="plan", engine_version=VERSION, goal=goal, domain=domain)
    # 윤리 게이트(목표 자체)
    gs = [s for s in scan_signals(K, goal + " " + inp.get("draft", ""), []) if s["code"] in ("M4", "M5")]
    if domain == "investment" or gs:
        out.update(status="BLOCKED", gate="ethics", quadrant="해당 없음",
            reason="투자 권유·수익 보장은 윤리 게이트에서 어떤 경우에도 차단합니다." + (f" (탐지: {', '.join(s['match'] for s in gs)})" if gs else ""),
            next_step="정보 제공(사실·위험 고지)만 가능하며 권유 문구는 만들지 않습니다.")
        return out
    # 팩트 게이트
    if not vfacts:
        out.update(status="BLOCKED", gate="fact", quadrant="사기꾼", mastery=X.mastery(kb, "하수", "팩트 0개: 남는 것 없음"),
            rules_fired=[X.tag(kb, "fact.no_fact_no_persuade", "plan 차단")] + ([X.tag(kb, "fact.claims_sourced", f"미검증 {len(ufacts)}개 → 의견")] if ufacts else []),
            reason="검증된 팩트가 0개입니다. 팩트 없는 설득은 사기꾼 영역이라 계획을 만들지 않습니다.",
            unverified_facts=[f.get("claim", "") for f in ufacts],
            required_facts=[dict(kind="core", need="목표를 뒷받침하는 핵심 사실 1개 이상 (출처·확인 여부 포함)")] +
                [dict(kind=k, need=kb["fact_kinds"].get(k, k)) for k in need_kinds],
            next_step="필요한 팩트를 확인해 verified=true, source를 채운 뒤 다시 plan 하세요.")
        return out
    inv = aud.get("involvement") or DOMAIN_DEFAULT_INVOLVEMENT.get(domain, "unknown")
    if inv not in kb["elm"]: inv = "unknown"
    weights = {"high": (60, 25, 15), "low": (35, 35, 30), "unknown": (45, 30, 25)}[inv]
    forb_p = set(f"principle.cialdini_{p}" for p in DOMAIN_FORBIDDEN_PRINCIPLES.get(domain, []))
    usable, hold = [], []
    for p in prefs:
        req = kb["principles"][p]["requires"]
        if p in forb_p: continue
        if any(r in kinds for r in req):
            usable.append(dict(id=p, name=kb["principles"][p]["name"], how=kb["principles"][p]["ethical_use"],
                               fact=[f["claim"] for f in vfacts if f.get("kind") in req][:2]))
        else:
            hold.append(dict(id=p, name=kb["principles"][p]["name"], missing_fact=[dict(kind=r, need=kb["fact_kinds"].get(r, r)) for r in req]))
    combo = usable[:3]
    quadrant = "리더" if combo else "학자형"
    def pick(kind_set): return [f["claim"] for f in vfacts if f.get("kind") in kind_set]
    logos = [f["claim"] for f in vfacts if f.get("kind") not in ("credential", "shared_identity", "shared_trait", "commitment", "favor")] or [vfacts[0]["claim"]]
    order = [
     dict(step=1, part="logos", weight=weights[0], content=logos, rule="검증 팩트·이유·대안을 먼저 (이유 존중 #24)"),
     dict(step=2, part="ethos", weight=weights[1], content=pick({"credential", "shared_identity", "shared_trait", "favor"}) or ["(검증된 자격·관계 팩트 없음: 부풀리지 말고 생략)"],
          rule="실제 자격·관계만, 부풀림 금지"),
     dict(step=3, part="pathos", weight=weights[2], content=pick({"commitment"}) or ["상대의 목표·걱정을 상대 말로 확인 (압박 금지)"],
          rule="공감은 하되 불안을 키워 재촉하지 않기"),
    ]
    forb = BASE_FORBIDDEN + DOMAIN_FORBIDDEN.get(domain, []) + \
        [f"{kb['principles'][p]['name']} 원칙 사용 금지(이 도메인)" for p in forb_p] + \
        [f"{h['name']} 원칙: 근거 팩트({', '.join(m['kind'] for m in h['missing_fact'])}) 확인 전 사용 금지" for h in hold]
    warnings = []
    if quadrant == "학자형":
        warnings.append("팩트는 있지만 쓸 수 있는 설득 원칙이 없습니다(학자형 위험). 원칙별 근거 팩트를 보강하세요.")
    if ufacts: warnings.append(f"미검증 팩트 {len(ufacts)}개는 메시지에 쓰지 않았습니다.")
    if domain == "politics":
        warnings.append("대중 반응 갈고리(싸움 구경·남 안 되는 것·새로운 것·남 탓)는 사실일 때만. 근거 없는 남 탓·싸움 프레임은 M10.")
        warnings.append("밴드왜건은 실제 지지 데이터(statistic)가 있을 때만.")
    strat, sfired = X.strategy(kb, inp, domain, inv, vfacts, ufacts)
    for b in strat["blocked_techniques"]: warnings.append(f"{b['name']} 기법은 {b['reason']}이라 쓰지 않습니다 (ban.grade_D).")
    forb += [f"D등급(재현 실패) 기법: {b['name']}" for b in strat["blocked_techniques"]]
    ms = X.mastery(kb, "고수", "팩트 → 심리 전달 → 행동 설계(" + ("BYAF·" if strat.get("byaf") else "") + "구체 요청·실행 계획) → 결과로 증명") if quadrant == "리더" \
        else X.mastery(kb, "중수", "학자형: 팩트는 있으나 전달 설계 부족 — 고수 1단계만 완료")
    out.update(status="OK", gate="pass", quadrant=quadrant, strategy=strat, mastery=ms,
        rules_fired=[f"R7 팩트 게이트 통과·ELM {inv} {X.PDF_TAG}"] + sfired,
        elm=dict(involvement=inv, route=kb["elm"][inv]["route"], guidance=kb["elm"][inv]["guidance"]),
        principle_combo=combo, on_hold=hold, message_order=order, forbidden_tactics=forb, warnings=warnings,
        unverified_facts=[f.get("claim", "") for f in ufacts], external_send="외부 발송·게시는 대표님 승인 후에만")
    if inp.get("draft"):
        out["draft_check"] = check(kb, dict(text=inp["draft"], facts=inp.get("facts"), domain=domain))
    return out

MODES = {"analyze": analyze, "plan": plan, "check": check}

def main(argv=None):
    ap = argparse.ArgumentParser(description="설득 뉴로심볼릭 엔진")
    ap.add_argument("mode", choices=MODES)
    ap.add_argument("--input", required=True, help="입력 JSON 파일 (- 이면 표준입력)")
    ap.add_argument("--kb", default=None)
    a = ap.parse_args(argv)
    inp = json.load(sys.stdin if a.input == "-" else open(a.input, encoding="utf-8"))
    need = "goal" if a.mode == "plan" else "text"
    if not isinstance(inp, dict) or not str(inp.get(need, "")).strip():
        print(json.dumps({"mode": a.mode, "error": f"입력 오류: '{need}' 필드가 필요합니다 (SCHEMA.md 참고)"}, ensure_ascii=False))
        return 1
    res = MODES[a.mode](load_kb(a.kb), inp)
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 2 if res.get("status") == "BLOCKED" or res.get("verdict") == "BLOCK" else 0

if __name__ == "__main__":
    sys.exit(main())
