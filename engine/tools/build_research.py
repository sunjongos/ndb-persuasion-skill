#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""설득심리학 심층연구 → 위키(WIKI-CODE-022) 개체·트리플·노트 생성. 사용: python3 tools/build_research.py [위키경로]
멱등: 같은 입력이면 같은 파일. 기존 허브(020·021)·팩트 게이트·엔진 개체에는 연결 줄만 덧붙인다(이미 있으면 건너뜀)."""
import os, sys, json, csv, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from research_src import *

WIKI = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ontology")
ENT = os.path.join(WIKI, "entities")
DAY = "2026-10-25"
SRC_LINE = f"설득심리학 심층연구 도시에 {DAY} (research: dossier.md·sources.csv 149개 출처 Crossref DOI·URL 존재·제목 확인·ontology_additions.json·engine_rules_additions.json). 효과 크기는 초록 기준(원문 표 미대조)"

O = json.load(open(os.path.join(RESEARCH_DIR, "ontology_additions.json"), encoding="utf-8"))
R = json.load(open(os.path.join(RESEARCH_DIR, "engine_rules_additions.json"), encoding="utf-8"))
S = {r["id"]: r for r in csv.DictReader(open(os.path.join(RESEARCH_DIR, "sources.csv"), encoding="utf-8-sig"))}
written, triples_all, unmapped = [], [], {}

ACCT_RE = re.compile(r"(?<![\d.,])\d{8,14}-\d{1,3}(?![\d,])|(?<![\d.,])\d{3,6}-\d{2,6}-\d{4,8}(?![\d,])")
ENCODED = set()
def safe_url(u):
    """위키 C11(계좌형 번호) 검사에 걸리는 DOI는 하이픈을 %2D로 퍼센트 인코딩(doi.org에서 그대로 해석됨)"""
    if ACCT_RE.search(u): ENCODED.add(u); return u.replace("-", "%2D")
    return u
def src(sid):
    r = S.get(sid)
    if not r: unmapped[sid] = "sources.csv에 없음"; return f"src:{sid}"
    return f"src:{sid} ({safe_url(r['DOI 또는 URL'])}) [등급 {r['근거 등급']}]"

def abs_tag(s):
    """수치가 있으면 원문 표 미대조 표시"""
    return s + " (수치: 초록 기준, 원문 표 미대조)" if re.search(r"\d", s) and "초록 기준" not in s else s

def mref(ref):
    ids = map_ref(ref)
    if not ids: unmapped[ref] = "매핑 대상 없음"
    elif ref in UNMAPPED_NOTES: unmapped[ref] = UNMAPPED_NOTES[ref] + " → " + ", ".join(ids)
    return ids

def write(fname, eid, conf, lines, search, source=SRC_LINE, typ="Topic"):
    body = [f"- {eid} - {r} - {o}" for r, o in lines]
    txt = f"---\nid: {eid}\ntype: {typ}\nupdated: {DAY}\nconfidence: {conf}\nsource: {source}\n---\n" + "\n".join(body) + f"\n> 검색어: {search}\n"
    open(os.path.join(ENT, fname), "w", encoding="utf-8").write(txt)
    written.append(fname); triples_all.extend((eid, r, o) for r, o in lines)

# 1) 등급·재현 실패 개체
for g in "ABCD":
    L = [("kb_kind", "evidence_grade"), ("grade", g), ("definition", f"[자료 내용] {GRADE_DEF[g]}"), ("part_of", HUB)]
    if g == "D": L += [("engine_policy", "[해석] 엔진은 D등급 기법을 추천하지 않고, 사용 주장이 보이면 '재현 실패'로 경고·차단한다"), ("related", REPL_FAILED)]
    write(f"Concept-EvidenceGrade{g}.md", GRADE_ID[g], 0.9, L, f"근거 등급 {g}, 설득 연구 신뢰도")
ents = {e["id"]: e for e in O["entities"]}
dl = [e["id"] for e in O["entities"] if e["evidence_grade"] == "D"]
write("Concept-ReplicationFailed.md", REPL_FAILED, 0.85,
      [("kb_kind", "replication_flag"), ("definition", "[자료 내용] 다기관·사전등록 재현에서 효과가 거의 0이거나 재현되지 않은 연구"), ("part_of", HUB),
       ("grade", GRADE_ID["D"])] + [("flags", wid(x)) for x in dl] +
      [("partially_flags", "principle.cialdini_presuasion (점화 부분만; '주의 초점'은 생존)"), ("source", src("OSC2015")), ("source", src("KLEIN2014")), ("source", src("KLEIN2018"))],
      "재현 실패, 재현 위기, D등급")

# 2) 연구 개체 69
extra = {}
for t in O["triples"]:
    if t["predicate"] == "evidence_grade": continue
    if (t["subject"], t["predicate"], t["object"]) in DROP_TRIPLES:
        unmapped[f"{t['subject']} {t['predicate']} {t['object']}"] = "방향 역전 의심(반발 이론이 BYAF를 반박하는 것이 아니라 BYAF가 반발을 완화) → 생략, 역방향 트리플만 유지"; continue
    if t["object"].startswith("theory.prospect("): t["object"] = "theory.prospect"; t["predicate"] += "_message_myth"
    objs = mref(t["object"]) if not t["object"].split(".")[0] in ("theory", "technique", "study", "bias", "defense", "case") else [wid(t["object"])]
    for o in objs:
        note = " (점화 부분 제외)" if t["object"].startswith("Cialdini:초전") else ""
        extra.setdefault(t["subject"], []).append((t["predicate"], f"{o}{note} (근거: {', '.join(t['sources'])})"))
for e in O["entities"]:
    oid, g = e["id"], e["evidence_grade"]
    L = [("kb_kind", "research_item"), ("orig_id", oid), ("item_type", e["type"]), ("name_ko", e["name_ko"]), ("name_en", e["name"]),
         ("part_of", HUB), ("evidence_grade", GRADE_ID[g]),
         ("summary", "[자료 내용] " + abs_tag(SUMMARY_FIX.get(oid, e["summary"])))]
    if oid in EFFECT: L.append(("effect_size", f"[자료 내용] {EFFECT[oid]} (초록 기준, 원문 표 미대조)"))
    if e.get("misuse_risk"): L.append(("misuse_risk", "[자료 내용] " + e["misuse_risk"]))
    if g == "D": L += [("replication", REPL_FAILED), ("engine_policy", "추천 금지 (ban.grade_D)")]
    for ref in e.get("links_existing") or []:
        for o in mref(ref): L.append(("relates_to", o + (" (점화 부분 제외)" if ref.startswith("Cialdini:초전") else "")))
    L += extra.get(oid, [])
    L += [("source", src(s)) for s in e["sources"]]
    if any(r == "contradicts" for r, _ in L):
        L.append(("resolution", "[해석] 연구 간 실제 논쟁으로 보존한다. 엔진은 근거 등급이 높은 쪽(A>B>C>D)을 기본값으로 쓰고, D등급 쪽은 추천하지 않는다"))
    if oid == "theory.elm": L.append(("same_as", "concept.elm_routes (PDF·대표님 철학 쪽 ELM 개체)"))
    write(wfile(oid), wid(oid), GRADE_CONF[g], L, f"{e['name_ko']}, {e['name']}, 설득 심층연구")

# 3) 엔진 규칙 50
for r in R["rules"]:
    oid = r["id"]; lvl, det, label = DETECT[oid]
    gr = sorted(set(r.get("source_grades") or []))
    L = [("kb_kind", "research_rule"), ("orig_id", oid), ("rule_kind", r["kind"]), ("label", label), ("level", lvl),
         ("grades", "/".join(gr)), ("part_of", HUB)] + [("evidence_grade", GRADE_ID[x]) for x in gr]
    L.append(("detector", json.dumps(det, ensure_ascii=False)))
    L.append(("when", "[자료 내용] " + json.dumps(r["when"], ensure_ascii=False)))
    L.append(("then", "[자료 내용] " + json.dumps(r["then"], ensure_ascii=False)))
    th = r["then"]
    for k in ("prefer", "avoid"):
        for x in th.get(k, []) if isinstance(th.get(k), list) else []:
            m = re.match(r"^(technique\.[a-z0-9_]+)(.*)$", x)
            L.append((k, wid(m.group(1)) + (f" {m.group(2)}" if m.group(2) else "") if m else x))
    for x in th.get("map", []) or []:
        for o in mref(x): L.append(("maps_to", o))
    if r.get("severity"): L.append(("severity", r["severity"]))
    L += [("source", src(s)) for s in r["sources"]]
    L.append(("implemented_by", "model.persuasion_engine"))
    write(rfile(oid), rid(oid), 0.8 if "C" not in gr and "D" not in gr else 0.7, L, f"설득 엔진 규칙 {oid}, {label}")

# 4) 출처 레지스트리
L = [("kb_kind", "source_registry"), ("part_of", HUB), ("count", str(len(S)))]
for sid, r in S.items():
    L.append(("cites", f"{sid} :: {r['저자']} {r['연도']} :: {r['제목']} :: {r['학술지/출판사']} :: {safe_url(r['DOI 또는 URL'])} :: 등급 {r['근거 등급']}"))
write("Ref-PersuasionResearchSources.md", "ref.persuasion_research_sources", 0.9, L, "설득 심층연구 출처 149, DOI")

# 5) 핵심 발견 7 + 찬반 검증
fids = []
for i, (slug, title, claim, srcs, g, links, rel) in enumerate(FINDINGS, 1):
    fid = f"concept.pr_finding_{slug}"; fids.append(fid)
    L = [("kb_kind", "research_finding"), ("number", str(i)), ("name_ko", title), ("part_of", HUB), ("evidence_grade", GRADE_ID[g]),
         ("claim", f"[자료 내용] {abs_tag(claim)}")] + [("about", x) for x in links] + [("source", src(s)) for s in srcs]
    tgt = {"supports": "principle.fact_before_persuasion", "supports_psychology": "principle.politics_psychology_first"}.get(rel)
    if tgt: L.append(("supports", tgt))
    else: L.append(("qualifies", "concept.ceo_persuasion_philosophy"))
    write(f"Concept-PRFinding{camel(slug)}.md", fid, GRADE_CONF[g], L, f"설득 핵심 발견 {i}, {title}")
L = [("kb_kind", "evidence_review"), ("name_ko", "대표님 원칙에 대한 찬반 증거"), ("part_of", HUB), ("reviews", "concept.ceo_persuasion_philosophy")]
L += [("pro_psychology", f"[자료 내용] {c} (근거: {', '.join(s)})") for c, s in PRO]
L += [("pro_facts", f"[자료 내용] {c} (근거: {', '.join(s)})") for c, s in CON]
L += [("supports", "principle.politics_psychology_first (행동·정체성·반복 영역 한정)"), ("supports", "principle.fact_before_persuasion (태도 변화 영역)"),
      ("grounds", "rule.persuasion_fact_gate (설득-정확도 상충: concept.bias_persuasion_accuracy_tradeoff)"),
      ("synthesis", f"[자료 내용] {SYNTH}"), ("conclusion", f"[해석] {CONCLUSION}")] + [("uses_finding", f) for f in fids]
write("Concept-PRCEOEvidenceReview.md", "concept.pr_ceo_evidence_review", 0.8, L, "대표님 설득 원칙 찬반 증거, 사실은 엔진 심리는 변속기")

# 6) 대표님 3단계 격언 (021 소속)
L = [("kb_kind", "ceo_principle"), ("name_ko", "하수·중수·고수 (팩트 위에서 설득해 행동과 결과를 만든다)"), ("part_of", "concept.ceo_persuasion_philosophy"),
     ("said_by", f"person.choi_sunjong ({DAY} 대화)"), ("fact", MAXIM)]
L += [("level", f"{n} :: {a} :: {b}") for n, a, b in LEVELS]
L += [("step", f"{i} :: {s}") for i, s in enumerate(STEPS, 1)]
L += [("maps_to", "principle.fact_persuasion_matrix (하수≈사기꾼·무존재 / 중수≈팩트보다 심리 / 고수≈리더+행동 설계)"),
      ("enforced_by", "rule.persuasion_fact_gate"), ("extends", "principle.fact_before_persuasion"),
      ("supported_by", "concept.pr_finding_fact_density (팩트 위 설득: 정보 밀도가 엔진)"),
      ("supported_by", "concept.pr_finding_attitude_behavior (고수 3단계: 행동은 요청·실행 계획으로)"),
      ("supported_by", "concept.pr_finding_illusory_truth (중수의 반복·심리 기술은 일시 효과 + 방어 필요)"),
      ("uses", "concept.technique_byaf"), ("uses", "concept.technique_implementation_intention"), ("uses", "concept.technique_direct_ask"),
      ("note", "[해석] 엔진 plan·check의 mastery 라벨로 하수/중수/고수를 표시한다"), ("implemented_by", "model.persuasion_engine")]
write("Principle-CEOMasteryLevels.md", MASTERY_ID, 0.9, L, "하수 중수 고수, 팩트 위에서 설득, 대표님 설득 격언",
      source=f"대표님 말씀 {DAY} 대화 (부모 에이전트 전달) + 설득심리학 심층연구(WIKI-CODE-022) 연결")

# 7) 허브 022
L = [("wiki_code", HUB_CODE), ("kb_kind", "hub"), ("name_ko", "설득심리학 심층연구"), ("extends", "concept.persuasion_misjudgment"),
     ("governed_by", "concept.ceo_persuasion_philosophy"), ("source", "ref.persuasion_research_sources"),
     ("summary", f"[자료 내용] 출처 149개(A·B·C·D 등급)로 PDF(020)를 넘어 이론 21·기법 27·연구 8·방어 5·편향 4·사례 4와 엔진 규칙 50을 정리"),
     ("synthesis", f"[자료 내용] {SYNTH}"), ("limit", "[자료 내용] 효과 크기 일부는 초록·기존 지식 기준; 동료심사 전 원고는 C; 대부분 WEIRD 표본, 한국 재현 부족")]
L += [("has_grade", GRADE_ID[g]) for g in "ABCD"] + [("has_finding", f) for f in fids] + [("has_review", "concept.pr_ceo_evidence_review"), ("has_flag", REPL_FAILED)]
L += [("has_item", wid(e["id"])) for e in O["entities"]] + [("has_rule", rid(r["id"])) for r in R["rules"]]
L += [("implemented_by", "model.persuasion_engine")]
write("Concept-PersuasionResearch.md", HUB, 0.85, L, "설득심리학 심층연구, 근거 등급, 재현 실패, 설득 엔진 규칙")

# 8) 기존 개체에 연결 줄 덧붙이기(멱등)
def append(fname, eid, lines):
    p = os.path.join(ENT, fname); t = open(p, encoding="utf-8").read()
    add = [f"- {eid} - {r} - {o}" for r, o in lines if f"- {eid} - {r} - {o}" not in t]
    if not add: return 0
    i = t.rfind("\n> 검색어:")
    t = t[:i] + "\n" + "\n".join(add) + t[i:]
    open(p, "w", encoding="utf-8").write(t); triples_all.extend((eid, r, o) for r, o in lines); return len(add)
app = {}
app["020"] = append("Concept-PersuasionMisjudgment.md", "concept.persuasion_misjudgment", [("extended_by", HUB + " (WIKI-CODE-022 설득심리학 심층연구)"), ("partially_flagged_by", REPL_FAILED + " (점화·자아 고갈 근거)")])
app["021"] = append("Concept-CEOPersuasionPhilosophy.md", "concept.ceo_persuasion_philosophy", [
    ("refined_by", HUB + " (WIKI-CODE-022)"), ("evidence_reviewed_by", "concept.pr_ceo_evidence_review"),
    ("has_principle", MASTERY_ID), ("maxim", MAXIM),
    ("conclusion", f"[해석] {CONCLUSION}"), ("synthesis", f"[자료 내용] {SYNTH} (WIKI-CODE-022)")] + [("key_finding", f) for f in fids])
app["gate"] = append("Rule-PersuasionFactGate.md", "rule.persuasion_fact_gate", [
    ("grounded_by", "concept.bias_persuasion_accuracy_tradeoff (설득력↑ → 정확도↓: 팩트 게이트의 실증 근거)"),
    ("fact_kind", "fact:counterargument (주요 반대 근거와 그 반박(고관여·중대 결정))"),
    ("checklist", "[자료 내용] 사업가 vs 사기꾼 판정표 7: 출처·최적화 후 정확도 재검사·반대 근거·의도/이해관계/AI 공개·BYAF·다크패턴 7종·D등급 기법 금지"),
    ("extended_by", HUB)])
app["engine"] = append("Model-PersuasionEngine.md", "model.persuasion_engine", [
    ("version", "1.1 (2026-10-25: 심층연구 규칙 50·근거 등급 표시·청중 상태 전략·다크패턴·D등급 금지·하수/중수/고수 라벨)"),
    ("implements", HUB), ("implements", MASTERY_ID)])
app["matrix"] = append("Principle-FactPersuasionMatrix.md", "principle.fact_persuasion_matrix", [("refined_by", MASTERY_ID + " (하수·중수·고수)")])

# 9) 노트 022 + 트리플 TSV
nd = os.path.join(WIKI, "notes", HUB_CODE); os.makedirs(nd, exist_ok=True)
items = O["entities"]
def row(e): return f"| {e['name_ko']} | {wid(e['id'])} | {e['evidence_grade']} | {EFFECT.get(e['id'], '-') + (' (초록 기준)' if e['id'] in EFFECT else '')} | {', '.join(e['sources'])} |"
md = [f"---\nwiki_id: {HUB_CODE}\ntitle: \"설득심리학 심층연구: 근거 등급·재현성·엔진 규칙\"\nentity: {HUB}\nsource: {SRC_LINE}\ncreated_at: {DAY}\n"
      f"note: 도시에 문구·수치 그대로 [자료 내용], 위키 연결·엔진 구현은 [해석]. 정치인 실명은 넣지 않았다(bot.politics). 외집단 적대 정규식의 정치 비하어는 탐지 패턴으로만 쓴다.\n---",
      "## 1. 본질", f"- [자료 내용] {SYNTH}.", f"- [해석] {CONCLUSION}.",
      "- [해석] WIKI-CODE-020(PDF 도구)을 근거 등급으로 다시 거르고, WIKI-CODE-021(대표님 철학)에 찬반 증거를 붙인다.",
      "", "## 2. 핵심 발견 7"]
for i, (slug, title, claim, srcs, g, links, rel) in enumerate(FINDINGS, 1):
    md.append(f"{i}. **{title}** [자료 내용] {claim} [{']['.join(srcs)}] — 등급 {g} → concept.pr_finding_{slug}")
md += ["", "## 3. 근거 등급", "| 등급 | 뜻 | 개수 |", "|---|---|---|"]
for g in "ABCD": md.append(f"| {g} | {GRADE_DEF[g]} | {sum(1 for e in items if e['evidence_grade'] == g)} |")
md += ["", "D등급(재현 실패): " + ", ".join(wid(x) for x in dl) + " → 엔진 추천 금지(ban.grade_D).", "", "## 4. 개체 (이론·기법·연구·방어·편향·사례)",
       "효과 크기는 모두 도시에 문구 그대로이며 원문 표와 대조하지 않았다(초록 기준).", "", "| 이름 | 위키 id | 등급 | 효과 크기 | 출처 id |", "|---|---|---|---|---|"]
md += [row(e) for e in items]
md += ["", "## 5. 엔진 규칙 50 (rule.pr_*)", "| 규칙 | 종류 | 수준 | 등급 | 설명 |", "|---|---|---|---|---|"]
for r in R["rules"]:
    md.append(f"| {r['id']} | {r['kind']} | {DETECT[r['id']][0]} | {'/'.join(sorted(set(r['source_grades'])))} | {DETECT[r['id']][2]} |")
md += ["", "## 6. 이름 참조 매핑 주의", *[f"- {k}: {v}" for k, v in UNMAPPED_NOTES.items()],
       "- theory.reactance counters technique.byaf: 방향 역전 의심 → 생략(technique.byaf counters theory.reactance만 유지)",
       "", "## 7. 한계", "- [자료 내용] 효과 크기 일부는 초록·기존 지식에서 가져옴 → 원문 표 대조 권장.",
       "- [자료 내용] COSTELLO2025·HACKEN2026B·SCHOEN2025·ELSAYED2024는 동료심사 전 원고(C).", "- [자료 내용] 대부분 WEIRD 표본, 한국 재현 부족.",
       "", "## 8. 연결", "- 위: concept.ceo_persuasion_philosophy (WIKI-CODE-021), principle.ceo_mastery_levels", "- 확장 대상: concept.persuasion_misjudgment (WIKI-CODE-020)",
       "- 출처: ref.persuasion_research_sources (149개, id·DOI)", "- 실행: model.persuasion_engine (engine, v1.1)"]
open(os.path.join(nd, f"{HUB_CODE}.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
with open(os.path.join(nd, f"{HUB_CODE}.triples.tsv"), "w", encoding="utf-8") as f:
    f.write("subject\trelation\tobject\n")
    for s, r, o in triples_all: f.write(f"{s}\t{r}\t{o.replace(chr(9), ' ')}\n")

# 10) 021 노트 보강(멱등)
p21 = os.path.join(WIKI, "notes", "WIKI-CODE-021", "WIKI-CODE-021.md"); t21 = open(p21, encoding="utf-8").read()
MARK = "## 7. 심층연구 보강 (WIKI-CODE-022)"
if MARK not in t21:
    s = ["", MARK, "### 7.1 핵심 발견 7"]
    for i, (slug, title, claim, srcs, g, links, rel) in enumerate(FINDINGS, 1):
        s.append(f"{i}. [자료 내용] {title}: {claim} [{']['.join(srcs)}] (등급 {g})")
    s += ["### 7.2 대표님 원칙에 대한 찬반 증거", "**'심리가 팩트보다 강하다'를 지지 (심리 쪽)**"]
    s += [f"- [자료 내용] {c} [{']['.join(x)}]" for c, x in PRO]
    s += ["**'팩트는 약하다'는 통념에 반대 (팩트 쪽)**"] + [f"- [자료 내용] {c} [{']['.join(x)}]" for c, x in CON]
    s += [f"- [자료 내용] 종합: {SYNTH}.", f"- [해석] 결론: {CONCLUSION}.",
          "- [해석] 대표님의 '정치는 심리'는 행동·정체성·반복 영역에 한정해 맞고, '팩트 없는 설득은 사기꾼'은 태도 변화 영역과 설득-정확도 상충 실험으로 실증 뒷받침된다.",
          "", "## 8. 대표님 격언: 하수·중수·고수 (2026-10-25)", f"> {MAXIM}", "", "| 단계 | 방식 | 결과 |", "|---|---|---|"]
    s += [f"| {n} | {a} | {b} |" for n, a, b in LEVELS]
    s += ["", "**고수 4단계**"] + [f"{i}. {x}" for i, x in enumerate(STEPS, 1)]
    s += ["", "- [해석] 사분면 대응: 하수 ≈ 사기꾼·무존재(팩트 게이트 BLOCKED), 중수 ≈ 팩트보다 심리(근거 없는 수치·반복·압박 → REVISE), 고수 ≈ 리더 + 행동 설계(BYAF·실행 계획).",
          "- [해석] 연구 연결: 팩트 위 설득 = concept.pr_finding_fact_density, 행동 설계 = concept.pr_finding_attitude_behavior, 중수의 반복 의존 = concept.pr_finding_illusory_truth.",
          "- 개체: principle.ceo_mastery_levels → principle.fact_persuasion_matrix, rule.persuasion_fact_gate", "",
          "## 9. 연결 추가", "- 근거 보강: concept.persuasion_research (WIKI-CODE-022), concept.pr_ceo_evidence_review"]
    open(p21, "w", encoding="utf-8").write(t21.rstrip("\n") + "\n" + "\n".join(s) + "\n")
p20 = os.path.join(WIKI, "notes", "WIKI-CODE-020", "WIKI-CODE-020.md"); t20 = open(p20, encoding="utf-8").read()
if "WIKI-CODE-022" not in t20:
    open(p20, "w", encoding="utf-8").write(t20.rstrip("\n") + "\n\n## 심층연구 연결\n- 근거 등급·재현성 보강: concept.persuasion_research (WIKI-CODE-022). 점화·자아 고갈 근거는 D등급(concept.replication_failed).\n")

print(json.dumps(dict(encoded_doi=len(ENCODED), files=len(written), new_triples=len(triples_all), appended=app, unmapped=unmapped), ensure_ascii=False, indent=1))
