# Maximum pair product 

# Noah is given an integer array A of length N. He must perform the following operations on the array :
# Select any integer pairs from the array with their sum equal to 18.
# From this select the pair with the maximum product such that the first element of the pair is greater than the second element of the pair.
# Your task is to help Noah find and return a pair in the form of an integer array which satisfies the conditions mentioned	
# Input Specification:

# input 1 : An integer N, representing length of array.
# Input 2 : An integer array A. 

# Output Specification:

# Return a pair in the form of an integer array which satisfies the conditions mentioned


def mpp(n, arr):
    max_pro = 0
    for i in range(n):
        a = arr[i]
        target = 18 - a
        if target in arr:
            pro = a * target
            if pro > max_pro:
                max_pro = pro
                pair = [a,target]
    return pair

arr = [11, 1, 2, 8, 10, 11, 15, 7]
n = len(arr)
print(mpp(n, arr)) 


arr = [20,16,2,1,5]
n = len(arr)
print(mpp(n, arr)) 
