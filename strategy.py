import os
import sys
from cpz.clients.sync import CPZClient

# --- Set credentials ---
os.environ["CPZ_AI_API_KEY"] = "cpz_key_882a2fb5a3274d54b600bac6"
os.environ["CPZ_AI_SECRET_KEY"] = "cpz_secret_46133v3n495s1s2nc342h577725e2f2w1t5s1g252u43m3c1"
os.environ["CPZ_STRATEGY_ID"] = "13197d7e-22b4-4b62-9d44-58b901a359c7"

# --- Direct argument values ---
qty = 1
strategy_id = os.getenv("CPZ_STRATEGY_ID")
env = "live"         # choose "paper" or "live"
broker = "alpaca"     # choose broker name


# --- Execute order ---
client = CPZClient()
client.execution.use_broker(broker, environment="live", account_id="899921312")

order = client.execution.order(
    symbol="GPRO",
    qty=qty,
    side="buy",
    order_type="market",
    time_in_force="DAY",
    strategy_id=strategy_id,
)

print(order.model_dump_json())
