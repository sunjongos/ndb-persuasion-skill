#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""위키 설득 온톨로지 → knowledge.json (기호 계층). 사용: python3 build_kb.py [위키경로] [출력경로]
위키 개체 중 'kb_kind' 트리플이 있는 것만 읽는다. 위키가 정본이고 이 파일은 파생물이다."""
import os, re, sys, json, glob, hashlib

WIKI = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ontology")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "knowledge.json")
TRIPLE = re.compile(r"^- (\S+) - (\S+) - (.+)$")
IDTOK = re.compile(r"^([a-z]+\.[a-z0-9_]+)")

def parse(path):
    t = open(path, encoding="utf-8").read()
    m = re.search(r"^id: (\S+)$", t, re.M)
    conf = re.search(r"^confidence: (\S+)$", t, re.M)
    trip = [TRIPLE.match(l).groups() for l in t.splitlines() if TRIPLE.match(l)]
    return (m.group(1) if m else None), float(conf.group(1)) if conf else None, trip

def cues(s): return [c.strip() for c in s.split(";") if c.strip()]
def ref(o):
    m = IDTOK.match(o); return m.group(1) if m else o

def build():
    ents = {}
    for f in sorted(glob.glob(os.path.join(WIKI, "entities", "*.md"))):
        eid, conf, trip = parse(f)
        if not eid: continue
        own = [(r, o) for s, r, o in trip if s == eid]
        kinds = [o for r, o in own if r == "kb_kind"]
        if kinds: ents[eid] = dict(kind=kinds[0], conf=conf, own=own, all=trip, file=os.path.basename(f))
    kb = dict(principles={}, tendencies={}, combos={}, defenses={}, cases={}, ceo_principles={}, gates={},
              signals=[], fact_kinds={}, elm={}, message_order={}, amplifies=[], persuader_types=[], hubs={},
              research_items={}, research_rules={}, grades={}, findings={}, sources={}, mastery={})
    def srcid(o): m = re.match(r"src:(\w+)", o); return m.group(1) if m else o
    def g(own, rel): return [o for r, o in own if r == rel]
    def g1(own, rel, d=""): v = g(own, rel); return v[0] if v else d
    for eid, e in ents.items():
        k, own = e["kind"], e["own"]
        if k == "principle":
            kb["principles"][eid] = dict(name=g1(own, "name_ko"), pillar=g1(own, "pillar"),
                triggers=[ref(o) for o in g(own, "triggers")], defenses=[ref(o) for o in g(own, "defended_by")],
                requires=[re.match(r"fact:(\w+)", o).group(1) for o in g(own, "requires")],
                cues=[c for o in g(own, "cue") for c in cues(o)], misuse=g1(own, "misuse"), ethical_use=g1(own, "ethical_use"),
                hospital_use=g1(own, "hospital_use"))
        elif k == "tendency":
            kb["tendencies"][eid] = dict(number=int(g1(own, "number", "0")), name=g1(own, "name_ko"), group=g1(own, "group"),
                cues=[c for o in g(own, "cue") for c in cues(o)], countered_by=g(own, "countered_by"),
                triggered_by=g(own, "triggered_by"), mechanism=g1(own, "mechanism"))
        elif k == "combo":
            kb["combos"][eid] = dict(name=g1(own, "name_ko"), valence=g1(own, "valence"), members=g(own, "member"),
                broken_by=g(own, "broken_by"), description=g1(own, "description"))
            for s, r, o in e["all"]:
                if r == "amplifies": kb["amplifies"].append([s, ref(o), eid])
        elif k == "defense":
            kb["defenses"][eid] = dict(name=g1(own, "name_ko"), layer=g1(own, "layer"), how=g1(own, "how"), counters=g(own, "counters"))
        elif k == "case":
            kb["cases"][eid] = dict(name=g1(own, "name_ko"), illustrates=g(own, "illustrates"), description=g1(own, "description"))
        elif k == "ceo_principle":
            hooks = {}
            for o in g(own, "cue"):
                if "::" in o:
                    n, c = o.split("::", 1); hooks[n.strip()] = cues(c)
                else: hooks.setdefault("_", []).extend(cues(o))
            kb["ceo_principles"][eid] = dict(name=g1(own, "name_ko"), facts=g(own, "fact"), hooks=hooks)
            if g(own, "level"):
                kb["mastery"] = dict(id=eid, maxim=g1(own, "fact"),
                    levels=[dict(zip(("name", "how", "result"), [x.strip() for x in o.split("::")])) for o in g(own, "level")],
                    steps=[o.split("::", 1)[1].strip() for o in g(own, "step")])
        elif k == "research_item":
            gr = g1(own, "evidence_grade")[-1:].upper()
            kb["research_items"][eid] = dict(orig=g1(own, "orig_id"), type=g1(own, "item_type"), name=g1(own, "name_ko"), grade=gr,
                summary=g1(own, "summary"), effect=g1(own, "effect_size"), misuse=g1(own, "misuse_risk"),
                sources=[srcid(o) for o in g(own, "source")], replication_failed=bool(g(own, "replication")))
        elif k == "research_rule":
            kb["research_rules"][g1(own, "orig_id")] = dict(id=eid, kind=g1(own, "rule_kind"), label=g1(own, "label"), level=g1(own, "level"),
                grades=g1(own, "grades"), detector=json.loads(g1(own, "detector", "{}")), prefer=g(own, "prefer"), avoid=g(own, "avoid"),
                maps_to=[ref(o) for o in g(own, "maps_to")], sources=[srcid(o) for o in g(own, "source")],
                then=json.loads(g1(own, "then").replace("[자료 내용] ", "", 1) or "{}"))
        elif k == "evidence_grade":
            kb["grades"][g1(own, "grade")] = dict(id=eid, definition=g1(own, "definition"))
        elif k == "research_finding":
            kb["findings"][eid] = dict(number=int(g1(own, "number", "0")), name=g1(own, "name_ko"), claim=g1(own, "claim"),
                sources=[srcid(o) for o in g(own, "source")])
        elif k == "source_registry":
            for o in g(own, "cites"):
                parts = [x.strip() for x in o.split(" :: ")]
                kb["sources"][parts[0]] = dict(ref=parts[1], url=parts[4].replace("%2D", "-"), grade=parts[-1].replace("등급 ", ""))
        elif k == "gate":
            kb["gates"][eid] = dict(rules=g(own, "rule"))
            for o in g(own, "signal"):
                code, name, level, rx, fk = [x.strip() for x in o.split(" :: ")]
                kb["signals"].append(dict(code=code, name=name, level=level, regex=rx, requires_fact=None if fk == "-" else fk))
            for o in g(own, "fact_kind"):
                m = re.match(r"fact:(\w+) \((.*)\)$", o); kb["fact_kinds"][m.group(1)] = m.group(2)
        elif k == "elm":
            for o in g(own, "route"):
                lvl, name, desc = [x.strip() for x in o.split("::")]
                kb["elm"][lvl] = dict(route=name, guidance=desc)
        elif k == "message_order":
            kb["message_order"] = {r: o for r, o in own if r in ("order", "logos", "ethos", "pathos")}
        elif k == "persuader_types":
            kb["persuader_types"] = g(own, "type")
        elif k == "hub":
            kb["hubs"][eid] = g1(own, "wiki_code")
    for s in kb["signals"]: re.compile(s["regex"])  # 정규식 검증
    for r in kb["research_rules"].values():
        for key, v in r["detector"].items():
            if isinstance(v, str) and key in ("any", "threat", "efficacy", "story", "number", "disclosure", "counter", "request", "byaf", "except"): re.compile(v)
    src = "".join(open(os.path.join(WIKI, "entities", e["file"]), encoding="utf-8").read() for e in ents.values())
    kb["_meta"] = dict(source_wiki="ontology" if len(sys.argv) <= 1 else WIKI, entities=len(ents), wiki_sha256=hashlib.sha256(src.encode()).hexdigest()[:16],
                       counts={k: len(v) for k, v in kb.items() if isinstance(v, (dict, list))})
    return kb

if __name__ == "__main__":
    kb = build()
    json.dump(kb, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("knowledge.json:", kb["_meta"]["counts"])
