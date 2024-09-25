def factNoVowel(string):
    vowels = "AEIOUaeiou"

    for s in string:
        if s in vowels:
            string = string.replace(s, '')

    if len(string) % 2 != 0:
        string = string.replace(string[-1], '')

    def factorial(n):
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact
    
    return factorial(len(string))

print(factNoVowel("AABBbyteC"))