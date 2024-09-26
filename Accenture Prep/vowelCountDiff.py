def vowelCountDiff(string):
    count = 0
    for s in string:
        if s in "aeiouAEIOU":
            count += 1
    return abs(count - len(string))

print(vowelCountDiff("niranjan"))

