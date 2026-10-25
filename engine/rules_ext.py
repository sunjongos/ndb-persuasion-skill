# -*- coding: utf-8 -*-
"""심층연구 규칙 50 (WIKI-CODE-022) 실행 계층. engine.py가 불러 쓴다. 규칙 정의는 knowledge.json의 research_rules(위키 rule.pr_*)."""
import re

NEG = re.compile(r"[^.!?\n]{0,12}?(필요\s*(는\s*)?없|않으셔도|안\s*하셔도|하지\s*마|않습니다|않아도|아닙니다)")
DIGIT_RE = re.compile(r"\d+(?:[.,]\d+)*")
BEHAVIOR_GOAL_RE = re.compile(r"예약|서명|신청|참여|투표|구매|도입|실천|복용|검진|등록|가입|방문|시술|수술|교체|사용|지키|바꾸")
PDF_TAG = "[근거: PDF 「설득과 오판」]"

def tag(kb, orig, note=""):
    r = kb["research_rules"][orig]
    src = ", ".join(r["sources"][:3]) + (" 외" if len(r["sources"]) > 3 else "")
    return f"{r['id']} [근거 {r['grades']}] {r['label']}" + (f" — {note}" if note else "") + f" (출처: {src})"

def _first(rx, text, neg=True):
    for m in re.finditer(rx, text):
        if neg and NEG.match(text[m.end(): m.end() + 20]): continue
        return m
    return None

def item_by_ref(kb, ref):
    """기법 이름·원본 id·위키 id로 연구 개체 찾기"""
    s = str(ref).strip().lower()
    for wid, it in kb["research_items"].items():
        if s in (wid.lower(), it["orig"].lower(), it["name"].lower()) or s == it["orig"].split(".")[-1]: return wid, it
    return None, None

def repeated_claims(text, n=3):
    sents = [re.sub(r"\s+", " ", x).strip() for x in re.split(r"[.!?\n]+", text) if len(x.strip()) >= 6]
    cnt = {}
    for s in sents: cnt[s] = cnt.get(s, 0) + 1
    return [s for s, c in cnt.items() if c >= n]

def scan_text(kb, text, inp, vfacts, domain):
    """텍스트·입력 플래그로 판정 가능한 규칙(info·warn·block, 탐지식 있는 strategy) 실행 → flags"""
    kinds = {f.get("kind") for f in vfacts}
    R = kb["research_rules"]; out = []
    def add(orig, match="", note="", level=None):
        r = R[orig]; out.append(dict(rule=orig, id=r["id"], level=level or r["level"], grade=r["grades"], label=r["label"],
                                     match=match, note=note, sources=r["sources"], fired=tag(kb, orig, note)))
    for orig, r in R.items():
        d = r["detector"]; lv = r["level"]
        if orig == "cue.repetition":
            rep = repeated_claims(text, d.get("same_claim_min", 3)); m = _first(d["any"], text)
            if rep or m: add(orig, (rep[0] if rep else m.group(0)), "같은 주장 3회 이상 반복" if rep else "")
        elif orig == "cue.fear_without_efficacy":
            m = _first(d["threat"], text, neg=False)
            if m and not re.search(d["efficacy"], text): add(orig, m.group(0), "위협 + 실행 방법(효능감)을 함께 제시")
        elif orig == "cue.narrative":
            m = re.search(d["story"], text)
            if m and not re.search(d["number"], text): add(orig, m.group(0), "대표성·통계를 함께")
        elif orig == "cue.ai_generated_mass":
            n = len(DIGIT_RE.findall(text))
            if inp.get("ai_generated") and n >= d["numbers_min"]: add(orig, f"수치 {n}개", "무작위 3개 표본 사실검증")
        elif orig == "man.impersonation":
            m = _first(d["any"], text)
            if m or inp.get("persona_verified") is False: add(orig, m.group(0) if m else "persona_verified=false")
        elif orig == "man.hidden_influence":
            if inp.get("conflict_of_interest") and not re.search(d["disclosure"], text): add(orig, "이해관계 있음·공개 문구 없음", "이해관계·광고 여부를 밝히세요")
        elif orig == "man.consent_bypass":
            m = _first(d["any"], text)
            if m: add(orig, m.group(0), "" if domain == "hospital_consult" else "의료 외 맥락: 경고", level="block" if domain == "hospital_consult" else "warn")
        elif orig == "ban.backfire_excuse":
            m = _first(d["any"], text, neg=False)
            if m and not re.search(d["except"], text[m.start(): m.end() + 15]): add(orig, m.group(0), "정정 역효과는 대규모 재현에서 거의 없음 → 정정하세요")
        elif orig == "fact.accuracy_after_optimization":
            if (inp.get("ai_generated") or inp.get("optimized")) and not inp.get("accuracy_rechecked"): add(orig, "accuracy_rechecked 없음", "최적화 후 사실 정확도 재검사")
        elif orig == "fact.disclose_ai":
            if inp.get("ai_generated") and not re.search(d["disclosure"], text): add(orig, "AI 공개 문구 없음")
        elif "any" in d and lv in ("info", "warn", "block", "strategy"):
            m = _first(d["any"], text)
            if not m: continue
            uf = d.get("unless_fact")
            if uf and uf in kinds: add(orig, m.group(0), f"검증 팩트({uf}) 있음: 사실대로만", level="ok"); continue
            add(orig, m.group(0), level="warn" if lv == "strategy" else None)
    fired = {f["rule"] for f in out}
    if "cue.repetition" in fired and not vfacts:
        add("man.repetition_without_evidence", next(f["match"] for f in out if f["rule"] == "cue.repetition"), "반복 대신 검증 팩트를 추가")
    if "cue.narrative" in fired:
        add("fact.base_rate_for_story", next(f["match"] for f in out if f["rule"] == "cue.narrative"), "사례 + 기저율")
    return out

def technique_flags(kb, techniques):
    out = []
    for t in techniques or []:
        wid, it = item_by_ref(kb, t)
        if it and it["grade"] == "D":
            out.append(dict(rule="ban.grade_D", id=kb["research_rules"]["ban.grade_D"]["id"], level="block", grade="D", label=kb["research_rules"]["ban.grade_D"]["label"],
                            match=f"{it['name']} ({wid})", note="재현 실패 → 추천 금지", sources=it["sources"],
                            fired=tag(kb, "ban.grade_D", f"{it['name']} ({wid}) 재현 실패")))
    return out

def tares(text, issues_codes, vfacts):
    """TARES 5항목 (진실성·진정성·존중·공정·사회적 책임)"""
    c = set(issues_codes)
    has = lambda *xs: any(x in c for x in xs)
    return {
        "truthfulness": not has("F0", "F1", "M2", "M6", "fact.no_fact_no_persuade", "dp.fake_social_proof"),
        "authenticity": not has("man.impersonation", "man.hidden_influence", "fact.disclose_ai"),
        "respect": not has("M3", "M8", "dp.false_scarcity", "dp.confirmshaming", "dp.nagging", "dp.roach_motel", "M1"),
        "equity": not has("man.consent_bypass", "dp.sneak_into_basket", "dp.preselected_default", "ban.ego_depletion", "M7"),
        "social_responsibility": not has("M4", "M5", "M10", "cue.outgroup_hostility", "ban.backfire_excuse"),
    }

def request_suggestion(kb, text):
    d = kb["research_rules"]["fact.behavior_ask_after_facts"]["detector"]
    if re.search(d["request"], text) and not re.search(d["byaf"], text):
        return dict(rule="fact.behavior_ask_after_facts", fired=tag(kb, "fact.behavior_ask_after_facts", "BYAF 문장 추가 권장"),
                    suggestion="요청 뒤에 '결정은 ○○님 몫입니다(안 하셔도 괜찮습니다)'를 붙이세요 (BYAF, 승낙 확률 약 2배)")
    return None

def mastery(kb, level, why):
    m = kb.get("mastery") or {}
    lv = next((x for x in m.get("levels", []) if x["name"] == level), {"name": level, "how": "", "result": ""})
    return dict(level=level, how=lv.get("how", ""), result=lv.get("result", ""), why=why, maxim=m.get("maxim", ""), principle=m.get("id", ""))

def infer_goal_type(goal):
    return "behavior" if BEHAVIOR_GOAL_RE.search(goal or "") else "attitude"

def strategy(kb, inp, domain, inv, vfacts, ufacts):
    """청중 상태 → 전략 규칙 선택 (aud.*·fact.*). D등급 기법은 차단 목록으로."""
    R = kb["research_rules"]; aud = inp.get("audience", {}) or {}; fired = []
    goal_type = aud.get("goal_type") or infer_goal_type(inp.get("goal", ""))
    prior = aud.get("prior_attitude", "unknown"); ident = aud.get("identity_threat", "low")
    culture = aud.get("culture", "collectivist"); timing = aud.get("timing", inp.get("timing", ""))
    state = aud.get("state", ""); proposal = " ".join([inp.get("goal", ""), inp.get("draft", ""), aud.get("proposal", "")])
    sel = []
    if inv == "high": sel.append("aud.high_involvement")
    if inv == "low": sel.append("aud.low_involvement")
    if prior == "opposed": sel.append("aud.opposed_identity" if ident == "high" else "aud.opposed_low_identity")
    if prior == "undecided": sel.append("aud.undecided")
    sel.append("aud.goal_behavior" if goal_type == "behavior" else "aud.goal_attitude")
    if state == "ambivalent" or (domain == "hospital_consult" and state in ("ambivalent", "hesitant")): sel.append("aud.patient_ambivalent")
    if domain == "staff" and goal_type == "behavior": sel.append("aud.staff_change")
    if culture == "collectivist": sel.append("aud.collectivist")
    if domain == "politics" and timing in ("late", "election_late", "막판"): sel.append("aud.campaign_late")
    if re.search(R["aud.no_microtarget_overclaim"]["detector"]["any"], proposal): sel.append("aud.no_microtarget_overclaim")
    prefer, avoid, blocked = [], [], []
    for s in sel:
        r = R[s]; fired.append(tag(kb, s))
        for p in r["prefer"]:
            tok = p.split()[0]; wid, it = item_by_ref(kb, tok)
            if it and it["grade"] == "D": blocked.append(dict(technique=wid, name=it["name"], reason="D등급 재현 실패")); continue
            row = dict(technique=wid or tok, name=it["name"] if it else p, grade=it["grade"] if it else "-", by=s, note=p[len(tok):].strip())
            if not any(x["technique"] == row["technique"] for x in prefer): prefer.append(row)
        for a in r["avoid"]:
            if a not in avoid: avoid.append(a)
    for t in inp.get("techniques") or []:
        wid, it = item_by_ref(kb, t)
        if it and it["grade"] == "D":
            blocked.append(dict(technique=wid, name=it["name"], reason="D등급 재현 실패 (ban.grade_D)")); fired.append(tag(kb, "ban.grade_D", it["name"]))
    prefer = [p for p in prefer if p["technique"] not in {b["technique"] for b in blocked}]
    out = dict(goal_type=goal_type, audience=dict(prior_attitude=prior, identity_threat=ident, state=state or "unknown", culture=culture, timing=timing or "-"),
               selected_rules=[R[s]["id"] for s in sel], prefer=prefer, avoid=avoid, blocked_techniques=blocked, notes=[])
    byaf_need = domain == "hospital_consult" or goal_type == "behavior" or prior == "opposed"
    if goal_type == "behavior":
        out["behavior_sequence"] = R["fact.behavior_ask_after_facts"]["then"].get("order", [])
        fired.append(tag(kb, "fact.behavior_ask_after_facts"))
    if byaf_need:
        out["byaf"] = dict(recommended=True, phrase="결정은 ○○님 몫입니다. 안 하셔도 괜찮습니다.", why="자율성 강조 → 승낙 확률 약 2배 (메타분석, 등급 A)")
    if ufacts:
        out["opinion_only"] = [f.get("claim", "") for f in ufacts]; fired.append(tag(kb, "fact.claims_sourced", f"{len(ufacts)}개는 '의견'으로 표시"))
    if inv == "high":
        kinds = {f.get("kind") for f in vfacts}
        if not kinds & {"alternative", "comparison", "counterargument"}:
            out["notes"].append("고관여: 주요 반대 근거 1개와 그 반박을 넣으세요 (fact.two_sided)"); fired.append(tag(kb, "fact.two_sided", "반대 근거 팩트 없음"))
    if inp.get("ai_generated") or inp.get("optimized"):
        out["notes"].append("AI 생성·최적화 메시지: AI 사용 공개 + 최적화 후 사실 정확도 재검사")
        fired += [tag(kb, "fact.disclose_ai"), tag(kb, "fact.accuracy_after_optimization")]
    if domain == "politics" and "aud.campaign_late" in sel:
        out["notes"].append("막판 설득 효과≈0: 지지층 동원(투표 계획·알림)에 집중")
    return out, fired
