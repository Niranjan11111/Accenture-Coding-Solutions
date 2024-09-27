def initials(string):
    print(f"{string[0].upper()}.{string[-1].upper()}")
    num = 3.2635738789
    print("{:.3f}".format(num))
    return string[0].upper() + '.' + string[-1].upper()


print(initials("Patrick cummins"))