# Financial Dataset

# You are working on a financial analyzing tool which represents the daily stock prices of a company over a time. 
# Each element in an integer array A of size N represents the closing price of the stock for a particular day. Your task is to find and retum an integer value representing the total number of days where the stock price decreased indicating negative growth.
# Input Specification:

# input1: An integer array A containing the closing price of the stockinput2: An integer value N representing the size of array

# Output Specification:

# Return an integer value representing the total number of days where the stock price decreased, indicating negative growth.

def finance(arr):
  count=0
  for i in arr:
    if i < 0:
      count+=1
    return count
    
