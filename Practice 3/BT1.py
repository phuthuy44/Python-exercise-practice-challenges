'''Phan A'''
#Cau 1
class HinhChuNhat:
     def __init__(self,width,height):
          self.width = width
          self.height = height
     def get_width(self):
          return self.width
     def get_height(self):
          return self.height
     def getArea(self):
          return self.width * self.height
HinhChuNhat = HinhChuNhat(5,10)
print("============Cau 1============")
print("Weight:", HinhChuNhat.get_width())
print("Height:", HinhChuNhat.get_height())
print("Area:", HinhChuNhat.getArea())
#Cau 2 
class Shape :
     def __init__(self):
          # TODO document why this method is empty
          pass 
     def getarea(self):
          return 0
class Square(Shape):
     def __init__(self,side):
          Shape.__init__(self)
          self.length = side
     def get_length(self):
          return self.length
     def getarea(self):
          return self.length * self.length
BT2 = Square(5)
print("===========Cau 2===========")
print("Length:",BT2.get_length())
print("Area:",BT2.getarea())

