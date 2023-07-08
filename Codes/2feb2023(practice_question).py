#PROGRAM1:Write a program to “stride” the character in a string.
str="Welcome to Python virtual Lab"
print("str[2:10:1]=",str[2:10:1])
print("str[3:7:2]=",str[3:7:2])
print("str[5:15:3]=",str[5:15:3])
print("\n")

#PROGRAM2:Write a program to count the length of a string.
str=input("Enter any string for which you want to calculate the length:")
print("Length of the string is:",len(str))
print("\n")

#PROGRAM3:Program to avoid whitespaces in string length.
str="Hello everyone I study in UPES"
a=str.replace(" ","")
print("String after removing whitespace:",a)
print("\n")

#PROGRAM4:Write a program to print even-length words in a string.
str="Python language has large standard Library"
x=str.split(" ")
for i in x:
    if len(i)%2==0:
        print(i)
print("\n")

#PROGRAM5:Write a program to print half words in upper case in a string.
a='hello everyone'
print('The original string is: {a}')
e=len(a)
s=len(a)
s=s//2
for i in range(0, s):
    print(a[i].upper(), end='')
for i in range (s, e):
    print(a[i], end='')
print("\n")

#PROGRAM6:Write a program to check if the string has one character and one digit.
a=input("Enter any string:")
print("The original string is:",a)
s=len(a)
for i in range(0, s):
    if a[i].isalpha():
        print('The string contains alphabet')
        break
for i in range(0, s):
    if a[i].isdigit():
        print('The string contains number')
        break
print("\n")




