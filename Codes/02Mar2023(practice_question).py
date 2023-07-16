#PROGRAM1(Write a program to sum up tuple elements)
Tuple=(10,20,30,40,50,60,70,80,90,200)
print("Elements in Tuple are:",Tuple)
print("Sum of the elements for the given Tuple is:",sum(Tuple))
print("\n")

#PROGRAM2(Write a program to add row wise elements in a tuple matrix)
list=[]
n=int(input('Enter the no. of rows you want to enter:'))
m=int(input('Enter the no. of columns you want to enter:'))
count=0
for i in range(1, m+1):
    for j in range(1, n+1):
       a=int(input('Enter the number:'))
       count+=a
       list.append(a)
    print(f'The tuple enter by the user in row {i} is {tuple(list)}')
    print(f'The sum of row {i} is {count}')
    list=[]
    count=0
print("\n")

#PROGRAM3(Write a program to update element in a tuple list)
def update(list):
    list[num-1]=value
    print("The updated list is:",list)
list=[1,4,3,4,5]
print(list)
num=int(input("Enter the position at which you want to update:"))
value=int(input("Enter the new value:"))
update(list)
print("\n")

#PROGRAM4(Write a program to interchange first and last element in a list)
L1=[1,2,3,4,5,6,7,8,9,10]
print("Original List:",L1)
length=len(L1)
temp=L1[0]
L1[0]=L1[length-1]
L1[length-1]=temp
print("List after intechanging first and last element:",L1)
print("\n")

#PROGRAM5(Write a program to check the length of the list)
L1=[1,2,3,4,5,6,7,8,9,10]
print("The elements of the list are:",L1)
print("Length of the given list is:",len(L1))
print("\n")

#PROGRAM6(Write a program to reverse a list)
L1=[1,2,3,4,5,6,7,8,9,10]
print("The original list is:",L1)
print("Now we will reverse the list")
L1.reverse()
print("List after reversing is:",L1)
print("\n")

#PROGRAM7(write a program to clone a list)
import copy
list=[]
n=int(input('Enter the number of element you want to enter:'))
for i in range(0, n):
    a=int(input('Enter the element:'))
    list.append(a)
list2=copy.copy(list)
print(f'The list before cloning:{list}')
print(f'The list after coloning:{list2}')
print("\n")

#PROGRAM8(write a program to count the occurrence of element in a list)
list=[]
n=int(input('Enter the number of element you want to enter:'))
for  i in range(0, n):
    a=int(input('Enter the element:'))
    list.append(a)
print(f'The list entered by the user:{list}')
m=0
for i in range(0, n):
    for j in range(0, n):
        if list[i]==list[j]:
            m+=1
    print(f'The occurance of {list[i]} is {m}')
    m=0
print("\n")

#PROGRAM9(write a program to calculate the sum and average of elements in list)
list=[]
n=int(input('Enter the number of element you want to enter:'))
count=0
for i in range(0, n):
    a=int(input('Enter the number:'))
    count+=a
    list.append(a)
avg=count/n
print(f'The list entered by the user:{list}')
print(f'The sum:{count} and average:{avg} of the list')
print("\n")

#PROGRAM10(write a program to multiply all no in a list)
list=[]
n=int(input('Enter the number of element you want to enter:'))
multi=1
for i in range(0, n):
    a=int(input('Enter the element:'))
    list.append(a)
    multi*=a
print(f'The list entered by the user:{list}')
print(f'The multiplication of all the number in the list:{multi}')
print("\n")

