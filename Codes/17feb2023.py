#PROGRAM1 (List)
list_A=[1,2,3,4,5]
print(list_A)

list_B=['A','b','c','d','E']
print(list_B)

list_C=["good","going"]
print(list_C)

list_D=[1,'a','bcd']
print(list_D)
print("\n")

#PROGRAM2 (List Creation)
L1=[1,2,5,4]
L5=L1[:]
print(L5)

L6=L1[0:2]
print(L6)
print("\n")

#PROGRAM3 (List Comprehension)
S=[x**2 for x in range(10)]
print(S)

A=[3,4,5]
B=[value *3 for value in A]
print(B)

B=[]
for i in A:
    B.append(i*3)
    print(B)

C=[i for i in S if i%2==0]
print(C)

l=list()
print(l)

A=B=[10,20,30]
print(A,B)


