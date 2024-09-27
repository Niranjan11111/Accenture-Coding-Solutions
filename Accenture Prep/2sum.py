def twoSum(arr, target):
    maxProd = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                prod = arr[i] * arr[j]
                if prod > maxProd:
                    maxProd = prod
                    result = [arr[i], arr[j]]
    return result

arr = [13, 2, 10, 8, 5, 4]
target = 15
print(twoSum(arr, target))

