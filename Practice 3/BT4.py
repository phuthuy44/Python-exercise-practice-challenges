class PHANSO:
     def __init__(self,tu=0,mau=1):
          self.tu = tu
          self.mau = mau
     def _input_(self):
          self.tu = int(input("Nhap tu so:"))
          self.mau = int(input("Nhap mau so:"))
          while self.mau == 0 :
               self.mau = int(input("Mau so khong hop le!Moi nhap lai:"))
     def USCLN(self,a,b):
          if b == 0:
               return a
          else :
               return self.USCLN(b,a%b)
     def rutgon(self):
          ucln = self.USCLN(self.tu,self.mau)
          self.tu = self.tu//ucln
          self.mau = self.mau//ucln
     def nghichdao(self):
          temp = self.tu
          self.tu = self.mau
          self.mau = temp
     def __str__(self):
          self.rutgon()
          return str(self.tu)+" /"+str(self.mau)
     def my_addition(self,ps):
          tu = self.tu * ps.tu + self.mau * ps.mau
          mau = self.mau *ps.mau
          result = PHANSO(tu,mau)
          result.rutgon()
          return result
     def add(self,ps):
          return self.my_addition(ps)
     def my_subtract(self,ps):
          tu = self.tu * ps.tu - self.mau * ps.mau
          mau = self.mau * ps.mau
          result = PHANSO(tu,mau)
          result.rutgon()
          return result
     def __sub__(self,ps):
          return self.my_subtract(ps)
     def my_multiply(self,ps):
          tu = self.tu * ps.tu
          mau = self.mau * ps.mau
          result = PHANSO(tu,mau)
          result.rutgon()
          return result
     def __mul__(self,ps):
          return self.my_multiply(ps)
     def my_division(self,ps):
          ps.nghichdao()
          return self.my_multiply(ps)
     def __truediv__(self,ps):
          return self.my_division(ps)
if __name__ == "__main__":
     ps1 = PHANSO(2,3)
     ps2 = PHANSO(4,5)
     print("Phan so 1:",ps1)
     print("Phan so 2:",ps2)
     ps1.rutgon()
     print("Phan so 1 sau khi rutgon:",ps1)
     ps3 = ps1.add(ps2)
     print("Tong 2 phan so :",ps3)
     ps3 = ps1.__mul__(ps2)
     print("Nhan 2 phan so :",ps3)
     ps3 = ps1.__truediv__(ps2)
     print("Chia 2 phan so :",ps3)
     ps3 = PHANSO()
     ps3._input_ ()
     print("Phan so 3 la:",ps3)
     
