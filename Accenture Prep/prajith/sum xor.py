# Sum XOR

# You are given an array A of length N. Your task is to find and return an integer value representing the difference between the sum of elements at odd index and XOR of elements at even index.

# Input Specification:

# input1: An integer N, representing the length of array
# input2: An integer array A
# Output Specification: Return an integer value representing the difference between the sum of elements at odd index and XOR of elements at even index.

def sumxor(arr):
    s = 0
    x = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            x = x ^ arr[i]
        else:
            s += arr[i]
    return s - x

result = sumxor([10, 5, 6, 3, 7, 2])
print(result)
