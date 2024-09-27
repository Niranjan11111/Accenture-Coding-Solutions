# def SWG(string):
#     l = len(string)
#     string = list(string)
#     aCount, bCount = 0, 0
#     i = 0
#     while i < l-2:
#         if string[i] == 's':
#             if string[i+5] == 'w':
#                 aCount += 1
#                 i += 10
#             elif string[i+5] == 'g':
#                 bCount += 1
#                 i += 8
#         if string[i] == 'w':
#             if string[i+5] == 'g':
#                 aCount += 1
#                 i += 8
#             elif string[i+5] == 's':
#                 bCount += 1
#                 i += 10
#         if string[i] == 'g':
#             if string[i+5] == 's':
#                 aCount += 1
#                 i += 8
#             elif string[i+5] == 'w':
#                 bCount += 1
#                 i += 8
#         return [aCount, bCount]
    
# s = "snakewaterwatersnakegunwaterwatergun"
# print(SWG(s))
        

def SWG(string):
    l = len(string)
    aCount, bCount = 0, 0
    i = 0
    
    while i < l - 2:
        if string[i:i+5] == 'snake':
            if string[i+5:i+10] == 'water':
                aCount += 1
                i += 10
            elif string[i+5:i+8] == 'gun':
                bCount += 1
                i += 8
        elif string[i:i+5] == 'water':
            if string[i+5:i+8] == 'gun':
                aCount += 1
                i += 8
            elif string[i+5:i+10] == 'snake':
                bCount += 1
                i += 10
        elif string[i:i+3] == 'gun':
            if string[i+3:i+8] == 'snake':
                aCount += 1
                i += 8
            elif string[i+3:i+8] == 'water':
                bCount += 1
                i += 8
        else:
            i += 1  # Move forward if no match found

    return [aCount, bCount]

# Example usage:
s = "snakewaterwatersnakegunsnakesnakegun"
print(SWG(s))
