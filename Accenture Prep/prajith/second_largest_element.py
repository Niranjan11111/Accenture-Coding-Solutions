def sec(arr,n):
    if n < 2:
        return 0
    
    arr.sort()
    x = list(set(arr))[-2]
    count =0
    for i in arr:
        if i == x:
            count+=1
    return count
    
arr = [1,2,3,3,3,4,4,5,5,5,5]
n = len(arr)
sec(arr,n)
