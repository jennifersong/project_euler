def make_change(amount, coins):
    if amount == 0:
        return 1
    elif len(coins) == 0:
        return 0
    else:
        ways = 0
        coin = coins[0]
        num_coins = 0
        while ((amount - num_coins * coin) >= 0):
            ways += make_change(amount - num_coins * coin, coins[1:])
            num_coins += 1
        return ways
    
print make_change(200, [1, 2, 5, 10, 20, 50, 100, 200])