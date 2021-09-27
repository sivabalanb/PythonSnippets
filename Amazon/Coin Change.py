coins = [1, 2, 5]
amount = 11


def coinchange(coins, amount):
    rs = [amount+1] * (amount+1)
    print("rs", rs)
    rs[0] = 0
    for i in range(1, amount+1):
        for c in coins:
            if i >= c:
                rs[i] = min(rs[i], rs[i-c] + 1)
                print(f"rs{i} {rs[i]} and  amount {amount} coins {c}")
            else:
                print(f"Else i{i} and c{c}")
        print("rs", rs)

    if rs[amount] == amount+1:
        return -1
    return rs[amount]


print(coinchange(coins, amount))
