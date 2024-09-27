def avgSteps(t, d, n):
    a = t - d
    ans = a // n
    return ans

print(round(avgSteps(6000, 2455, 7)))