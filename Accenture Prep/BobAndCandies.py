candies = sorted([5, 15, 86, 1, 1, 1, 80])
print(candies)
amount = 86
total = 0
for c in candies:
    if c % 5 == 0:
        total += 1
    else:
        if amount >= c:
            total += 1
            amount -= c
print(total, amount)
