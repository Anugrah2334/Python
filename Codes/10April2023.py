class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)
class teacher(person):
    def __init__(self, name, age, exp, r_area):
        person.__init__(self, name, age)
        self.exp=exp
        self.r_area=r_area
    def displaydata(self):
        person.display(self)
        print('Experience:', self.exp)
        print('Research area:', self.r_area)
class student(person):
    def __init__(self, name, age, course, marks):
        person.__init__(self, name, age)
        self.course=course
        self.marks=marks
    def displaydata(self):
        person.display(self)
        print('Course:', self.course)
        print('Marks:', self.marks)
print('********TEACHER***********')
t=teacher('Jaya', 43,20, 'Recommneder Systems')
t.displaydata()
print('********STUDENT************')
s=student('Mani', 20, 'BTech', 78)
s.displaydata()

class parent:
    def __init__(self, txt):
        self.message=txt
    def printmessage(self):
        print(self.message)
class child(parent):
    def __init__(self, txt):
        super().__init__(txt)
x=child('Hello, and Welcome!')
x.printmessage()


#multiple inheritance
class base1(object):
    def __init__(self):
        super(base1, self).__init__()
        print('Base1 class ')
class base2(object):
    def __init__(self):
       super(base2, self).__init__()
       print('Base2 class')
class derived(base1, base2):
    def __init__(self):
        super(derived, self).__init__()
        print('Derived class')
d=derived()

class class1:
    def m(self):
        print('In class 1')
class class2(class1):
    def m(self):
        print('In class 2')
class class3(class1):
    def m(self):
        print('In class 3')
class class4(class2, class3):
    pass
obj=class4()
obj.m()

#multilevel

class person:
    def name(self):
        print('name....')
class teacher(person):
    def qualification(self):
        print('Qualification....Ph.D must')
class HOD(teacher):
    def experience(self):
         print('Experience.....at least 15 years')
hod=HOD()
hod.name()
hod.qualification()
hod.experience()
        
#multipath
class student:
    def name(self):
        print('Name...')
class academic_performance(student):
    def acad_score(self):
        print('Academic score....90% and above')
class ECA(student):
    def ECA_score(self):
        print('ECA score....60% and above')
class result(academic_performance, ECA):
    def eligibility(self):
        print('********************Minimun eligibily to apply***************')
        self.acad_score()
        self.ECA_score()
r=result()
r.eligibility()
