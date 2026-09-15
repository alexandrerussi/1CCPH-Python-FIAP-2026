# repo.py

from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

# CRUD
# CREATE - create_lead()
# READ - read_leads()
# UPDATE
# DELETE

def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        # se corromper, começar vazio
        return []

def create_lead(lead_dict):
    leads = read_leads() # lista de leads
    leads.append(lead_dict)

    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

def read_leads_search(query):
    leads = read_leads() # lista de leads
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} {lead["company"]} {lead["email"]}".lower()

        if query in txt_lead:
            results.append(lead)

    if not results:
        print("Nada encontrado")
        return
    else:
        return results
