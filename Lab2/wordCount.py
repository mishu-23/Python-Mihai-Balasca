def wordCount(word):
    words = word.split(" ")
    return len(words);

text = input("Enter a sentence: ")
print(wordCount(text))