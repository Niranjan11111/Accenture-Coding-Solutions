def sumXor(arr):
    x, y = 0, 0
    for i in range(len(arr)):
        if i % 2 == 0:
            x ^= arr[i]
        else:
            y += arr[i]
    return y - x

arr = [10, 5, 6, 3, 7, 2]
print(sumXor(arr))