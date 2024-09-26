def A(arr):
    ans=""
    for i in arr:
        if i[0]=="A":
            ans+=i
    return ans

arr = ["Apple","Orange","Apricot"]
A(arr)
