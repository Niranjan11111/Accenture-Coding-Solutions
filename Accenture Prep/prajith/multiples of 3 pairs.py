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

