import json
import urllib.request
import base64
import ssl

# ══════════════════════════════════════════
# KONFIGURASI — sesuaikan jika perlu
# ══════════════════════════════════════════
BASE_URL = "https://cibseven2.foul.one/engine-rest"
USERNAME = "demo"
PASSWORD = "admin123"

# Skip SSL verification jika perlu
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

auth_header = "Basic " + base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()

def api_get(path):
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", auth_header)
    try:
        resp = urllib.request.urlopen(req, context=ctx)
        return json.loads(resp.read())
    except Exception as e:
        print(f"  ERROR: {e}")
        return []

# ══════════════════════════════════════════
# 1. PROCESS DEFINITIONS
# ══════════════════════════════════════════
print("=" * 80)
print("1. PROCESS DEFINITIONS YANG TERDAFTAR")
print("=" * 80)
defs = api_get("/process-definition")
for d in defs:
    print(f"  Key: {d.get('key','?'):<40} Name: {d.get('name','?')}")
print(f"\n  Total: {len(defs)} process definitions\n")

# ══════════════════════════════════════════
# 2. DECISION DEFINITIONS (DMN)
# ══════════════════════════════════════════
print("=" * 80)
print("2. DECISION DEFINITIONS (DMN)")
print("=" * 80)
decisions = api_get("/decision-definition")
for d in decisions:
    print(f"  Key: {d.get('key','?'):<40} Name: {d.get('name','?')}")
print(f"\n  Total: {len(decisions)} decision definitions\n")

# ══════════════════════════════════════════
# 3. SEMUA PROCESS INSTANCES + MONITORING
# ══════════════════════════════════════════
print("=" * 80)
print("3. TABEL MONITORING — SEMUA PROCESS INSTANCES")
print("=" * 80)
instances = api_get("/history/process-instance?sortBy=startTime&sortOrder=asc")

header = f"{'No':<4} {'Proses':<45} {'Status':<12} {'Total':<7} {'Done':<7} {'Active':<7}"
print(header)
print("-" * len(header))

for i, inst in enumerate(instances, 1):
    pid = inst["id"]
    pname = inst.get("processDefinitionName") or inst.get("processDefinitionKey", "?")
    state = inst.get("state", "?")

    activities = api_get(f"/history/activity-instance?processInstanceId={pid}")
    total = len(activities)
    done = len([a for a in activities if a.get("endTime")])
    active = total - done

    print(f"{i:<4} {pname:<45} {state:<12} {total:<7} {done:<7} {active:<7}")

print()

# ══════════════════════════════════════════
# 4. DETAIL PER INSTANCE — VARIABEL + ACTIVITIES
# ══════════════════════════════════════════
print("=" * 80)
print("4. DETAIL PER INSTANCE")
print("=" * 80)

for i, inst in enumerate(instances, 1):
    pid = inst["id"]
    pname = inst.get("processDefinitionName") or inst.get("processDefinitionKey", "?")
    state = inst.get("state", "?")

    print(f"\n--- Instance #{i}: {pname} [{state}] ---")
    print(f"    ID: {pid}")
    print(f"    Start: {inst.get('startTime','?')}")
    print(f"    End:   {inst.get('endTime','belum selesai')}")

    # Variabel
    print(f"\n    VARIABEL:")
    variables = api_get(f"/history/variable-instance?processInstanceId={pid}")
    for v in variables:
        val = v.get("value", "?")
        if isinstance(val, str) and len(val) > 80:
            val = val[:80] + "..."
        print(f"      {v.get('name','?'):<30} = {val}  ({v.get('type','?')})")

    # Activities
    print(f"\n    ACTIVITIES:")
    activities = api_get(f"/history/activity-instance?processInstanceId={pid}")
    for a in activities:
        atype = a.get("activityType", "?")
        aname = a.get("activityName", "?") or "(unnamed)"
        status = "DONE" if a.get("endTime") else "ACTIVE"
        if atype in ["startEvent", "endEvent", "noneEndEvent", "exclusiveGateway"]:
            continue  # skip noise
        print(f"      [{status:<6}] {aname} ({atype})")

# ══════════════════════════════════════════
# 5. DECISION INSTANCES (DMN RESULTS)
# ══════════════════════════════════════════
print("\n" + "=" * 80)
print("5. DECISION INSTANCES (HASIL DMN)")
print("=" * 80)
dec_instances = api_get("/history/decision-instance?includeInputs=true&includeOutputs=true")
if not dec_instances:
    print("  Belum ada decision instance (jalankan P3 dulu)")
else:
    for di in dec_instances:
        print(f"\n  Decision: {di.get('decisionDefinitionName','?')}")
        print(f"  Time: {di.get('evaluationTime','?')}")
        inputs = di.get("inputs", [])
        for inp in inputs:
            print(f"    INPUT:  {inp.get('clauseName','?')} = {inp.get('value','?')}")
        outputs = di.get("outputs", [])
        for out in outputs:
            print(f"    OUTPUT: {out.get('clauseName','?')} = {out.get('value','?')}")

print("\n" + "=" * 80)
print("SELESAI — Copy output di atas untuk data laporan BAB 7")
print("=" * 80)
