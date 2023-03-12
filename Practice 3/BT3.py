class MyComplexNumber:
     def __init__(self,real = 0,imag = 0):
          self.real = real
          self.imag = imag
     def __str__(self):
          if self.imag < 0 :
               sign = '-'
          else :
               sign = '+'
          return f'''{self.real} {sign} {abs(self.imag)}'''
     def input(self):
          self.real = float(input('Enter real part: '))
          self.imag = float(input('Enter imaginary part: '))
     def my_addition(self,other):
          r = self.real + other.real
          i = self.imag + other.imag
          return MyComplexNumber(r,i)
     def my_subtraction(self,other):
          r = self.real - other.real
          i = self.imag - other.imag
          return MyComplexNumber(r,i)
     def my_multi(self,other):
          r = self.real * other.real - self.imag * other.imag
          i = self.real * other.imag + self.imag * other.real
          return MyComplexNumber(r,i)
     def my_division(self,other):
          sr,si,o_r,oi = self.real,self.imag,other.real,other.imag
          r = float(o_r**2 + oi**2)
          return MyComplexNumber((sr**o_r+si**oi)/r,(si**o_r-sr**oi)/r)
     def __add__(self,other):
          return self.my_addition(other)
     def __sub__(self,other):
          return self.my_subtraction(other)
     def __mul__(self,other):
          return self.my_multi(other)
     def __truediv__(self,other):
          return self.my_division(other)
     def magnitude(self):
          return ((self.real**2) + (self.imag**2))**0.5
     def compare(self,other):
          if self.magnitude() == other.magnitude():
               print("The magnitudes of I and J are equal.")
          elif self.magnitude() > other.magnitude():
               print("The magnitude of I is greater than the magnitude of J.")
          else :
               print("The magnitude of J is greater than the magnitude of I.")
     def __eq__(self,other):
          return self.magnitude () == other.magnitude ()
     def __lt__(self,other):
          return self.magnitude () < other.magnitude ()
     def __gt__(self,other):
          return self.magnitude () > other.magnitude ()
I = MyComplexNumber(10,2)
J = MyComplexNumber()
J.input()
print("I =",I)
print("J =",J)
print("I + J =",I+J)
print("I + J =",I.__add__(J))
print("I - J =",I.__sub__(J))
print("I - J =",I-J)
print("I * J =",I*J)
print("I * J =",I.__mul__(J))
print("I / J =",I/J)
print("I / J =",I.__truediv__(J))
I.compare(J)
I.__eq__(J)
I.__lt__(J)
I.__gt__(J)