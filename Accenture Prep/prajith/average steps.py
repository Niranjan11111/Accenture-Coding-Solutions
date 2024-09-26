# Goal Tracker

# You are developing a feature for daily steps. Users input a health and fitness app that helps users the total number of daily steps S, the number of steps they 20 track their have completed D, and the number of days they have been tracking their steps N Your task is to find and return an integer value representing the average number of steps the user needs to take per day to reach their target.Note: 
# Round off the output to its nearest value

# Input Specification:

# input1: An integer value S representing the total number of daily steps.input2: An integer value D representing the number of steps user has completed.input3: An integer value N representing the number of days the user has been tracking their steps.

# Output Specification:

# Return an integer value representing the average number of steps the user needs to take per day to reach their target

def steps(s,d,n):
    return round((s-d)/n)
print(steps(348,327,5))
print(steps(6000,2455,7))
