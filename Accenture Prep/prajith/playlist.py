def playlist(s, k):
    substrings = []
    n = len(s)
    sub=[]
    for i in range(n - k + 1):
        substrings.append(s[i:i + k])
    for i in substrings:
        sub.append(i.count("a"))
    return max(sub)


S = "abaca"
K = 3
print(playlist(S, K))
S ="bcdefgfedcb"
K=5
print(playlist(S,K))
