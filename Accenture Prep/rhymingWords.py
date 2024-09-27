def rhymingWords(words, target):
    wordDict = {}
    for word in words:
        if word == target:
            continue 
        wordDict[word] = 0  

        rev_word = list(reversed(word))
        rev_target = list(reversed(target))
        
        min_length = min(len(rev_word), len(rev_target))
        
        for i in range(min_length):
            if rev_word[i] == rev_target[i]:
                wordDict[word] += 1
            else:
                break

        max_key = max(wordDict, key=wordDict.get)
        max_value = wordDict[max_key]

    return (max_key, max_value)


words = ["thunder", "blender", "under", "puzzle"]
target = "thunder"
print(rhymingWords(words, target))
