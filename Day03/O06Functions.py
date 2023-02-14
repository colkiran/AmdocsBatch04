
def greet():
    print("Greeting Mr. Lionel Messi, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event")

# gname is non default arg, city is default arg
# non default should not follow default arg
def greetGstCty(gname, city="Barcelona"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the city")

greet()
print("-" * 40)

greetGst("Lionel Messi")
greetGst("Cristiano Ronaldo")

print("-" * 40)
greetGstCty("Messi")
greetGstCty("Neymar")
greetGstCty("Ronaldo", "Turin")

# Variable Length Arguments
def prodAll(*numbers):      # *numbers can take more than one value and store it in a tuple
    print(numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return prod

print(prodAll(1, 2, 3, 4, 5))

print("-" * 40)

def extractDetails(**details):
    print(details)
    print("-" * 40)
    for k, v in details.items():
        print(k, "=>", v)


extractDetails(name='Messi', age=35, goals=350, ballondor=7, club='PSG', country="Argentina")

print("-" * 40)
def mulMe(x, y):
    return x * y

print(f"The product of 8 and 7 is :{mulMe(8,7)}")

# python supports recursive calls
# using recursive calls write a code to find 1. factorial of a number 2.fibanocci series

# factorial
print("-" * 40)
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

num = 5
print(f"The factorial of {num} is :{fact(num)}")

# fibanocci series
print("-" * 40)
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

iter = 8
for i in range(iter):
    print(fibo(i), end=" ")
print()

print("-" * 40)
def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithCalc(20, 5)
print(f"res: {res}")

print("-" * 40)
from test import add
print(add(35, 82))


