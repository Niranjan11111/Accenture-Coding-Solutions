def find(arr,t):
    res = []
    for i in range(len(arr)):
        if arr[i] == t:
            res.append(i)
    return [-1,-1] if len(res) == 0 else res

arr = [5,7,7,8,8,10]
t = 8
print(find(arr, t))

arr = [5,7,8,8,10]
t = 6
print(find(arr, t))
