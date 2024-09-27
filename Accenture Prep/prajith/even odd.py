# Even Odd

# Jack has an array A of length N. He wants to label whether the number in the array is even or odd. Your task is to help him find and return a string with labels even or odd in sequence according to which the numbers appear in the array.

# Input Specification:

# input1: An integer array A, representing the array of numbers
# input2: An integer N, representing the length of the array
# Output Specification: Return a string with labels even or odd in sequence
# according to which the numbers appear in the array.

def evenodd(arr):
  ans=""
  for i in arr:
    if i%2==0:
      ans+="even"
    else:
      ans+="odd"
    return ans
