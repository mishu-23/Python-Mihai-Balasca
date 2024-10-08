def bits(num):
    count = 0
    while num > 0:
        if num % 2 == 1:
            count += 1
        num //= 2
    return count

number = int(input("Enter a number: "))
print(bits(number))