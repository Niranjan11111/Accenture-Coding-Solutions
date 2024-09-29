N = 14
def isPrime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

if N == 0 or N == 1:
    print(0)
else:
    sum = 0
    for i in range(N+1):
        if isPrime(i):
            sum += i
print(sum)