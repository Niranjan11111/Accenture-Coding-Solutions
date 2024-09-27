# Alice and Song
# Alice has a collection of songs represented as a string S where each character represents a song. A playlist is a substring of the given string with exactly K number of songs. She wants to create a playlist that contains maximum number of her favourite song which is 'a'. Your task is to find and return an integer value representing the maximum number of favourite songs that she can get in a single playlist. 

# Input Specification:
# input1: A string value S representing the collection of songs.
# input2: An integer value K representing the number of songs in the playlist.

# Output Specification:
# Return an integer value representing the maximum number of favourite songs that she can get in a single playlist.


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
