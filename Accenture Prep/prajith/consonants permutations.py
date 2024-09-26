def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
def perm(arr):
    vow = "aeiou"
    res=[]
    for str in arr:
        count=0
        for i in str.lower():
            if i not in vow:
                count+=1
        res.append(fact(len(str))//fact(len(str)-count))
    return res
perm(["hello","abc"])
