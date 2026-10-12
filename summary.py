import csv

def read_orders(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

orders = read_orders("orders.csv")
print(len(orders), "orders loaded")
print(orders[0])
def delivered_only(orders):
    return [o for o in orders if o["status"] == "delivered"]
delivered = delivered_only(orders)
print(len(delivered), "delivered orders")
def revenue_by_state(orders):
    totals = {}
    skipped = []
    for o in orders:
        try:
            price = float(o["price"])
        except ValueError:
            skipped.append(o["order_id"])
            continue
        state = o["state"]
        totals[state] = totals.get(state, 0) + price
    return totals, skipped
revenue = revenue_by_state(delivered)
revenue, skipped = revenue_by_state(delivered)
for state, total in revenue.items():
    print(f"{state}: {total:.2f}")
print("Skipped bad rows:", skipped)