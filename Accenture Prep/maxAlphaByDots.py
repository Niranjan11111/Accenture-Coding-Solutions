def maxAlphaByDots(string):
    segments = string.split('.')
    for segment in segments:
        themaxChars = 0
        maxChar = 0
        for i in range(len(segment)):
            if segment[i].isalpha():
                maxChar += 1
        if maxChar > themaxChars:
            themaxChars = maxChar
    return themaxChars

print(maxAlphaByDots("abc.ab.cf"))