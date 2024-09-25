def even_odd(arr, n):
    result = []
    for i in range(min(n, len(arr))):
        if arr[i] % 2 == 0:
            result.append('even')
        else:
            result.append('odd')
    return ''.join(result)

input1 = (1, 2, 5)
input2 = 2

output = even_odd(input1, input2)
print(output)  