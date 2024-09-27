# Character Count

# You are given a string S of length N. Your friend wants to know the number of times his favorite letter C occurs in the string. Your task is to help your friend find and return an integer value representing the number of times a character occurs in a particular string.

# Note: 
# All the characters in the strings are in lowercase.
# Input Specification:

# input1: A string S
# input2: An integer N, representing the length of string
# input3: A character C

# Output Specification:

# Return an integer value representing the number of times a character occurs in a particular string
def charcount(str,n,c):
  return str.count(c)
#or
def charcount(str,n,c):
  count = 0
  for i in str:
    if i == c:
      count+=1
  return count
