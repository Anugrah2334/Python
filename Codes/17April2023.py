class one:
    def set(self, var):
        self.var=var
    def get(self):
        return self.var
class two:
    def __init__(self, var):
        self.o=one()
        self.o.set(var)
    def show(self):
        print('Number=', self.o.get())
t=two(100)
t.show()


#abstract class
class fruit:
    def taste(self):
        raise NotImplementedError()
    def rich_in(self):
        raise NotImplementedError()
    def colour(self):
        raise NotImplementedError()
class mango(fruit):
    def taste(self):
        return 'sweet'
    def rich_in(self):
        return 'Vitamin A'
    def colour(self):
        return 'Yellow'
class orange(fruit):
    def taste(self):
        return 'Sour'
    def rich_in(self):
        return 'Vitamin c'
    def colour(self):
        return 'Orange'
alphanso=mango()
print(alphanso.taste(), alphanso.rich_in(), alphanso.colour())
org=orange()
print(org.taste(), org.rich_in(), org.colour())


class employee:
    raise_amt=1.04
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@email.com'
        self.pay=pay
    def fullname(self):
        return '{} {}',format(self.first, self.last)
    def apply_raise(self):
        self.pay=int(self.pay+self.raise_amt)
emp_1=employee('Corey', 'Schafer', 50000)
emp_2=employee('Test', 'Employee', 60000)
print(emp_1.first, emp_1.last, emp_1.email, emp_1.pay)
print(emp_2.first, emp_2.last, emp_2.email, emp_2.pay)

class employee:
    raise_amt=1.04
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@email.com'
        self.pay=pay
    def fullname(self):
        return '{} {}',format(self.first, self.last)
    def apply_raise(self):
        self.pay=int(self.pay+self.raise_amt)
    def __repr__(self):
        return "Employee('{}','{}','{})".format(self.first, self.last, self.pay)
    def __str__(self):
        return '{}-{}'.format(self.fullname(), self.email)
    def __add__(self,other):
        return self.pay+other.pay
    def __len__(self):
        return len(self.fullname())

emp_1=employee('Corey', 'Schafer', 50000)
emp_2=employee('Test', 'Employee', 60000)
print(emp_1.__repr__())
print(emp_1.__str__())
print(emp_1+emp_2)
print(len(emp_1))
print(len('test'))
print('test'.__len__())

class complex:
    def __init__(self):
        self.real=0
        self.imag=0
    def setValue(self, real, imag):
        self.real=real
        self.imag=imag
    def display(self):
        print('(', self.real,'+', self.imag,'i)')
c1=complex()
c1.setValue(1,2)
c2=complex()
c2.setValue(3,4)
c3=complex()
c3=c1+c2
c3.display()

class complex:
    def __init__(self,a ,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return self.a+other.a, self.b+other.b
obj1=complex(1,2)
obj2=complex(2,3)
obj3=obj1+obj2
print(obj3)

class a:
    def __init__(self, a):
        self.a=a
    def __add__(self, o):
        return self.a+o.a
ob1=a(1)
ob2=a(2)
ob3=a('Geeks')
ob4=a('For')
print(ob1+ob2)
print(ob3+ob4)
print(a.__add__(ob1,ob2))
print(a.__add__(ob3, ob4))
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))

def __add__(self, num):
    self.d+=num
    if self.m!=2:
        max_days=dict[self.m]
    elif self.m==2:
        isleap=chk_leap_year(self.y)
        if isleap==1:
            max_days=29
        else:
            max_days=28
    while self.d>max_days:
        self.d-=max_days
        self.m+=1
    while self.m>12:
        self.m-=12
        self.y+=1

class mylist:
    def __init__(self,list):
        self.list=list
    def __getitem__(self, index):
        return self.list[index]
    def __setitem__(self, index, num):
        self.list[index]=num
    def __len__(self):
        return len(self.list)
    def display(self):
        print(self.list)
l=mylist([1,2,3,4,5,6,7])
print('LIST IS:')
l.display()
index=int(input('Enter the index of list you want to access:'))
print(l[index])
index=int(input('Enter the indedx at which you want to mpdify:'))
num=int(input('Enter the correct number:'))
l[index]=num
l.display()
print('The length of my list is:', len(l))

class marks:
    def __init__(self):
        self.max_marks={'Maths':100, 'Computers':50, 'Science':75}
    def __contains__(self, sub):
        if sub in self.max_marks:
            return True
        else:
            return False
    def __getitem__(self,sub):
        return self.max_marks[sub]
    def __str__(self):
        return 'The dictionary has name of subjects and maximum marks allotted to them'
m=marks()
print(str(m))
sub=input('Enter the subject for which you want to know extra marks:')
if sub in m:
    print('Social studies paper has maximum marks allotted:', m[sub])

class number:
    def __init__(self, num):
        self.num=num
    def display(self):
        return self.num
    def __abs__(self):
        return abs(self.num)
    def __float__(self):
        return float(self.num)
    def __oct__(self):
        return oct(self.num)
    def __hex__(self):
        return hex(self.num)
    def __setitem__(self, num):
        self.num=num
n=number(-14)
print('N is:', n.display())
print('ABS(N) is:', abs(n))
n=abs(n)
print('Converting to float...., N is:', float(n))
print('Hexadecimal equivalent of N is:', hex(n))
print('Octal equivalent of N is:', oct(n))


class mult:
    def __init__(self, num):
        self.num=num
    def __call__(self, o):
        return self.num*o
x=mult(10)
print(x(5))



        

