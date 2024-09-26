def secLarRepNum(arr):
    repNums = []
    for n in arr:
        if arr.count(n) > 1 and n not in repNums:
            repNums.append(n)
    repNums.sort()
    return repNums[-2]

arr = [1, 2, 2, 4, 4, 6, 7, 7]
print(secLarRepNum(arr))