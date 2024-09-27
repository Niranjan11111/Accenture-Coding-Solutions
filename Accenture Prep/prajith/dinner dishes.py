# Dinner Dishes

# You are planning a dinner menu for an event, and you have a list of 2004 N dishes stored in array A, each with a certain cost associated with it. 
# You must select two such dishes, such that the sum of their costs is maximum among all available pairs. Your task is to find and return an 
# integer value representing the sum of such available pair. Return 0 in case of no such pair available.
# Input Specification:

# input1: An integer array A representing the cost of dishesinput2: An integer value N representing the number of dishes available.

# Output Specification:

# Return an integer value representing sum of such pair available. In case, there are no such pair present, return 0.
def dinner(arr):
    if len(arr)<2:
        return 0
    else:
        return sum(arr[-2:])
