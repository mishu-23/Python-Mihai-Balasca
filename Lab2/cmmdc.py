def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def gcd_multiple(numbers):
    res = numbers[0]
    for num in numbers[1:]:
        res = gcd(res, num)
    return res

count = input("Zi cate numere vrei sa scrii:")
numbers = []
for i in range(int(count)):
    num = int(input(f"Numarul {i + 1}: "))
    numbers.append(num)
print(gcd_multiple(numbers))