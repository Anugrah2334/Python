#PROGRAM1(Creating Python Tuples)
values:tuple[int|str,...]=(1,2,4,"Geek")
print(values)
print("\n")

#PROGRAM2(Utility of Tuples)
quo,rem=divmod(100,3)
print("Quotient=",quo)
print("Remainder=",rem)
print("\n")

Tup1=(1,2,3,4,5)
Tup2=(6,7,8,9,10)
Tup3=Tup1+Tup2
print(Tup3)
print("\n")

#PROGRAM3(Accessing Values in Tuples)
Tup1=(1,2,3,4,5,6,7,8,9,10)
print("Tup[3:6]=",Tup1[3:6])
print("Tup[:8]=",Tup1[:8])
print("Tup[4:]=",Tup1[4:])
print("Tup[:]=",Tup1[:])
print("\n")

var=("Geeks","for","Geeks")
print("Value in Var[0]=",var[0])
print("Value in Var[1]=",var[1])
print("Value in Var[2]=",var[2])
print("Value in Var[-3]=",var[-3])
print("Value in Var[-2]=",var[-2])
print("Value in Var[-1]=",var[-1])
print("\n")

#PROGRAM4(Concatenating 2 Tuples)
tuple1=(0,1,2,3)
tuple2=('pyhton','geek')
print(tuple1+tuple2)
print("\n")

#PROGRAM5(Deleting elements in Tuple)
#Tup1=(1,2,3,4,5)
#del Tup1[3]
#print(Tup1)
#Tup1=(1,2,3,4,5)
#del Tup1
#print(Tup1)
#tuple1=(90,1,2,3)
#tuple1[0]=4
#print(tuple1)
#tuple3=(0,1)
#del tuple3
#print(tuple3)

#PROGRAM6(value assignment)
val1,val2,val3=(1,2,3)
print(val1,val2,val3)
Tup1=(100,20,300)
(val1,val2,val3)=Tup1      #tuple assigned to another Tuple
print(val1,val2,val3)
#expression are evaluated before assignment
(val1,val2,val3)=(2+4,5/3+4,9%6)
print(val1,val2,val3)
print("\n")

#PROGRAM7(Tuples for returning multiple values and Nested Tuples)
def max_min(vals):
    x=max(vals)
    y=min(vals)
    return(x,y)
vals=(99,98,90,97,89,86,93,82)
(max_marks,min_marks)=max_min(vals)
print("Highest Marks=",max_marks)
print("Lowest Marks=",min_marks)
print("\n")

Toppers=(("Arav","BSc",92.0),("Chaitanya","BCA",99.0),("Dhruvika","Btech",97))
for i in Toppers:
    print(i)
print("\n")

#PROGRAM8(Creating Nested Tuples)
tuple1=(0,1,2,3)
tuple2=('python','geek')
tuple3=(tuple1,tuple2)
print(tuple3)
print("\n")

#PROGRAM9(Create a Tuple with repetition)
tuple3=('python',)*3
print(tuple3)
print("\n")

#PROGRAM10(Checking the Index)
Tup=(1,2,3,4,5,6,7,8)
print(Tup.index(4))

students=("Bhavya","era","Falguni","Huma")
index=students.index("Falguni")
print("Falguni is present at location:",index)
#index=students.index("Isha")
#print("isha is present at location:",index)
print("\n")

#PROGRAM11(count()Method)
tup="abcdxxxabcdxxxabcdxxx"
print("x apperas",tup.count('x'),"times in",tup)

def double(T):
    return([i*2 for i in T])
Tup=1,2,3,4,5
print("Original Tuple:",Tup)
print("Double values:",double(Tup))
print("\n")

#PROGRAM12(Variable-length Argument Tuple)
def display(*args):
    print(args)
Tup=(1,2,3,4,5,6)
display(Tup)
print("\n")

#PROGRAM13(zip() function)
Tup=(1,2,3,4,5)
List1=['a','b','c','d','e']
print(list((zip(Tup,List1))))
print("\n")

#PROGRAM14(Creating Set)
s={1,2.0,"abc"}
print(s)
print("\n")

#PROGRAM15(Set Operation)
s=set([1,2,3,4,5])
t=set([6,7,8])
s.update(t)
print(s)

s=set([1,2,3,4,5])
s.add(6)
print(s)

s=set([1,2,3,4,5])
s.remove(3)
print(s)

s=set([1,2,3,4,5])
s.discard(3)
print(s)

s=set([1,2,3,4,5])
s.pop()
print(s)

s=set([1,2,3,4,5])
s.clear()
print(s)

s=set([1,2,3,4,5])
print(len(s))

s=set([1,2,3,4,5])
print(3 in s)

s=set([1,2,3,4,5])
print(6 not in s)

s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
print(s<=t)

s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
print(s.issuperset(t))

s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
print(s|t)

s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
z=s&t
print(z)

s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
s.intersection_update(t)
print(s)

s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
z=s-t
print(z)

s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
s.difference_update(t)
print(s)

s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
z=s^t
print(z)

s=set([1,2,3,4,5])
t=set([1,2,3,4,5,6,7,8,9,10])
print(s.copy())

s=set([1,2,3])
t=set([4,5,6])
print(s.isdisjoint(t))

s=set([0,1,2,3,4])
print(all(s))

s=set([0,1,2,3,4])
print(any(s))

s=set(['a','b','c','d'])
for i in enumerate(s):
    print(i,end=' ')

s=set([0,1,2,3,4,5])
print(max(s))

s=set([0,1,2,3,4,5])
print(min(s))

s=set([0,1,2,3,4,5])
print(sum(s))

s=set([5,4,3,2,1,0])
print(sorted(s))

s=set(['a','b','c'])
t=set("abc")
z=set(tuple('abc'))
print(s==t)
print(s!=z)

#PROGRAM16(Creating Dictionary)
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(Dict)

#PROGRAM17(Access value in Dictionary)
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print("Dict[ROLL_NO]=",Dict['Roll_No'])
print("Dict[NAME]=",Dict['Name'])
print("Dict[COURSE]=",Dict['Course'])
print("\n")

#PROGRAM18(Adding and Modifying Item in a Dictionary)
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print("Dict[ROLL_NO]=",Dict['Roll_No'])
print("Dict[NAME]=",Dict['Name'])
print("Dict[COURSE]=",Dict['Course'])
Dict['Marks']=95     #new entry
print("Dict[MARKS]=",Dict['Marks'])
print("\n")

#PROGRAM19(Modify Entry in a Dictionary)
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print("Dict[ROLL_NO]=",Dict['Roll_No'])
print("Dict[NAME]=",Dict['Name'])
print("Dict[COURSE]=",Dict['Course'])
Dict['Marks']=95     #new entry
print("Dict[MARKS]=",Dict['Marks'])
Dict['Course']='BCA'
print("Dict[COURSE]=",Dict['Course'])  #entry updated
print("\n")

#PROGRAM20(Deleting Items in Dictionary)
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print("Name is:",Dict.pop('Name'))     #returns name
print("Dictionary after popping Name is:",Dict)
print("Marks is:",Dict.pop('Marks',-1)) #returns default value
print("Dictionary after popping mark sis:",Dict)
print("Randomly popping any item:",Dict.popitem())
print("Dictionary after random popping is:",Dict)
#print("Aggregate is:",Dict.pop('Aggr'))  #generate error
#print("Dictionary after popping aggregate is:",Dict)

#PROGRAM21(Sorting Item and Looping over Items in Dictionary)
Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(sorted(Dict.keys()))
print("\n")

Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print("KEYS:",end='')
for keys in Dict:
    print(keys, end=' ')   #accessing only keys
print("\nVALUES:",end=' ')
for val in Dict.values():
    print(val, end=' ')   #accessing only values
print("\nDICTIONARY:",end=' ')
for key, val in Dict.items():
    print(key,val,"\t",end=' ')  #accessing keys and values
print("\n")

#PROGRAM22(Nested Dictionary)
Students={'Shiv':{'CS':90,'DS':89,'CSA':92},'Sadhvi':{'CS':91,'DS':87,'CSA':94},'Krish':{'CS':93,'DS':92,'CSA':88}}
for key,val in Students.items():
    print(key, val)
print("\n")

#PROGRAM23(Dictionary Functions)
Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(len(Dict1))

Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(str(Dict1))

Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
Dict1.clear()
print(Dict1)

Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
Dict2=Dict1.copy()
print("Dict:",Dict2)
Dict2['Name']='Saesha'
print("Dict1 after modification:",Dict1)
print("Dict2 after modification:",Dict2)

Subjects=['CSA','C++','DS','OS']
Marks=dict.fromkeys(Subjects,-1)
print(Marks)

Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(Dict1.get('Name'))

Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print('Marks' in Dict1)

Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(Dict1.items())

Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(Dict1.keys())

Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
Dict1.setdefault('Marks',0)
print(Dict1['Name'],"has got marks=",Dict1.get('Marks'))

Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
Dict2={'Marks':90,'Grade':'O'}
Dict1.update(Dict2)
print(Dict1)

Dict1={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print(Dict1.values())

#Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
#for i,j in Dict.iteritems():
#   print(i, j)

Dict={'Roll_No':'16/001','Name':'Arav','Course':'BTech'}
print('Name' in Dict)
print('Marks' in Dict)
print("\n")

#PROGRAM24(String formatting with Dictionaries)
Dict={'Sneha':'BTech','Mayank':'BCA'}
for key,val in Dict.items():
    print("%s is studying %s" %(key,val))







