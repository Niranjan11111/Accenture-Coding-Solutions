# Second Occurrence 

# Charles is given an array A. He wants to find the count of occurences of second largest element in the array. Your task is to help him and return an integer value representing the count of occurrence of the second largest element in an array. 

# note:
# If the array contains the same elements, then return 0
# The array has only consecutive elements	
# Input Specification:

# input 1 : An integer N, representing length of array.
# Input 2 : An integer array A. 

# Output Specification:

# Return an integer value representing the count of occurrence of the second largest element in an array

def sec(arr,n):
    if n < 2:
        return 0
    
    arr.sort()
    x = list(set(arr))[-2]
    count =0
    for i in arr:
        if i == x:
            count+=1
    return count
    
arr = [1,2,3,3,3,4,4,5,5,5,5]
n = len(arr)
sec(arr,n)
