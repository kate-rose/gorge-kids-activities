"""Build winter.html from tools/winter_template.html + tools/winter_data.py.

    python3 tools/build_winter.py
"""
import json, pathlib, sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from winter_data import A

TYPES = {"help", "meals", "events", "library", "outdoors", "arts"}
COUNTIES = {"Skamania", "Klickitat", "Hood River", "Wasco"}
AGES = {"babies", "kids", "teens"}
REQUIRED = ["name", "category", "dates", "location", "ages", "cost", "desc", "link", "counties", "ageGroups", "types", "es"]

errors, names = [], set()
for a in A:
    n = a.get("name", "?")
    for k in REQUIRED:
        if not a.get(k):
            errors.append(f"{n}: missing {k}")
    if n in names:
        errors.append(f"{n}: duplicate name")
    names.add(n)
    if set(a.get("types", [])) - TYPES: errors.append(f"{n}: bad type {a['types']}")
    if set(a.get("counties", [])) - COUNTIES: errors.append(f"{n}: bad county {a['counties']}")
    if set(a.get("ageGroups", [])) - AGES: errors.append(f"{n}: bad age {a['ageGroups']}")
    for k in ("deadline", "until"):
        if a.get(k): date.fromisoformat(a[k])
    if not a.get("link", "").startswith("https://"):
        errors.append(f"{n}: link not https")
if errors:
    sys.exit("\n".join(errors))

cards = [{k: v for k, v in a.items() if k != "es"} for a in A]
tr = {a["name"]: {"name": a["es"][0], "desc": a["es"][1]} for a in A}

tmpl = (ROOT / "tools" / "winter_template.html").read_text()
out = (tmpl.replace("/*DATA*/[]", json.dumps(cards, ensure_ascii=False, indent=1))
           .replace("/*TR*/{}", json.dumps(tr, ensure_ascii=False, indent=1)))
(ROOT / "winter.html").write_text(out)
print(f"winter.html: {len(cards)} listings "
      f"({sum('help' in a['types'] for a in A)} holiday help, {sum('meals' in a['types'] for a in A)} food)")
