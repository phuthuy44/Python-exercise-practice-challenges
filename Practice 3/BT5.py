
class Shape:
     def __init__(self,color, name):
        self.color = color
        self.name = name
     def findarea(self):
         pass
     def findperimeter(self):
         pass
     def __str__(self):
         return self.name
     
class Circle(Shape):
     def __init__(self,name,color,radius):
          super().__init__(color, name)
          self.radius = radius
     def findarea(self):
         area = 3.14 * self.radius * self.radius
         return area
     def findperimeter(self):
         perimeter = 2 * 3.14 * self.radius
         return perimeter
class Rectangle(Shape):
     def __init__(self,name,color,width,height):
         super().__init__(color, name)
         self.width = width
         self.height = height
     def findarea(self):
         area = self.width * self.height
         return area
     def findperimeter(self):
         perimeter = (self.width + self.height) * 2
         return perimeter
class Square(Shape):
     def __init__(self, name, color,side):
          super().__init__(color, name)
          self.side = side
     def findarea(self):
         area = self.side * self.side
         return area
     def findperimeter(self):
         perimeter = self.side * 4
         return perimeter

while True:
     print(f'''\n
     ======Choose problem to solve ======
     0. Exit 
     1. Circle
     2. Rectangle
     3. Square
     ''')
     select = int(input('Enter your choice: '))
     if str(select).isdigit():
          select = int(select)
          if select == 0:
               break
          elif select == 1:
              radius = float(input('Enter the radius of the circle: '))
              Circle = Circle("Circle", "red", radius)
              print("Area: ", Circle.findarea())
              print("Perimeter: ", Circle.findperimeter())
          elif select == 2:
              width = float(input('Enter the width of the rectangle: '))
              height = float(input('Enter the height of the rectangle: '))
              rectanle = Rectangle("Rectangle", "green", width, height)
              print("Area: ", rectanle.findarea())
              print("Perimeter: ", rectanle.findperimeter())
          elif select == 3:
              side = float(input('Enter the side length of the square: '))
              square = Square("Square", "blue", side)
              print("Area: ", square.findarea())
              print("Perimeter: ", square.findperimeter())
     else :
         print("\n You must enter a number! Please try again.")
