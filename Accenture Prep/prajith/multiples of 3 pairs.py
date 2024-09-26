# Product Pair

# You are given an integer array A of length N and your task is to find and return an integer value representing the count of unique pairs whose products are multiples of 3. 

# Note:

# A unique pair means that the elements must be the same regardless of their order. For instance {1, 3} and {3, 1} are considered as the same pair.

# Input Specification:

# input1: An integer value N, representing the size of the array
# input2: An integer array A

# Output Specification:

# Return an integer value representing the count of unique pairs whose products are multiples of 3.

def count_pairs_multiple_of_3(A):
    seen_pairs = set() 
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] % 3 == 0 or A[j] % 3 == 0:
                pair = tuple(sorted([A[i], A[j]]))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
    return len(seen_pairs)


A = [3,6,5,4]
print(count_pairs_multiple_of_3(A))

