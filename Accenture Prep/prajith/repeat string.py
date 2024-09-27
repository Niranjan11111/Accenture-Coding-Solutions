Repeat String

# You are given an integer N and a string S. Your task is to find and return a new string which consists of the original string repeated N times.

# Input Specification:

# input1: An integer value N 
# input2: A string value S

# Output Specification:

# Return a new string which consists of the original string repeated N times.


def repeat(n,str):
    ans=""
    for i in range(n):
        ans+=str
    return ans
