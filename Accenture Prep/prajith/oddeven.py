def oddeven(l):
    ans=''
    for i in l:
        if i%2==0:
            ans+= 'Even'
        else: 
            ans+= 'Odd'
    return ans
l = [2,2,3,4,5,6]
oddeven(l)
