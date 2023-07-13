#PROGRAM1
x=input("Enter your first name:")
y=input("Enter your last name:")
print("Enter your Date of Birth")
a=input("Month?")
b=input("Day?")
c=input("Year?")
print(x+y+" was born on "+a+b+c)
print("\n")

#PROGRAM3
x=int(input("Enter any number:"))
a=x+3
print("After addition of 3 to the eneterd number the rusult is:",a)
b=a*2
print("After than the result after multiplication by 2 is:",b)
c=b-2*x
print("After the subtraction of twice the original number result becomes:",c)
print("The final result is:",c)
print("\n")

#PROGRAM4
print("Program to convert temperature from farenheit to Celsius")
F=int(input("Enter the temperature in Farenheit:"))
C=(F-32)*5/9
print("Temperature in Celsius is:",C)
print("\n")

#PROGRAM5
def odd():
    x=int(input('Enter the number:'))
    return x%2==1
print(odd())
print("\n")

#PROGRAM6
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
def SubtractNumber(x,y):
    return x-y
print("The difference of two number is:",SubtractNumber(x,y))
print("\n")

#PROGRAM7
x=int(input("Enter any number:"))
def FourthPower():
    return x**4
print("The fourth power of the netered number is:",FourthPower())
print("\n")

#PROGRAM8
x=int(input("Enter the number:"))
import math
def calculate():
    a= math.log(x, 10)
    b=math.sin(x)
    c=math.cos(x)
    print("Log=",a)
    print("Sin=",b)
    print("Cosine=",c)
calculate()
print("\n")

#PROGRAM9 (a)
def tictactoe():
    print('________________________')
    print('|       |       |       |')
    print('|       |       |       |')
    print('|_______|_______|_______|')
    print('|       |       |       |')
    print('|       |       |       |')
    print('|_______|_______|_______|')
    print('|       |       |       |')
    print('|       |       |       |')
    print('|_______|_______|_______|')
tictactoe()
print("\n")

#PROGRAM9 (b)
def tictactoe():
    a=('______________________')
    b=('|______|______|______|')
    c=('|      |      |      |')
    print(f'{a}\n{c}\n{c}\n{b}\n{c}\n{c}\n{b}\n{c}\n{c}\n{b}')
tictactoe()
print("\n")

#PROGRAM10
import random
def roll_D(x,y):
    for i in range(0, y):
        print(random.randint(1,x))
    return print("That's all")
y=int(input('Enter the number you want to roll the dice:'))
roll_D(6,y)
print("\n")


    

