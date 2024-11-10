#1

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter()/2
        return (s*(s - self.a)*(s - self.b)*(s - self.c)) ** 0.5

print("-> Circle")
circle = Circle(5)
print("perimetru cerc:", circle.perimeter())
print("arie cerc:", circle.area())

print("-> Rectangle")
rectangle = Rectangle(5, 5)
print("perimetru dreptunghi", rectangle.perimeter())
print("arie dreptunghi", rectangle.area())

print("-> Triangle")
triangle = Triangle(5, 5, 5)
print("perimetru triunghi", triangle.perimeter())
print("arie triunghi", triangle.area())

#2
print("")

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"ai depus {amount} lei")
        return self.balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"mai ai {self.balance} lei")
        else:
            print(f"n-ai bani nici sa treci strada")
        return self.balance
    def show_balance(self):
        print(f"mai ai {self.balance} lei")

class SavingsAccount(Account):
   def bonus(self, bonus):
       self.balance += bonus
       print(f"Ai primit un bonus de {bonus} lei. Acum ai {self.balance} lei")
       return self.balance

class CheckingAccount(Account):
    def write_check(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"ai scos un check de {amount} lei. mai ai {self.balance} lei")
        else:
            print("n-ai tu bani de check. du-te la munca")
        return self.balance
    def use_coupon(self, amount):
        self.balance += amount
        print(f"a venit pensia in valoare de {amount} lei")
        return self.balance

print("-> Account")
account = Account(50)
account.deposit(100)
account.withdraw(140)
account.show_balance()

print("-> SavingAccount")
savings = SavingsAccount(50)
savings.deposit(100)
savings.bonus(15)
savings.show_balance()

print("-> CheckingAccount")
checking = CheckingAccount(50)
checking.write_check(100)
checking.write_check(40)
checking.use_coupon(100)
checking.show_balance()

#3
print("")
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.make} {self.model} {self.year}"

class Car(Vehicle):
    def mileage(self, miles, gallons):
        return miles/gallons

class Motorbile(Vehicle):
    def mileage(self, miles, gallons):
        return miles/gallons

class Truck(Vehicle):
    def mileage(self, miles, gallons):
        return miles/gallons

print("-> Truck")
truck = Truck("Toyota", "nuj, ceva de la Toyota", 2024)
print("info: ", truck.get_info())
print("mileage", truck.mileage(300, 15))

#4
print("")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def  get_info(self):
        return f"{self.name} {self.salary}"

class Manager(Employee):
    def manage(self):
        return "Manageriaza echipa"

class Engineer(Employee):
    def manage(self):
        return "Developing stuff"

class Salesperson(Employee):
    def sell(self):
        return "Selling stuff"

print("-> Manager")
manager = Manager("Alice", 5000)
print("info", manager.get_info())
print("ce face?", manager.manage())

#5
print("")

class Animal:
    def __init__(self, name):
        self.name = name
    def can_swim(self):
        pass
    def can_fly(self):
        pass
    def can_walk(self):
        pass

class Mammal(Animal):
    can_swim = True
    can_fly = False
    can_walk = True

class Bird(Animal):
    can_swim = False
    can_fly = True
    can_walk = True

class Fish(Animal):
    can_swim = True
    can_fly = False
    can_walk = False

print("-> Mammal")
mammal = Mammal("unicorn")
print(f"un {mammal.name} poate sa: "
      f"inoate = {mammal.can_swim}"
      f" zboare = {mammal.can_fly}"
      f" mearga = {mammal.can_walk}"
      )

#6
print("")

class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.checkedout = False

    def checkout(self):
        if not self.checkedout:
            self.checkedout = True
            return f"{self.title} {self.year} checked out"
        return f"{self.title} {self.year} already checked out"

    def return_item(self):
        if self.checkedout:
            self.checkedout = False
            return f"{self.title} {self.year} returnata"
        return f"{self.title} {self.year} not checked out"

    def get_info(self):
        return f"{self.title} {self.year} "

class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def get_info(self):
        return super().get_info() + f"{self.author}"

class DVD(LibraryItem):
    def __init__(self, title, year, director):
        super().__init__(title, year)
        self.director = director

    def get_info(self):
        return super().get_info() + f" {self.director}"

class Magazine(LibraryItem):
    def __init__(self, title, year):
        super().__init__(title, year)

    def get_info(self):
        return super().get_info()

print("-> Book")
book = Book("Amintiri din copilarie", "1837", "Ion Creanga")
print("Book Info ->", book.get_info())
print("Check Out Book -> ", book.checkout())
print("Check Out Book -> ", book.checkout())
print("Book return ->", book.return_item())
print("Book return ->", book.return_item())

