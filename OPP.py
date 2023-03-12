'''NameSpace'''
from types import SimpleNamespace
#Now we can create new object representing dogs:
dog1 = SimpleNamespace(name="Toki", age=10, breed ="Shephered")
print(dog1) #namespaces(age=10, breed="Shephered", name="Toki")
print(dog1.name) #Toki

dog1.name = "Tina"
print(dog1) #namespaces(age=10, breed="Shephered", name="Tina")
print(dog1.name) #Tina

dog2 = SimpleNamespace(name="Bom", age=12, breed ="poodle")
dog3 = SimpleNamespace(name="Tina", age=10, breed ="Shephered")
print(dog1 == dog2) #False 
print(dog1 == dog3) #True
print(type(dog1)) #<class 'types.SimpleNamespace'>
'''DataClass'''
from dataclasses import make_dataclass
#Now we can create new class named Dog where #instances(individula dogs) have 3 properties
#fields: name, age, breed
Dog = make_dataclass('Dog', ['name', 'age', 'breed'])
#Now we can create new instance of Dog class:
dog1 = Dog(name="Toki", age=10, breed ="Shephered")
print(dog1) #Dog(age=10, breed="Shephered", name="Toki")
print(dog1.name) #Toki
dog1.name = "Tina"
print(dog1) #Dog(age=10, breed="Shephered", name="Tina")
print(dog1.name) #Tina
try :
    dog2 = Dog(name="Kaki",age = 10)
except Exception as e:
    print(e) #missing 1 required positional argument: 'breed'
dog2 = Dog(name="Susi",age = 12, breed ="poodle")
dog3 = Dog(name="Tina",age = 10, breed ="Shephered")
print(dog1 == dog2) #False 
print(dog1 == dog3) #True
print(type(dog1)) #<class 'types.Dog'>
print(isinstance(dog1, Dog)) #True
'''Aliases : la kha nag ma tai 1 o nhow co nhieu doi tuong cung tro toi'''
#Objects are muntable so aliases change!
from types import SimpleNamespace
import copy 
dog1 = SimpleNamespace(name="Toki", age=10, breed ="Shephered")
dog2 = dog1   #this is an alias
dog3 = copy.copy(dog1) #this is a copy, not an alias
dog1.name = "Tina"
print(dog2.name) #Tina(the alias chaged, since it is the same object)
print(dog3.name) #Toki(the copy did not change, since it is a different object)
'''Classes'''
#A class must have a body, wvwn if it does nothing. so we will use 'pass for now'...
class MyNewClas:
    '''This is a docstring.I have created a new class'''
    pass
#class tao ra mot local namespace moi tro thanh noi de cac thuoc tinhs cua no duoc khai bao. thuoc tinh co the la ham hoac du lieu
#Ngoai ra, con co cac thuoc tinh dac biwt bat dau voi dau gach duoi kep(__) Vi du __doc__ se tra ve chuoi docstring mo ta cua lop do
class Person :
    '''this is a person class'''
    age = 10 
    def greet(self):
        print("hello!")
print(Person.age) #10
print(Person.greet) #<function Person.greet>
print(Person.__doc__) #this is a person class

person = Person() # create a object have name is person
print(person.greet) #<bound method Person.greet of <__main__.Person object>
#calling object's greate() method 
person.greet() #hello! == Person.greet(person)
'''Inheritance(Ke thua)'''
#class Polugon co thuoc tinh n de dinh nghia so canh va sides de luu gia tri moi canh.
class Polygon:
     def __init__(self,no_of_sides):
          self.n = no_of_sides
          self_sides = [0 for i in range(no_of_sides)]
     #Ham inputSides() nhap vao do lon cac canh
     def inputSides(self):
         self.sides = [
             float(input("Enter the side " + str(i+1) + ": "))
             for i in range(self.n)
         ]
     #ham dispSides() hien thi danh sach cac canh cua da giac
     def dispSides(self):
         for i in range(self.n):
             print("Side",i+1,"is",self.sides[i])
#create a class inheriting from Polygan
class Triangle(Polygon):
     def __init__(self):
          Polygon.__init__(self,3)
     def findArea(self):
          a,b,c = self.sides
          #calculate the semi-perimeter 
          s = (a + b + c) / 2
          area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
          print("The area of the triangle is %0.2f"%area)
if "name" == "__main__":
     t = Triangle()
     t.inputSides()
     t.findArea()
#kiem tra moi quan he cua 2 lop
#isinstance(object, class) return true if object is an instance of class or a instance of subclass of class
#issubclass(class1, class2) return true if class1 is a subclass of class2
     isinstance(t,Triangle) #True
     isinstance(t,Polygon) #True
     isinstance(t,int) #False
     isinstance(t,object) #True
     issubclass(Polygon,Triangle) #False
     issubclass(Triangle,Polygon) #True
     issubclass(bool,int) #True

