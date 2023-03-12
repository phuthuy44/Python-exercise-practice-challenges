class Student(object):
     def __init__(self, name, number):
          self.name = name
          self.number = number
          self.scorelist = [0]*number
     def getName(self):
          return self.name
     def getScores(self,i):
          return self.score[i]     
     def inputScore(self):
          for i in range(self.number):
               self.scorelist[i] = int(input("Enter score for subject {} : ".format(i+1)))
     def getAveraged(self):
          return sum(self.scorelist)/self.number
     def getHighscore(self):
          return max(self.scorelist)
     def hasScholarship(self):
          if self.getAveraged()>= 8.0 and all(score>= 4 for score in self.scorelist):
               return True
          return False
     def __str__(self):
          s = "Student name: {}\n".format(self.name)
          s += "Exam Scores: {}\n".format(self.scorelist)
          s = "Averaged Score: {}\n".format(self.getAveraged())
          return s
     
st = Student("Amed", 5)
#st.getName()
print(st.getName())
#st.getScores()
st.inputScore()
print(st)
print("Highest Score: {}\n".format(st.getHighscore()))
if st.hasScholarship():
     print("Student has Scholarship")
else :
     print("Student does not have Scholarship")
#st.getAveraged()