def favSongCount(string, l):
    aCount = 0
    for i in range(len(string)-l):
        subs = string[i:i+l]
        if subs.count('a') > aCount:
            aCount = subs.count('a')

    return aCount

print(favSongCount("behbjnjbhv", 3))