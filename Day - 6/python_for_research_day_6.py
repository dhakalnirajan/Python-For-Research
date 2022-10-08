# -*- coding: utf-8 -*-
"""Python For Research - Day 6.ipynb

# Day 6
"""

# Function
def function_name(arguments):
    return expression

"""# Default Argument vs non-default Argument"""

def greet(name, msg):
    print(f"Hello, {name} {msg}")

greet("ram", "GM")

greet("shyam", "Good Morning")

greet("Hari", "Good Evening")

"""# Multiple return value"""

def add(num1, num2):
    total = 0
    total = num1 + num2
    return num1, num2, total

type(add(3, 4))

num1, num2, total = add(3, 4)

total

"""# WAP to find the factorial of given numbers.

0! = 1

1! = 1

2! = 2 * 1! = 2 * 1

3! = 3 * 2! = 3 * 2 * 1

4! = 4 * 3! = 4 * 3 * 2 * 1

5! = 5 * 4! = 5 * 4 * 3 * 2 * 1

"""

def find_factorial(num):
    if num == 0:
        return 1

    fact = 1

    for i in range(1, num + 1):
        fact = fact * i
    return fact

find_factorial(5)

"""# Recursion"""

def test():
    # body of function
    test()

test()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

factorial(5)

"""# Python Class OOP (object Oriented Programming)"""

class person:    # class is a blueprint of creating object
    pass         # pass is a placeholder.

obj = person()

type(obj)

# if __name == "__main__"

obj2 = person()

class mammal():
    has_hair = True        # class attribute

cow = mammal()

cow.has_hair

human = mammal()
human.has_hair

class mammal():
    has_hair = True                    # class attribute
    def __init__(self, no_of_legs):    # initialize object attribute
        print(type(self))              # remove print on this line to not see class in the output in the cells below
        self.no_of_legs = no_of_legs   # object attribute

cow = mammal()   # asks how many legs does a cow have. To fix the issue, check the cell below.

cow = mammal(4)
print(cow.has_hair)
print(cow.no_of_legs)

human = mammal(2)
print(human.has_hair)
print(human.no_of_legs)

class mammal():
    has_hair = True                    # class attribute
    def __init__(self, no_of_legs, sound):    # initialize object attribute
        print(type(self))              # remove print on this line to not see class in the output in the cells below
        self.no_of_legs = no_of_legs   # object attribute
        self.sound = sound
    
    def display_legs(self):
        print("The number of legs is {}".format(self.no_of_legs))

cow = mammal(4, 'Moooooowww')

cow.display_legs()

cow.sound

human = mammal(2, "giggles")
human.sound

"""# Inheritance"""

class A:
    def __init__(self):
        self.name = "A"

class B:
    def __init__(self):
        self.newname = "B"

b = B()

b.name

class A:
    def __init__(self):
        self.name = "A"

class B(A):
    def __init__(self):
        self.newname = "B"
        super().__init__()       # super is keyword, or name and super is attribute

b = B()    # single inheritance

b.name

"""# Access specifier in python / or limiting variable behavior"""

class person:
    name = "Nirajan"     # public
    _teach = 'Python'    # protected
    __age = 24           # private

obj = person()

obj.name

obj._teach

obj.__age

"""# Polymorphism"""

2 + 3

[2, 7, 8] + [11, 0]

"hi" + "Good Morning"

"""# Other Example: Polymorphism in Function"""

len("Hi my name is Nirajan")

len([4, 77, 83, 0, -1])

len({'name': 'Nirajan'})

# polymorphism chahi operator overloading bata huxa

# dunders are used to overload operator     for example: __add__ overloads + operator

# Assignment: Write about Function overloading vs overriding
