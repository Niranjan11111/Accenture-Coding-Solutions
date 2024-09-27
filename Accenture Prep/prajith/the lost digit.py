# The lost Digit

# You are working on a number sequence puzzle. You have an array A, that is supposed to contain all the numbers from 1 to N, but you realize one number is missing. The array might have been shuffled, so the numbers are ot in order. Your task is to find and return an integer value representing the missing number from the sequence.

# Input Specification:
# Input1: An integer array Ainput2: An integer value N representing the length of the sequence

# Output Specification:
# Return an integer value representing the missing number from the sequence.

def lost(arr,n):
  return (max(arr)*(max(arr)+1))//2 - sum(arr)
arr=[1,2,4,5]
n=len(arr) 
lost(arr,n)
