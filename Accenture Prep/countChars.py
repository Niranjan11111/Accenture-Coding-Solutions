def countChars(string, n, target):
    count = 0
    for i in range(n):
        if string[i] == target:
            count += 1
    return count
print(countChars("helloworld", 10, 'l'))