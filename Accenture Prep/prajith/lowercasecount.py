def lowcount(str):
    c=0
    for i in str:
        if i.islower():
            c+=1
    return c
str = "abcedfGHIJ"
lowcount(str)

# def lowcount(str):
#   c=0
#   for i in str:
#     if ord(i) >97 or ord(i) < 122:
#       c+=1
#   return c
