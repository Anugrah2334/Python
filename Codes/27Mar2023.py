#PROGRAM1
num=int(input("Enter the numerator:"))
deno=int(input("Enter the denominator:"))
try:
    quo=num/deno
    print("quotient:",quo)
except ZeroDivisionError:
    print("Denominator cannot be zero")
print("\n")

#PROGRAM2
try:
    num=int(input("Enter the number:"))
    print(num**2)
except(KeyboardInterrupt):
    print("You should have eneterd a number...... Program Terminating...")
except(ValueError):
    print("Please check before you enter..... Program Terminating...")
print("Bye")
print("\n")

#PROGRAM3
try:
    num=int(input("Enter the number:"))
    print(num**2)
except(KeyboardInterrupt, ValueError, TypeError):
    print("Pleasr check before you enter.....Program terminating...")
print("Bye")
print("\n")

#PROGRAM4
try:
    file=open('File1.txt')
    str=f.readline()
    print(str)
except IOError:
    print("Error occoured during Input..... Program Terminating...")
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unecpected error....Program Terminating...")
print("\n")

#PROGRAM5
try:
    file=open('File1.txt')
    str=file.readline()
    print(str)
except IOError:
    print("Error occoured during Input..... Program terminating...")
else:
    print("Program terminating Successfully.....")
print("\n")

try:
    file=open('File.txt')
    dtr=f.readline()
    print(str)
except:
    print("Error occoured during Input..... Program Terminating...")
else:
    print("Program Terminating.....Successfully")
print("\n")
    
    

