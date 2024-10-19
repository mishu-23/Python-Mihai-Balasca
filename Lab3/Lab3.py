#1
def fib(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

#2
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
        return True
def find_prime(lst):
    return [num for num in lst if isPrime(num)]

#3
def list_op(a: [], b: []):
    intersec = []
    intersec = set(a) & set(b)
    # for i in a:
    #     if i in b:
    #         intersec.append(i)

    union = []
    union = set(a) | set(b)
    # for i in a:
    #     union.append(i)
    # for i in b:
    #     if i not in union:
    #         union.append(i)

    a_min_b = []
    a_min_b = set(a) - set(b)
    # for i in a:
    #     if i not in b:
    #         a_min_b.append(i)

    b_min_a = []
    b_min_a = set(b) - set(a)
    # for i in b:
    #     if i not in a:
    #         b_min_a.append(i)
    return (intersec, union, a_min_b, b_min_a)

#4
def compose(notes, moves, start_pos):
    song = []
    pos = start_pos
    for move in moves:
        pos = (pos + move) % len(notes)
        song.append(notes[pos])
    return song

#5
def zero_mat(mat):
    n = len(mat)
    for i in range(1, n):
        for j in range(i):
            mat[i][j] = 0
    return mat

#6
def appearing_x_times(x, *lists):
    frecv = {}

    for list in lists:
        for item in list:
            if item in frecv:
                frecv[item] += 1
            else:
                frecv[item] = 1
    result = [item for item, count in frecv.items() if count == x]
    return result

#7

def palindrome(num):
    num_str = str(num)
    return num_str[::-1] == num_str

def palind_list(list):
    # count = 0
    # greatest_palindrome = 0
    # for item in list:
    #     if palindrome(item):
    #         count += 1
    #         if item > greatest_palindrome:
    #             greatest_palindrome = item

    palind = [item for item in list if palindrome(item)]
    count = len(palind)
    greatest_palindrome = max(palind) if palind else None
    return (count, greatest_palindrome)

#8
def ascii_function(x = 1, list = [], flag = True):
    result = []
    for word in list:
        if flag:
            chars = [char for char in word if ord(char) % x == 0]
        else:
            chars = [char for char in word if ord(char) % x != 0]
        result.append(chars)
    return result

#9
def spectators(field):
    result = []
    for column in range(len(field[0])):
        max_height = -1
        for row in range(len(field)):
            current_height = field[row][column]
            if current_height <= max_height:
                result.append((row, column))
            else:
                max_height = current_height
    return result

#10
def transformed_lists(*lists):
    max_length = max(len(list) for list in lists)
    result = [tuple(list[i] if i < len(list) else None for list in lists) for i in range(max_length)]
    return result

#11
def order_by_third(list):
    def key_fun(tuple):
        return tuple[1][2] if len(tuple[1]) > 2 else ''
    return sorted(list, key=key_fun)

#12
def rhyme(words):
    rhymes = {}
    for word in words:
        word_rhyme = word[-2:] if len(word) > 2 else word
        if word_rhyme not in rhymes:
            rhymes[word_rhyme] = []
        rhymes[word_rhyme].append(word)
    return rhymes.values()
#cum afisez fara dict_values? sa castez la list nu memrge idk de ce

#-------------------------------------------------------

print("ex 1:")
print("Fibonacci de 5", fib(5))

print("ex 2:")
list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 4, 6, 8]
print("Prime: ", find_prime(list))

print("ex 3:")
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print("Operatii cu multimi: ", list_op(a, b))

print("ex 4:")
notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_pos = 2
print("Cantec: ", compose(notes, moves, start_pos))

print("ex 5:")
mat = [[1,2,3],[4,5,6],[7,8,9]]
print("Zero Below Diagonal: ", zero_mat(mat))

print("ex 6:")
lists = [[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]]
x = 2
print(appearing_x_times(x, *lists))

print("ex 7:")
numbers = [121, 343, 456, 787, 12321, 10, 99, 10001]
print(palind_list(numbers))

print("ex 8:")
x = 2
list = ["test", "hello", "lab002"]
flag = False
print(ascii_function(x, list, flag))

print("ex: 9")
field = \
 [[1, 2, 3, 2, 1, 1],
 [2, 4, 4, 3, 7, 2],
 [5, 5, 2, 5, 6, 4],
 [6, 6, 7, 6, 7, 5]]
print(spectators(field))

print("ex 10:")
lists = [[1, 2, 3], [5, 6, 7], ["a", "b"]]
print(transformed_lists(*lists))

print("ex 11:")
list = [('abc', 'bcd'), ('abc', 'zza')]
print(order_by_third(list))

print("ex 12:")
words = ['ana', 'banana', 'carte', 'arme', 'parte']
print(rhyme(words))