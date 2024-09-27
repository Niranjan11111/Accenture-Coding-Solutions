# Product of an Array

# You are given an integer array A of size N. Your task is to find and return an integer value representing the product of all the elements in the array.

# Input Specification:

# input1: An integer array A
# input2: An integer value N representing the size of the array

# Output Specification:

# Return an integer value representing the product of all the elements in the array.

def product(arr):
  pro = 1
  for i in arr:
    pro*=i
  return pro
