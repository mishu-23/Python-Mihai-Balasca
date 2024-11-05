#ex1

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())

#ex2

class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

queue = Queue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.pop())
print(queue.pop())

#ex3

class Matrix:
    def __init__(self, rows, cols, fill = 0):
        self.rows = rows
        self.cols = cols
        self.data = [[fill for i in range(cols)] for j in range(rows)]

    def get(self, row, col):
        return self.data[row][col]

    def set(self, row, col, value):
        self.data[row][col] = value

    def transpose(self):
        transp = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                transp.set(j, i, self.get(i, j))
        return transp

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("nr de col din A dif de nr de linii din B")

        res = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                res.set(i, j, sum(self.get(i, k) * other.get(k, j) for k in range(self.cols)))
        return res

    def transform(self, function):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = function(self.data[i][j])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

matrix = Matrix(3, 3)
matrix.set(0, 0, 0)
matrix.set(1, 0, 1)
matrix.set(2, 0, 2)
matrix.set(0,1, 3 )
matrix.set(1, 1, 4)
matrix.set(2, 1, 5)
matrix.set(0, 2, 6)
matrix.set(1, 2, 7)
matrix.set(2, 2, 8)

print(matrix)
transp = matrix.transpose()
print('')
print(transp)

matrix2 = matrix
print('')
print(matrix2)

mult = matrix.multiply(matrix2)
print('')
print(mult)

matrix.transform(lambda x: x * x)
print('')
print(matrix)