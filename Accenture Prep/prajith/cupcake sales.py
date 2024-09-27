# Cupcake Sales

# You are given an array A of size N, where each element represents the number of cupcakes sold in a single transaction. Your task is to find and return an integer value representing the sum of the cupcakes from the transactions where 5 or more cupcakes were sold. Return 0 if there is no transaction with more than 5 cupcakes sold.

# Input Specification:

# input1: An integer value N representing the number of transactionsinput2: An integer array A representing the number of cupcakes, sold in each transaction.
# Output Specification:

# Return an integer value representing the sum of the cupcakes from the transactions where 5 or more cupcakes were sold Return 0 if there is no transaction with more than 5 cupcakes sold.

def cupcake(n,arr):
  ans=0
  for i in arr:
    if i>=5:
      ans+=i
  return ans
