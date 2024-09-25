def diffBS(str1, str2):
    def countSpaces(string):
        count = 0
        for s in string:
            if s == '_':
                count += 1
        return count
    return abs(countSpaces(str1) - countSpaces(str2))
str1 = "He_ll_o_w_r_ld"
str2 = "Hello_World"
print(diffBS(str1, str2))