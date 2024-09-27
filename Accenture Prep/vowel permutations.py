# Vowel Permutation

# You are given a string S and your task is to find and return the count of permutations formed by fixing the positions of the vowels present in the string.

# Note: 
# Ensure the result is non negative.

# If there are no consonants then return 0.
# Input Specification:

# input1: A string S

# Output Specification:

# Return an integer value representing the count of permutations formed by fixing the positions of the vowels present in the string.

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
