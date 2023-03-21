'''PhanA'''
import numpy as np
def MangMotChieu():
     def Cau1():
          print("============Cau 1=============")
          x = np.arange(1,11)
          print(x)
          print(type(x))
          print(x.shape)
          y = np.pi/2 - x 
          z = np.cos(x) - np.sin(x)
          print(y)
          print(z)
          def checkPrime(x):
               if x < 2: return False
               for i in range(2,x):
                    if x%i == 0:
                         return False
               return True
          l = []
          for i in x :
               if checkPrime(i):
                    l.append(i)
          print(l)
          sochan = x[x%2==0]
          sole = x[x%2==1]
          print(sochan)
          print(sole)
          t = x.copy()
          x = np.where(t%2 == 0,-1,-2)
          print(x)
     def Cau2():
          print("============Cau 2=============")
          t = np.arange(4,10)
          print(t)
          print(t.min())
          print(t.max())
          print(t.argmax())
          print(t.argmin())
     def Cau3():
          print("============Cau 3==============")
          a = np.array([1,2,3,2,3,4,3,4,5,6])
          b = np.array([7,2,10,2,7,4,9,4,9,8])
          print(np.intersect1d(a,b))
          n = (a == b)
          print(np.array(list(set(a[n]))))
     def Cau4():
          print("============Cau 4================")
          a = np.array([2,6,1,9,10,3,27])
          l = []
          for i in a :
               if i > 5 and i < 10 :
                    l.append(i)
          print(l)
     Cau1()
     Cau2()
     Cau3()
     Cau4()
MangMotChieu()


          
          