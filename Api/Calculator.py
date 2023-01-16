
"""function to calculate stake2 given odds1, odds2, stake1
"""
def calculate_profit(odds1, odds2, stake1):
    sign = odds1[0]
    odds1 = float(odds1[1:])
    stake1 = float(stake1)
    if sign=="-":
        payout = stake1 + ((stake1 * 100) / odds1)
    else:
        payout = stake1 + (stake1 * (odds1 / 100))
    stake2 = None
    # need to find stake, given payout and odds
    sign2 = odds2[0]
    odds2 = float(odds2[1:])
    if sign2 == "-":
        stake2 = (odds2 * payout) / (odds2 + 100)
    else:
        stake2 = (100 * payout) / (odds2 + 100)
    total = stake1 + stake2
    profit = payout - total
    return stake2, payout, profit


"""function to calculate amount to put on each side of the arb
param odds1: first option odds
param odds2: second option odds
param total_amt: total amount willing to spend
returns list: [amount to place on bet1, amount to place on bet2, profit]
"""
def get_all(odds1, odds2, total_amt):
    total_amt = int(total_amt)
    maximum = total_amt
    res = []
    while total_amt > 0:
        stake1 = total_amt
        stake2, payout, profit = calculate_profit(odds1, odds2, stake1)
        if stake1 + stake2 < maximum:
            res = [total_amt, stake2, profit]
            return res
        total_amt -= 1


r = get_all("-110", "+180", "500")
print(r)

