import time
class Student:
     count = 0
     def __init__(self, id, name,BirthOfDate,address,phone,DTB):
        self.id = id
        self.name = name
        self.BirthOfDate= BirthOfDate
        #self.age = None
        #self.age = time.localtime() - self.BirthOfDate.year
        self.address = address
        self.phone = phone
        self.DTB = DTB
        Student.count += 1
     def get_id(self):
         return self.id
     def set_Name(self,name):
         self.name = name
     def get_Name(self):
         return self.name
     def set_BirthOfDate(self,BirthOfDate):
         self.BirthOfDate = BirthOfDate
     def get_BirthOfDate(self):
         return self.BirthOfDate
     def set_Address(self,address):
         self.address = address
     def get_Address(self):
         return self.address
     def set_Phone(self,phone):
         self.phone = phone
     def get_Phone(self):
         return self.phone
     def set_DTB(self,DTB):
         self.DTB = DTB
     def get_DTB(self):
         return self.DTB
     def show(self,listSV):
          print("========================Information of Student==============================")
          #print(" ID "," NAME "," BIRTH OF DATE "," ADDRESS "," PHONE "," DTB ")
          #print(" "+ self.id + " " + self.name + " " + self.BirthOfDate +" "+ self.address + " " + self.phone + " " + self.DTB)
          '''print(f"ID: {self.id}")
          print(f"Name: {self.name}")
          print(f"BirthOfDate: {self.BirthOfDate}")
          print(f"Address: {self.address}")
          print(f"Phone: {self.phone}")
          print(f"DTB: {self.DTB}")'''
          print("{:<8} {:18} {:<8} {:18} {:<18} {:<8}".format("ID","Name","BirthOfDate","Address","Phone","DTB"))
          if listSV.__len__() > 0:
              for i in listSV:
                  print("{:<8} {:18} {:<8} {:<18} {:<18} {:<8}".format(i.id,i.name,i.BirthOfDate, i.address,i.phone,i.DTB))
          print("\n")
          