from operator import index


def occurrences(substring, string):
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        count += 1
        index += len(substring)
    return count

string = input("Enter a string: ")
substring = input("Enter a substring: ")
print(occurrences(substring, string))