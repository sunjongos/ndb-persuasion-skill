# -*- coding: utf-8 -*-
"""ontology_src 데이터로 위키 개체·노트를 쓴다. 사용: python3 build_wiki.py ontology"""
import os, sys
import tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ontology_src import *

W = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ontology")
E = os.path.join(W, "entities")
D = "2026-10-25"
HUB = "concept.persuasion_misjudgment"; CHUB = "concept.ceo_persuasion_philosophy"
written = []; triples = []

def ent(fname, eid, typ, conf, src, lines, kw=None):
    body = [f"---\nid: {eid}\ntype: {typ}\nupdated: {D}\nconfidence: {conf}\nsource: {src}\n---"]
    for l in lines:
        s, r, o = l
        body.append(f"- {s} - {r} - {o}")
        triples.append((s, r, o))
    if kw: body.append(f"> 검색어: {kw}")
    open(os.path.join(E, fname + ".md"), "w", encoding="utf-8").write("\n".join(body) + "\n")
    written.append(eid)

tmap = {n: tid(n, s) for n, s, *_ in TEND}
tname = {n: nm for n, s, nm, *_ in TEND}
# 역방향: 경향 <- 원칙, 경향 <- 방어, 경향 <- 결합
trig_by = {}; ctr_by = {}; mem_of = {}
for p in PRINCIPLES:
    for t, _ in p["triggers"]: trig_by.setdefault(t, []).append(p["id"])
for did, f, ko, layer, how, cs in DEFENSES:
    for n in cs: ctr_by.setdefault(tmap[n], []).append(did)
for c in COMBOS:
    for n in c["members"]: mem_of.setdefault(tmap[n], []).append(c["id"])

# ---- Cialdini 원칙
for p in PRINCIPLES:
    i = p["id"]; L = [
     (i, "kb_kind", "principle"), (i, "name_ko", p["ko"]), (i, "pillar", p["pillar"]), (i, "part_of", HUB),
     (i, "mechanism", "[자료 내용] " + p["mech"]), (i, "evidence_study", "[자료 내용] " + p["study"] + " (원 연구 수치, 재현성 주의)"),
     (i, "misuse", "[자료 내용] 밀수꾼: " + p["misuse"]), (i, "ethical_use", "[자료 내용] 탐정: " + p["ethical"]),
     (i, "hospital_use", "[자료 내용] " + p["hospital"])]
    L += [(i, "triggers", f"{t} ({nm}, 자료 8쪽 연결선)") for t, nm in p["triggers"]]
    L += [(i, "defended_by", f"{d} ({why})") for d, why in p["defense"]]
    L += [(i, "requires", f"fact:{k} ({FACT_KINDS[k]})") for k in p["requires"]]
    L += [(i, "cue", p["cues"])]
    if i == "principle.cialdini_presuasion": L.append((i, "note", "[자료 내용] 7원칙 이후 확장 개념(점선 상자)"))
    ent(p["file"], i, "Topic", 0.85, SRC_PDF, L, f"치알디니 {p['ko']}, 설득 원칙, {p['pillar']}")

# ---- Munger 25
for n, slug, nm, grp, mech, hosp, cues in TEND:
    i = tmap[n]; L = [(i, "kb_kind", "tendency"), (i, "number", str(n)), (i, "name_ko", nm), (i, "group", grp),
        (i, "part_of", HUB), (i, "part_of", "model.munger"), (i, "mechanism", "[자료 내용] " + mech), (i, "hospital_example", "[자료 내용] " + hosp)]
    L += [(i, "triggered_by", p) for p in trig_by.get(i, [])]
    L += [(i, "countered_by", d) for d in ctr_by.get(i, [])]
    L += [(i, "member_of", c) for c in mem_of.get(i, [])]
    if cues: L.append((i, "cue", cues))
    if n == 25:
        L += [(i, "emerges_from", c["id"]) for c in COMBOS]
        L.append((i, "rule", "[자료 내용] 결합은 곱셈(A×B×C×D)이라 고리 하나만 끊어도 멈춘다"))
    if n in (19, 20, 21, 1, 11, 13, 17, 23):
        L.append((i, "note", "[자료 내용] 멍거에게만 있는 영역(치알디니 대응 원칙 없음)"))
    ent(TFILE(n, slug), i, "Topic", 0.85, SRC_PDF, L, f"멍거 {n}번 {nm}, 오판 경향, {grp}")

# ---- 롤라팔루자 결합
for c in COMBOS:
    i = c["id"]; L = [(i, "kb_kind", "combo"), (i, "name_ko", c["ko"]), (i, "valence", c["val"]), (i, "part_of", HUB),
        (i, "instance_of", tmap[25]), (i, "description", "[자료 내용] " + c["note"])]
    L += [(i, "member", tmap[n]) for n in c["members"]]
    ms = c["members"]
    L += [(tmap[a], "amplifies", f"{tmap[b]} ({c['ko']} 결합 안에서)") for a, b in zip(ms, ms[1:])]
    L += [(i, "broken_by", d) for d in c["defense"]]
    ent(f"{c['file']}", i, "Topic", 0.8, SRC_PDF, L, f"롤라팔루자, {c['ko']}")

# ---- 방어 도구
for did, f, ko, layer, how, cs in DEFENSES:
    L = [(did, "kb_kind", "defense"), (did, "name_ko", ko), (did, "layer", layer), (did, "part_of", HUB), (did, "how", "[자료 내용] " + how)]
    L += [(did, "counters", tmap[n]) for n in cs]
    ent(f, did, "Topic", 0.85, SRC_PDF, L, f"방어 도구, {ko}, {layer}")

# ---- 병원 사례
for cid, f, ko, desc, ill, dfs in CASES:
    L = [(cid, "kb_kind", "case"), (cid, "name_ko", ko), (cid, "part_of", HUB), (cid, "applies_at", "org.namyangju_baek_hospital"),
         (cid, "description", "[자료 내용] " + desc)]
    L += [(cid, "illustrates", x) for x in ill]
    L += [(cid, "uses_defense", d) for d in dfs]
    ent(f, cid, "Topic", 0.8, SRC_PDF, L, f"병원 적용 사례, {ko}")

# ---- 설득자 유형
i = "concept.persuader_types"
ent("Concept-PersuaderTypes", i, "Topic", 0.85, SRC_PDF, [
 (i, "kb_kind", "persuader_types"), (i, "part_of", HUB),
 (i, "type", "서투른 자: 진짜 강점도 못 살린다"),
 (i, "type", "밀수꾼: 가짜 희귀성·권위를 들여온다 → 결국 평판 붕괴"),
 (i, "type", "탐정: 상황에 이미 있는 진짜 요소만 찾아 정직하게 드러낸다"),
 (i, "hospital_model", "[자료 내용] 병원의 모델은 탐정"),
 (i, "institutional_design", "[자료 내용] 멍거식 제도 설계: 금전등록기, 원가 가산 계약 금지처럼 구조로 부패 차단"),
 (i, "illustrated_by", "concept.case_consult_detective"),
 (i, "enforced_by", "rule.persuasion_ethics_gate")], "밀수꾼, 탐정, 서투른 자, 설득 윤리")

# ---- 규칙(게이트)
i = "rule.persuasion_fact_gate"
ent("Rule-PersuasionFactGate", i, "Decision", 0.9, SRC_CEO + " + " + SRC_PDF, [
 (i, "kb_kind", "gate"), (i, "part_of", CHUB),
 (i, "rule", "설득 계획 전에 검증된 팩트(출처·확인 여부)를 먼저 확인한다. 검증 팩트가 0개면 '사기꾼 영역'으로 차단하고 필요한 팩트를 요구한다"),
 (i, "rule", "각 설득 원칙은 자기 근거 팩트 종류가 확인될 때만 쓸 수 있다 (Tactic -requires- Fact)"),
 (i, "rule", "초안에 나온 수치는 검증 팩트 안에 있어야 한다. 없으면 '근거 없는 수치'로 수정 요구"),
 (i, "derived_from", "principle.fact_before_persuasion"), (i, "derived_from", "principle.fact_persuasion_matrix"),
 (i, "implemented_by", "model.persuasion_engine")] +
 [(i, "fact_kind", f"fact:{k} ({v})") for k, v in FACT_KINDS.items()], "팩트 게이트, 사기꾼 차단, 근거 확인")
i = "rule.persuasion_ethics_gate"
ent("Rule-PersuasionEthicsGate", i, "Decision", 0.9, SRC_CEO + " + " + SRC_PDF, [
 (i, "kb_kind", "gate"), (i, "part_of", CHUB), (i, "part_of", HUB),
 (i, "rule", "탐정만 허용, 밀수꾼 금지: 가짜 희귀성·조작된 사회적 증거·약점 압박·결정 시간 박탈 금지"),
 (i, "rule", "투자 권유·수익 보장 문구는 어떤 경우에도 차단"),
 (i, "rule", "외부 발송(메일·메시지·게시)은 대표님 승인 후에만"),
 (i, "derived_from", "concept.persuader_types"), (i, "derived_from", "principle.fact_before_persuasion"),
 (i, "implemented_by", "model.persuasion_engine")] +
 [(i, "signal", f"{c} :: {nm} :: {lv} :: {rx} :: {fk}") for c, nm, lv, rx, fk in SIGNALS], "윤리 게이트, 조작 탐지, 다크 패턴, 투자 권유 차단")

# ---- 근거 출처·개념
ent("Ref-PersuasionMisjudgmentPDF", "ref.persuasion_misjudgment_pdf", "Source", 0.9, SRC_PDF, [
 ("ref.persuasion_misjudgment_pdf", "title", "설득과 오판: 영향력의 과학 × 오판의 심리학 (NDB 직원 교육자료, Spine Center 직원 역량 강화 강의 노트, 2026-10, 16쪽)"),
 ("ref.persuasion_misjudgment_pdf", "describes", HUB),
 ("ref.persuasion_misjudgment_pdf", "cites", "ref.cialdini_influence"), ("ref.persuasion_misjudgment_pdf", "cites", "ref.munger_misjudgment"),
 ("ref.persuasion_misjudgment_pdf", "cites_studies", "Regan 1971; Cialdini 1975; Freedman & Fraser 1966; Goldstein·Cialdini·Griskevicius 2008; Martin·Bassi·Dunbar-Rees 2012; Mandel & Johnson 2002; Milgram 1963"),
 ("ref.persuasion_misjudgment_pdf", "caveat", "[자료 내용] 재현성 위기(수치는 원 연구 값), WEIRD 표본(한국은 집단주의), 멍거 목록은 실무자의 관찰 체크리스트, 편향을 안다고 사라지지 않음")], "설득과 오판 PDF, 직원 교육자료")
ent("Ref-CialdiniInfluence", "ref.cialdini_influence", "Source", 0.85, SRC_PDF, [
 ("ref.cialdini_influence", "title", "Robert Cialdini, Influence: The Psychology of Persuasion (2021 확장판); Pre-Suasion (2016)"),
 ("ref.cialdini_influence", "basis_of", "principle.cialdini_reciprocity"), ("ref.cialdini_influence", "basis_of", "principle.cialdini_presuasion"),
 ("ref.cialdini_influence", "method", "[자료 내용] 3년간 영업·방문판매·모금 조직에 잠입 관찰; 칠면조 '칩칩' 소리 = 클릭-윙(자동 반응)")], "치알디니 설득의 심리학, 초전 설득")
ent("Ref-MungerMisjudgment", "ref.munger_misjudgment", "Source", 0.85, SRC_PDF, [
 ("ref.munger_misjudgment", "title", "Charlie Munger, The Psychology of Human Misjudgment (1995 하버드 강연, 2005 개정); Practical Thought About Practical Thought? (1996)"),
 ("ref.munger_misjudgment", "basis_of", "concept.munger_t25_lollapalooza"), ("ref.munger_misjudgment", "related", "model.munger"),
 ("ref.munger_misjudgment", "frame", "[자료 내용] 표준적 오작동: 평소엔 잘 맞는 어림법이 특정 조건에서 오판을 낳는다")], "멍거 인간 오판의 심리학")
ent("Ref-AristotleRhetoric", "ref.aristotle_rhetoric", "Source", 0.9, "웹 확인 2026-10-25: https://plato.stanford.edu/entries/aristotle-rhetoric/", [
 ("ref.aristotle_rhetoric", "title", "Stanford Encyclopedia of Philosophy, 'Aristotle's Rhetoric' (Rhet. I.2, 1356a)"),
 ("ref.aristotle_rhetoric", "fact", "기술적 설득 수단(pisteis)은 셋: 말하는 사람의 성품(ethos), 듣는 사람의 감정(pathos), 논증 자체(logos)"),
 ("ref.aristotle_rhetoric", "fact", "ethos 신뢰의 근거 = 실천적 지혜(phronesis)·덕·선의"),
 ("ref.aristotle_rhetoric", "fact", "수사학은 오용될 수 있다는 문제를 아리스토텔레스도 다뤘다 (SEP 4.3절)"),
 ("ref.aristotle_rhetoric", "url", "https://plato.stanford.edu/entries/aristotle-rhetoric/"),
 ("ref.aristotle_rhetoric", "describes", "concept.logos_ethos_pathos")], "아리스토텔레스 수사학, 로고스 에토스 파토스")
ent("Ref-ELMPettyCacioppo", "ref.elm_petty_cacioppo", "Source", 0.9, "웹 확인 2026-10-25: doi 10.1016/S0065-2601(08)60214-2, 저자 PDF richardepetty.com", [
 ("ref.elm_petty_cacioppo", "title", "Petty & Cacioppo (1986) The Elaboration Likelihood Model of Persuasion, Advances in Experimental Social Psychology 19권 123~205쪽"),
 ("ref.elm_petty_cacioppo", "fact", "중심 경로 = 주장의 장점을 꼼꼼히 따짐; 주변 경로 = 단순 단서(출처의 매력·전문성 등)로 판단"),
 ("ref.elm_petty_cacioppo", "fact", "중심 경로로 바뀐 태도가 더 오래가고 행동을 더 잘 예측한다"),
 ("ref.elm_petty_cacioppo", "url", "https://doi.org/10.1016/S0065-2601(08)60214-2"),
 ("ref.elm_petty_cacioppo", "url", "https://richardepetty.com/wp-content/uploads/2019/01/1986-advances-pettycacioppo.pdf"),
 ("ref.elm_petty_cacioppo", "describes", "concept.elm_routes")], "ELM 정교화 가능성 모델, 중심 경로, 주변 경로")
i = "concept.logos_ethos_pathos"
ent("Concept-LogosEthosPathos", i, "Topic", 0.85, SRC_CEO, [
 (i, "kb_kind", "message_order"), (i, "part_of", CHUB), (i, "source", "ref.aristotle_rhetoric"),
 (i, "order", "logos → ethos → pathos (팩트 먼저, 그다음 신뢰, 마지막에 감정)"),
 (i, "logos", "검증된 팩트·이유·대안 (원칙: 이유 존중 #24, 팩트 게이트)"),
 (i, "ethos", "실제 자격·경력·선의 (원칙: 권위·호감·연대감, 부풀림 금지)"),
 (i, "pathos", "상대의 목표·두려움에 공감하되 압박 금지 (원칙: 일관성—본인 목표 말로 쓰기)"),
 (i, "note", "[해석] 순서는 대표님 원칙(팩트 먼저)을 메시지 구성에 옮긴 것; 아리스토텔레스 원문이 순서를 정한 것은 아니다")], "로고스 에토스 파토스, 메시지 순서")
i = "concept.elm_routes"
ent("Concept-ELMRoutes", i, "Topic", 0.85, SRC_CEO, [
 (i, "kb_kind", "elm"), (i, "part_of", CHUB), (i, "source", "ref.elm_petty_cacioppo"),
 (i, "route", "high :: 중심 경로 :: 관여도 높음(내 몸·돈·생명과 직결, 시간·능력 있음) → 논증의 질, 양면 메시지, 데이터·대안"),
 (i, "route", "low :: 주변 경로 :: 관여도 낮음(관심 적음, 바쁨) → 짧고 쉬운 단서(진짜 자격, 실제 사회적 증거, 이야기); 팩트 한 줄은 반드시"),
 (i, "route", "unknown :: 혼합 :: 관여도 모름 → 첫 문장 핵심 팩트 + 짧은 신뢰 단서, 관심 보이면 상세 근거"),
 (i, "note", "[해석] 치알디니 원칙들은 대개 주변 경로 단서로 작동한다; 환자 수술 상담은 중심 경로가 기본"),
 (i, "maps_to", "principle.politics_psychology_first")], "ELM, 관여도, 중심 경로, 주변 경로")

# ---- 대표님 원칙
for c in CEO:
    i = c["id"]; L = [(i, "kb_kind", "ceo_principle"), (i, "name_ko", c["ko"]), (i, "part_of", CHUB), (i, "said_by", "person.choi_sunjong (2026-10-25 대화)")]
    L += [(i, "fact", x) for x in c["facts"]]
    L += [(i, "note", x) for x in c["interp"]]
    L += [(i, r, o) for r, o in c["rel"]]
    if c["cues"]:
        for part in c["cues"].split(" || "): L.append((i, "cue", part))
    ent(c["file"], i, "Topic", 0.9, SRC_CEO, L, f"대표님 설득 철학, {c['ko']}")

# ---- 최상위 허브(021)
i = CHUB
L = [(i, "wiki_code", "WIKI-CODE-021"), (i, "kb_kind", "hub"), (i, "owner", "person.choi_sunjong"),
     (i, "summary", "팩트 위에 설득을 세운다: 팩트 없는 설득은 사기꾼, 팩트만 있고 설득이 없으면 학자형, 둘 다 있어야 리더"),
     (i, "rank", "최상위 원칙: 치알디니·멍거 도구(WIKI-CODE-020)는 이 원칙 아래에서만 쓴다"),
     (i, "governs", HUB)]
L += [(i, "has_principle", c["id"]) for c in CEO]
L += [(i, "has_gate", "rule.persuasion_fact_gate"), (i, "has_gate", "rule.persuasion_ethics_gate"),
      (i, "uses", "concept.logos_ethos_pathos"), (i, "uses", "concept.elm_routes"),
      (i, "supported_by", "ref.aristotle_rhetoric"), (i, "supported_by", "ref.elm_petty_cacioppo"),
      (i, "related", "principle.political_judgment"), (i, "related", "principle.catalyst_triad"),
      (i, "implemented_by", "model.persuasion_engine")]
ent("Concept-CEOPersuasionPhilosophy", i, "Topic", 0.9, SRC_CEO, L, "대표님 설득 철학, 팩트와 설득, 리더 사기꾼 학자형, 정치는 심리")

# ---- PDF 허브(020)
i = HUB
L = [(i, "wiki_code", "WIKI-CODE-020"), (i, "kb_kind", "hub"), (i, "source", "ref.persuasion_misjudgment_pdf"),
     (i, "summary", "[자료 내용] 치알디니 7원칙(남이 나를 움직이는 방식)과 멍거 25경향(내가 나를 속이는 방식)은 같은 뿌리(자동 반응)를 가리킨다"),
     (i, "governed_by", CHUB), (i, "lecture", "project.ndb_lecture_persuasion_202610"),
     (i, "three_pillars", "[자료 내용] 관계(상호성·호감·연대감) / 불확실성 해소(사회적 증거·권위) / 즉각 행동(일관성·희귀성)"),
     (i, "autopilot_conditions", "[자료 내용] 병원은 시간 압박·피로·위계·불확실성·감정이 겹쳐 자동 반응이 잘 켜진다"),
     (i, "defense_layers", "[자료 내용] 감지(치알디니) → 분리(멍거) → 구조(체크리스트·제도)"),
     (i, "cialdini_only", "[자료 내용] 초전 설득, 연대감, 설득자 윤리, 신체 경보, 다크 패턴"),
     (i, "related", "model.munger"), (i, "related", "model.ndb"), (i, "related", "concept.rise_fall_3layers"),
     (i, "related", "principle.political_judgment"), (i, "has", "concept.persuader_types"), (i, "has", "rule.persuasion_ethics_gate"),
     (i, "implemented_by", "model.persuasion_engine")]
L += [(i, "has_principle", p["id"]) for p in PRINCIPLES]
L += [(i, "has_tendency", tmap[n]) for n in sorted(tmap)]
L += [(i, "has_combo", c["id"]) for c in COMBOS]
L += [(i, "has_defense", d[0]) for d in DEFENSES]
L += [(i, "has_case", c[0]) for c in CASES]
ent("Concept-PersuasionMisjudgment", i, "Topic", 0.85, SRC_PDF, L, "설득과 오판, 치알디니, 멍거, 롤라팔루자, 병원 설득 윤리")

# ---- 엔진·강의
i = "model.persuasion_engine"
ent("Model-PersuasionEngine", i, "Decision", 0.8, "어시스턴트 구현 2026-10-25 (engine, 위키 밖 작업 폴더)", [
 (i, "kb_kind", "engine"), (i, "is_a", "model.ndb (뉴로심볼릭: LLM이 단서 추출·문장 초안, 기호 규칙이 검증·점수·차단)"),
 (i, "path", "engine/engine.py (analyze 방어 / plan 공격 / check 윤리)"),
 (i, "knowledge_from", "이 위키의 설득 개체 → build_kb.py → knowledge.json"),
 (i, "implements", "rule.persuasion_fact_gate"), (i, "implements", "rule.persuasion_ethics_gate"),
 (i, "implements", CHUB), (i, "uses", HUB),
 (i, "limit", "[해석] 키워드·정규식 기반이라 문맥을 놓칠 수 있다; LLM 단서와 사람 판단으로 보완")], "설득 엔진, 뉴로심볼릭, 설득 점검")
i = "project.ndb_lecture_persuasion_202610"
ent("Project-NDBLecturePersuasion202610", i, "Topic", 0.7, SRC_PDF, [
 (i, "title", "남양주백병원 10월 직원 교육: 설득과 오판 (Spine Center 직원 역량 강화 강의 노트)"),
 (i, "organized_by", "org.namyangju_baek_hospital"), (i, "produced", HUB), (i, "source", "ref.persuasion_misjudgment_pdf"),
 (i, "sibling_of", "project.ndb_lecture_ggs_202610 (같은 10월 직원 강의 묶음, [해석])"),
 (i, "open_question", "강의자·강의 일시·대상 부서는 PDF에 없음 (미확인)")], "10월 직원 강의, 설득과 오판")

print(len(written), "entities"); 
import json
json.dump(triples, open(os.path.join(tempfile.gettempdir(), "persuasion_triples.json"), "w"), ensure_ascii=False)
