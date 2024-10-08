def count_vowels(string):
    vow = "aeiouAEIOU"
    count = 0
    for i in string:
        if i in vow:
            count += 1
    return count

word = input("Enter a string: ")
print(count_vowels(word))