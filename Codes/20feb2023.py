#PROGRAM1(Access values in List)
num_list=[1,2,3,4,5,6,7,8,9,10]
print("num_list is:",num_list)
print("first element in the list is:",num_list[0])
print("num_list[2:5]=",num_list[2:5])
print("num_list[::2]=",num_list[::2])
print("num_list[1::3]=",num_list[1::3])

List=['Delhi', 'Chennai', 'Mumbai']
print(List[0:2])

List=[10, 20, 30, 40 , 50, 60]
print(List[::2])
print(List[4:])
print(List[:3])
print(List[:])
print(List[-1])
print("\n")

#PROGRAM2(Traversing List)
l1=[1, 2,3 ,4 ,5, 6,7 ,8, 9, 10]
i=0
while i<4:
    print(l1[i], end='\t')
    i+=1
print('\n')
for i in l1:
    print(i, end='\t')

#i=0
#while i<len[l1]:
#    print(l1[i])
#    i+=1
# continue
print("\n")

#PROGRAM3(Updating Value in Lits)
num_list=[1, 2, 3,4 ,5,6, 7,8 ,9, 10]
print('List is:', num_list)

num_list[5]=100
print('List after updation is:', num_list)

num_list.append(200)
print('List after appending is:', num_list)

del num_list[3]
print('list after deleting a value is:', num_list)

l1=[3, 4, 6, 7]
l1.append(70)
print(l1)

a=[100, 90, 80, 50]
l1.append(a)
print(l1)

List1=[1, 'a', 'abc', [2,3,4, 5], 8.9]
i=0
while i<(len(List1)):
    print('List1[',i,']=', List1[i])
    i+=1

l=['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(l[2])
print(l[2][2])
print(l[2][2][0])

#PROGRAM4(Change nested list item value)
l=['a', ['bb', 'cc'], 'd']
l[1][1]=0
print(l)

l[1].append('xx')
print(l)
l[1].insert(0, 'xx')
print(l)

l[1].extend([1, 2, 3])
print(l)

x=l[1].pop(1)
print(l)

print(x)
del l[1][1]
print(l)

l=['a', ['bb', 'cc'], 'd']
l[1].remove('cc')
print(l)

l=['a', ['bb', 'cc'], 'd']
print(len(l))
print(len(l[1]))

l=[[1, 2,3], [4, 5, 6], [7, 8, 9]]
for list in l:
    for number in list:
        print(number, end='\t')
print("\n")

#PROGRAM5(cloning lists)
list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2=list1
print('list1=', list1)
print('list2=', list2)
list3=list1[2:6]
print('List3=', list3)

#PROGRAM6(basic list operation)
#len
len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(len)
#concatenation
a=[1, 2, 3, 4, 5]+[6, 7, 8,9 ,10]
print(a)
#repetition
print(('Hello', 'World')*2)
#in
print('a' in ['a', 'e', 'i', 'o', 'u'])
#not in
print(3 not in [0, 2, 4, 6, 8])
#max
num_list=[6, 3, 7, 0, 1, 2, 4, 9]
print(max(num_list))
#min
num_list=[6, 3, 7, 0, 1, 2, 4, 9]
print(min(num_list))
#sum
num_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('SUM=', sum(num_list))
#all
num_list=[0, 1, 2, 3]
print(all(num_list))
#any
num_list=[6, 7, 7, 0, 1, 2, 4, 9]
print(any(num_list))
#list
#list1=list('HELLO')
#print(list1)
#sorted
list1=[3, 4, 1, 2, 7, 8]
list2=sorted(list1)
print(list2)
#sort
num_list=[6, 3, 7, 0, 1, 2, 4, 9]
num_list.sort()
print(num_list)
print("\n")

#PROGRAM7(stack in python)
stack=[1, 2, 3, 4, 5, 6]
print('Original stack is:', stack)
stack.append(7)
print('Stack after push operation is:', stack)
stack.pop()
print('Stack after pop operation is:', stack)
last_element_index=len(stack)-1
print('Value obtained after peep operation is:', stack[last_element_index])
print("\n")

#PROGRAM8(using list in queues)
queue=[1,2,3, 4, 5, 6]
print('Original queue is:', queue)
queue.append(7)
print('Queue after insertion is:', queue)
queue.pop(0)
print('Queue after deletion is:', queue)
print('Value obtained after peep operation is:', queue[(len(queue)-1)])


