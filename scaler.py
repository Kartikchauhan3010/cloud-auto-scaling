import psutil
import random
import time

servers = {
    "server-1": {"cpu": 30, "memory": 50},
    "server-2": {"cpu": 40, "memory": 60}
}

history = []

def simulate_server_load():
    for s in servers:
        servers[s]["cpu"] = random.randint(10, 95)
        servers[s]["memory"] = random.randint(20, 90)

def scaling_engine():

    cpu_values = [servers[s]["cpu"] for s in servers]
    avg_cpu = sum(cpu_values) / len(cpu_values)

    decision = "Stable"

    if avg_cpu > 75:
        new_server = f"server-{len(servers)+1}"
        servers[new_server] = {
            "cpu": random.randint(20,50),
            "memory": random.randint(30,60)
        }
        decision = "Scale Up"

    elif avg_cpu < 25 and len(servers) > 1:
        servers.pop(list(servers.keys())[-1])
        decision = "Scale Down"

    history.append({
        "time": time.strftime("%H:%M:%S"),
        "instances": len(servers),
        "cpu": avg_cpu
    })

    if len(history) > 20:
        history.pop(0)

    return decision

def get_system_metrics():

    simulate_server_load()

    decision = scaling_engine()

    local_cpu = psutil.cpu_percent(interval=1)
    local_memory = psutil.virtual_memory().percent

    return {
        "servers": servers,
        "decision": decision,
        "local_cpu": local_cpu,
        "local_memory": local_memory,
        "history": history
    }