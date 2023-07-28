class student:
    def name(self):
        print('Name...')
class academic_perfromance(student):
    def acad_score(self):
        print(f'Academic score....90% and above')
class eca(student):
    def eca_score(self):
        print(f'ECA score....60% and above')
class result(academic_perfromance, eca):
    def eligibilty(self):
        print('********Minimum eligibility***********')
        self.acad_score()
        self.eca_score()
r=result()
r.eligibilty()

class polygon:
    def __init__(self, no_of_sides):
        self.n=no_of_sides
        self.slides=[0 for i in range (no_of_sides)]
    def inputslides(self):
        self.slides=[float(input('Enter side'+str(i+1)+':')) for i in range (self.n)]
                     
    def dispslides(self):
        for i in range(self.n):
            print('Side', i+1, 'is', self.slides[i])
class triangle(polygon):
    def __init__(self):
        polygon.__init__(self, 3)
    def findarea(self):
        a,b,c=self.slides
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print(f'The area of the triangle is {area}')
t=triangle()
t.inputslides()
t.dispslides()
t.findarea()

class base1(object):
    def __init__(self):
        print('Base1 class')
class base2(object):
    def __init__(self):
        print('Base2 class')
class derived(base1, base2):
    pass
d=derived()

def add(x,y,z=0):
    return z+y+z
print(add(2,3))
print(add(2,3,4))

class india():
    def capital(self):
        print('New delhi is the capital of India')
    def language(self):
        print('Hindi is the most widely spoken language of India')
    def type(self):
        print('India is a development country')
class USA():
    def capital(self):
        print('Washington, D.C. is the capital of USA')
    def language(self):
        print('English is the primary language of USA')
    def type(self):
        print('Usa is a development country')
obj_ind=india()
obj_usa=USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

class parent():
    def __init__(self):
        self.value='Inside Parent'
    def show(self):
        print(self.value)
class child(parent):
    def __init__(self):
        self.value='Inside child'
    def show(self):
        print(self.value)
obj1=parent()
obj2=child()
obj1.show()
obj2.show()

class parent1():
    def show(self):
        print('Inside parent1')
class parent2():
    def display(self):
        print('Inside parent2')
class child(parent1, parent2):
    def show(self):
        print('Inside child')
obj=child()
obj.show()
obj.display()

class parent():
    def display(self):
        print('Inside parent')
class child(parent):
    def show(self):
        print('Inside child')
class grandfchild(child):
    def show(self):
        print('Inside grandchild')
g=grandfchild()
g.show()
g.display()

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
