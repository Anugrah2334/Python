#PROGRAM1 (Recurssive Function)
def tri_recurssion(k):
    if(k>0):
        result=k+tri_recurssion(k-1)
        print(result)
    else:
        result=0
    return result
print("\n\nRecurssion Example result")
tri_recurssion(6)
print("\n")

#PROGRAM2
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the value of n:"))
print("The factorial of",n,"is",fact(n))
print("\n")

#PROGRAM3
def countdown(n):
    print(n)
    if n==0:
        return          #Terminate recurssion
    else:
        countdown(n-1)
n=int(input("Enter the nunber:"))
countdown(n)
print("\n")

#PROGRAM4 (Documentation String)
def func():
    """The program just prints a message.
    It will display Hello World!!!    """
    print("Hello World!!!")
print(func.__doc__)
print("\n")

#PROGRAM5 (import statement)
from math import pi
print("PI=",+pi)
print("\n")

#PROGRAM6 (The dir() function)
def print_var(x):
    print(x)
x=10
print_var(x)
print(dir())
print("\n")

#PROGRAM7 (Module and Namespaces)
#module1
def repeat_x(x):
    return x*2

#module2
def repeat_x(x):
    return x**2
import module1
import module2
result=repeat_x(10)
print("\n")

#PROGRAM8 (Local, Global and Built-in namespaces)
def max(numbers):                            #global namespace
    print("USER DEFINED FUNCTION MAX.....")
    large=-1                                 #local namespace
    for i in numbers:
        if i>large:
            large=i
        return large
numbers=[9,-1,4,2,7]
print(max(numbers))
print("Sum of these numbers=",sum(numbers)) #built in namespace




