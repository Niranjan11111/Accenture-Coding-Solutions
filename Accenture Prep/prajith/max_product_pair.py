def mpp(n, arr):
    max_pro = 0
    for i in range(n):
        a = arr[i]
        target = 18 - a
        if target in arr:
            pro = a * target
            if pro > max_pro:
                max_pro = pro
                pair = [a,target]
    return pair

arr = [11, 1, 2, 8, 10, 11, 15, 7]
n = len(arr)
print(mpp(n, arr)) 


arr = [20,16,2,1,5]
n = len(arr)
print(mpp(n, arr)) 
