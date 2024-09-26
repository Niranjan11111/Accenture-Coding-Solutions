# Find Letters

# Your friend gives you a string S which contains the name of a person and asks you to find the first and last letter of their name. Your task is to find and return a string representing the first and the last letter.
# Note:
# The output should be two capital letters with a dot separating them.
# The output is case sensitive.
# Input Specification:

# Input: A string S representing the name 

# Output Specification:

# Return a string representing the first and the last letter.

def findletters(name):
  return name[0].upper() +"."+name[-1].upper()
 
name = input()
print(findletters(name))
