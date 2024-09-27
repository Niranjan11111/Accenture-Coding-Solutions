# Halloween Candies

# Bob goes to the supermarket to shop for candies represented by array A for a Halloween party. 
# His mother gave him some money M. Due to the festive season, there are several offers in the supermarket. 
# One such offer says if the total Bob is spending on candy is a multiple of 5, he can buy it without spending any money; otherwise, 
# he will just save it for future use. If the price of one candy is equal to Ai, which is the price of a particular candy, Bob can shop as long as he has money. 
# Your task is to find and return the maximum number of candies Bob can buy.

# Note: Assume 1-based indexing.

# Input Specification:

# input1: An integer value N, representing the number of candies.
# input2: An integer array A, representing the price of each candy.
# input3: An integer value M, representing the amount of money.
# Output Specification: Return the number of candies Bob can buy.
def halloween(n, a, i):
    y=[]
    for x in a:
        if x <=i:
            y.append(x)
    
    if len(y) == 0:
        return n
    
    y.sort()
    d = n - len(y)
    index = 0
    while index < len(y):
        m = y[index]
        if m == 0:
            break
        d += 1
        index += 1
    
    return d
result = halloween(3, [5, 15, 105], 16)
print(result)
