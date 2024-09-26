def lowcount(str):
    c=0
    for i in str:
        if i.islower():
            c+=1
    return c
str = "abcedfGHIJ"
lowcount(str)

# def lowcount(s):
#     c = 0
#     for i in s:
#         if ord('a') <= ord(i) <= ord('z'):
#             c += 1
#     return c

# print(lowcount("abcdefGHIJ"))
