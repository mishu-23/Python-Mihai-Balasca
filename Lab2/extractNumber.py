def extractNumber(text):
    number = ""
    for i in text:
        if i.isdigit():
            number += i
        elif number:
            break
    return number

string = input("Enter a string: ")
number = extractNumber(string)
if number:
    print(number)
else:
    print(0)