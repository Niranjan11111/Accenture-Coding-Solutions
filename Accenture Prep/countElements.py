def countElements(dict):
    maxKeys = 0
    maxValues = max(dict.values())
    print(maxValues)
    for key, values in dict.items():
        if values == maxValues:
            maxKeys = key
            break
    print(maxKeys)

dict = {
    'apple': 10,
    'banana': 15,
    'orange': 8,
    'grape': 15
}
countElements(dict)