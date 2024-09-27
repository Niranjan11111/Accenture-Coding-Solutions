def maxMatch(strArr, string):
    maxLen = 0
    for s in strArr:
        if s in string:
            if len(s) > maxLen:
                maxLen = len(s)
                maxS = s
    return maxLen, maxS

strArr = ["hello", " world", "he", "lll"]
string = "hello, world"
print(maxMatch(strArr, string))
        

