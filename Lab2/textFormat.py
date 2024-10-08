def converter(string):
    res = string[0].lower()
    for char in string[1:]:
        if char.isupper():
            res += '_' + char.lower()
        else:
            res += char
    return res

string = input("Enter an UpperCamelCase string: ")
print(converter(string))