# Prime Number Picnic

# You are planning a picnic for a group of friends who love math. To make it interesting, you decided to bring unique numbers of items, N. Your task is to find and return an integer value representing the sum of all the prime numbers till N. In case, the number of items is 0 or 1, return 0.

# Note:
# Prime numbers are natural numbers that are divisible by only 1 and the number itself.
# Input Specification:

# input1: An integer value N

# Output Specification:

# Return an integer value representing the sum of the prime numbers till N. In case, the number of items is not prime, return 0.
def primepic(n):
    def isprime(num):
        if num <2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
    ans = 0
    for i in range(2,n+1):
        if isprime(i):
            ans+=i
    return ans if ans>0 else 0
n = int(input())
primepic(n)
