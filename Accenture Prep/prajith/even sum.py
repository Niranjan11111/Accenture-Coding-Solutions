# Even Sum

# You are organizing a charity run where participants contribute a 34460to find and return an integer value representing the total amount of money raised if the race is N km long.Input Specification:

# input1: An integer value N Output Specification:

# Return the sum of all even numbered kilometers till N they complete

def evensum(n):
    ans=0
    for i in range(1,n+1):
        if i%2==0:
            ans+=i
    return ans
n = int(input())
evensum(n)
