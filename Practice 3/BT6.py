import datetime
import re
class NhanVien :
     def __init__(self, id,fullname,birthdate,email,phone,employee_type):
          self.ID = id
          self.FullName = fullname
          self.BirthDate = birthdate
          self.Phone = phone    
          self.Email = email
          self.Employee_type = employee_type
          employee_count = 0
          NhanVien.employee_count += 1
     def showInfo(self,listNV):
          print("{:<8} {:18} {:<8} {:18} {:<18}".format("ID","FullName","BirthOfDate","Email","Phone"))
          if listNV.__len__() > 0:
               for i in listNV:
                    print("{:<8} {:18} {:<8} {:<18} {:<18}".format(i.id,i.fullname,i.birthdate, i.email,i.phone))
          print("\n")
     def getId(self):
          return self.ID
     def getName(self):
          return self.FullName
     def getBirthDate(self):
          return self.BirthDate
     def getEmail(self):
          return self.Email
     def getPhone(self):
          return self.Phone
     def getEmployee_type(self):
          return self.Employee
     def setName(self):
          name = input("Enter the full name: ")
     def setEmail(self):
          email = input("Enter the email:")
     def setBirthDate(self):
          birthdate = input("Enter the birth date:")   
     def setPhone(self):
          phone = input("Enter the phone number:")
     def CheckBirthDate(self,birthdate):
          try :
               # Trying to convert a string to a datetime object.
               birthdate = datetime.datetime.strprime(birthdate,'%d/%m/%Y')
               return True
          except Exception:
               return False
     def CheckEmail(self,email):
          #Check Email format using regex
          pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
          if re.match(pattern, email) :
               return True
          else:
               return False
     def CheckFullName(self,fullname):
          # Checking if any character in the string is a digit.
          if any(char.isdigit() for char in fullname) :
               return False
          # Checking if the string contains any non-alphabetic characters.
          elif not fullname.isalpha() :
               return False
          else:
               return True
     def checkPhone(self,phone):
          patern = r'^\d{10}$'
          if re.match(patern, phone) :
               return True
          else :
               return False
     def add_NhanVien(self):
          listnv = []
          n = int(input("How many NhanVien do you want to add? "))
          for i in range(0,n):
               i.setName()
               i.setBirthDate()
               i.setEmail()
               i.setPhone()
               listnv.append(i)

     def register_user(self):
          if not NhanVien.CheckFullName(self.FullName) :
               raise Exception("Full name is not valid")
          if not NhanVien.CheckBirthDate(self.BirthDate) :
               raise Exception("Birth date is not valid")
          if not NhanVien.CheckEmail(self.Email) :
               raise Exception("Email is not valid")
          if not NhanVien.checkPhone(self.Phone) :
               raise Exception("Phone number is not valid")
     
class Experience(NhanVien):
     def __init__(self,id,fullname,birthdate,email,phone,employee_type,ExplnYear,ProSkill):
          super().__init__(id,fullname,birthdate,email,phone,employee_type)
          self.ExplnYear = ExplnYear
          self.ProSkill = ProSkill
     def getExplnYear(self):
          return self.ExplnYear
     def getProSkill(self):
          return self.ProSkill
     def setExplnYear(self, explnYear):
          self.ExplnYear = explnYear
     def setProSkill(self, proSkill):
          self.ProSkill = proSkill
     def showInfo(self, listNV):
          super().showInfo(listNV)
          print("{:<8} {:<8} {:<8}").format("Type","ExplnYear","ProSkill")
          print("{:<8} {:<8} {:<8}").format("Experience",self.ExplnYear,self.ProSkill)
class Fresher(NhanVien):
     def __init__(self,id,fullname,birthdate,email,phone,employee_type, GraduationRank, Education):
          super().__init__(id,fullname,birthdate,email,phone,employee_type)
          self.GradutionRank = GraduationRank
          self.Education = Education
     def getGraduationRank(self):
          return self.GradutionRank
     def getEducation(self):
          return self.Education
     def setGraduationRank(self, graduationRank):
          self.GradutionRank = graduationRank
     def setEducation(self, education):
          self.Education = education
     def showInfo(self, listNV):
          super().showInfo(listNV)
          print("{:<8} {:<8} {:<8}").format("Type ","GraduationRank","Education")
          print("{:<8} {:<8} {:<8}").format("Fresher",self.GradutionRank,self.Education)
class Intern(NhanVien):
     def __init__(self, id, fullname, birthdate, email, phone, employee_type,majors,semester,university):
          super().__init__(id, fullname, birthdate, email, phone, employee_type)
          self.majors = majors
          self.semester = semester
          self.university = university
     def getMajors(self):
          return self.majors
     def getSemester(self):
          return self.semester
     def getUniversity(self):
          return self.university
     def setMajors(self, majors):
          self.majors = majors
     def setSemester(self, semester):
          self.semester = semester
     def setUniversity(self, university):
          self.university = university
     def showInfo(self, listNV):
          super().showInfo(listNV)
          print("{:<8} {:<8} {:<8} {:<8}").format("Type","Majors","Semester","University")
          print("{:<8}{:<8} {:<8} {:<8}").format("Intern",self.majors,self.semester,self.university)
     