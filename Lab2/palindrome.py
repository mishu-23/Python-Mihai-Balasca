def palindrome(num):
    num_str = str(num)
    return num_str[::-1] == num_str
num = int(input("Enter a number: "))
print(palindrome(num))