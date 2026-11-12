#!/usr/bin/env python3
"""Holt Runen-Daten + Icons aus Riots Data Dragon (offizielle Fan-Daten-API).
Aufruf: python3 tools/fetch_data.py [version]  -> data/runes_<lang>.json, img/..."""
import json, os, sys, urllib.request
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"lol-runes"}), timeout=30) as r:
        return r.read()
ver = sys.argv[1] if len(sys.argv) > 1 else json.loads(get("https://ddragon.leagueoflegends.com/api/versions.json"))[0]
os.makedirs(f"{BASE}/data", exist_ok=True)
icons = set()
for lang in ("en_US", "de_DE"):
    d = json.loads(get(f"https://ddragon.leagueoflegends.com/cdn/{ver}/data/{lang}/runesReforged.json"))
    json.dump({"version": ver, "trees": d}, open(f"{BASE}/data/runes_{lang}.json", "w"), ensure_ascii=False)
    for t in d:
        icons.add(t["icon"])
        for s in t["slots"]:
            for r in s["runes"]: icons.add(r["icon"])
for n in ["StatModsAdaptiveForceIcon","StatModsAttackSpeedIcon","StatModsCDRScalingIcon","StatModsMovementSpeedIcon","StatModsHealthPlusIcon","StatModsHealthScalingIcon","StatModsTenacityIcon"]:
    icons.add(f"perk-images/StatMods/{n}.png")
miss = []
for i in sorted(icons):
    p = f"{BASE}/img/{i}"
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if os.path.exists(p): continue
    try: open(p, "wb").write(get(f"https://ddragon.leagueoflegends.com/cdn/img/{i}"))
    except Exception as e: miss.append(i)
print("version", ver, "icons", len(icons), "missing", miss)
