n = 3 # 4 # 8 # 10 # 45
count = 0
for k in range(1, n+1):
    s = bin(k)[2:]
    print(s)
    for i in s:
        if i == '0':
            s = s.replace('0', '1')
        elif i == '1':
            s = s.replace('1', '2')
    summ = 0
    for i in s:
        summ += int(i)
    if summ % 2 != 0:
        count += 1
print(count)
