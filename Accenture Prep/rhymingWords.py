# def rhymingWords(words, target):
#     max_word = ""
#     max_value = 0

#     for word in words:
#         if word == target:
#             continue

#         rev_word = list(reversed(word))
#         rev_target = list(reversed(target))

#         min_length = min(len(rev_word), len(rev_target))
#         rhyme_score = 0

#         for i in range(min_length):
#             if rev_word[i] == rev_target[i]:
#                 rhyme_score += 1
#             else:
#                 break

#         if rhyme_score > max_value:
#             max_value = rhyme_score
#             max_word = word

#     return f"{max_word} {max_value}"

words = ["thunder", "under", "hnder"]
target = "thunder"
# print(rhymingWords(words, target))
target = list(target[::-1])
result = ""
maxScore = 0

for word in words:
    word = list(word[::-1])
    score = 0
    if word == target:
        continue

    for i in range(min(len(word), len(target))):
        if word[i] == target[i]:
            score += 1
        else:
            break
        
    if score > maxScore:
        maxScore = score
        result = word
print(''.join(result)[::-1])
