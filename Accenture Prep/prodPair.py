def prodPairs(arr):
    arr = list(set(arr))  # Remove duplicates
    pairs = set()  # Use a set to store pairs
    pairCount = 0
    l = len(arr)
    if l < 2:
        return 0
    
    for i in range(l):
        for j in range(i + 1, l):
            if (arr[i] * arr[j]) % 3 == 0 and (arr[i], arr[j]) not in pairs and (arr[j], arr[i]) not in pairs:
                pairCount += 1
                pairs.add((arr[i], arr[j]))  # Add pair to the set

    return pairCount

arr = [3, 6, 5, 4]
print(prodPairs(arr))

