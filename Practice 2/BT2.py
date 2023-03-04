'''Phan B'''
#Cau1 :
print("===========Cau 1===========")
a = input("Enter string list:")
a = a.split(",")
print("List a:",a)
def stringCompare(str1):
    sorted_list = sorted(str1)
    print("List (String compare):",sorted_list)
def IntegerCompare(str1):
     sorted_list = sorted(a,key = int)
     print("List (Integer compare):",sorted_list)
stringCompare(a)
IntegerCompare(a)
print("\n")
#Cau2 :
print("===========Cau 2===========")
a = input("Enter string list:")
a = a.split(",")
print("List a:",a)
def delete_list(str1):
     index = [1,2,3,6]
     l =[element for i, element in enumerate(str1) if i not in index]
     print("Delete list:",l)
delete_list(a)
print("\n")
#Cau 3 :
print("===========Cau 3===========")
def delete_3():
     a = input("Enter string list:")
     a = a.split(",")
     print("List a:",a)
     def delete_3a():
     # Creating an empty list.
          b = []
          for i in a:
               if i not in b:
                    b.append(i)
          print("New list_3a : ["," , ".join(b),"]")
     def delete_3b():
          b = list(set(a))
          print("new list_3b : ["," , ".join(b),"]")
     delete_3a()
     delete_3b()
delete_3()
print("\n")
#Cau 4 
print("===========Cau 4===========")
def count_4():
     a = input("Enter string list:")
     a = a.split(",")
     print("List a:",a)
     a = [int(i) for i in a]
     def count_4a():
          b = []
          for i in a :
               if i not in b :
                    b.append(i)
          count_element = []
          for i in b :
               count = 0
               for j in a:
                    if i == j :
                         count += 1
               count_element.append(count)
          dic ={}
          for i in range(len(b)):
               dic[b[i]] = count_element[i]
          print("Cau 4a:")
          for element, value in dic.items():
               print(" {} : {} ".format(element, value))
     def count_4b():
          from collections import Counter
          dic = Counter(a)
          print("Cau 4b:")
          for element, value in dic.items():
               print(" {} : {} ".format(element,value))
     count_4a()
     count_4b()
count_4()
print("\n")
#Cau 5:
print("===========Cau 5===========")
def createList():
     def createList_5a():
          print("Cau 5a:")
          n = int(input("Enter number of elements:"))
          a = []
          for i in range(n):
               x = int(input("Enter element %d :" %(i+1)))
               a.append(x)
          print("List a:",a)
     def createList_5b():
          print("Cau 5b:")
          a = []
          while True:
               x = int(input("Enter element(Enter -1 to end):"))
               if x == -1 :
                    break
               a.append(x)
          print("List a:",a)
     createList_5a()
     createList_5b()
createList()
print("\n")
#Cau 6:
print("===========Cau 6===========")
def createList_6():
     a = input("Enter string list:")
     a = a.split(",")
     b = input("Enter string list:")
     b = b.split(",")
     print("List a:",a)
     print("List b:",b)
     def createList_6a():
          c= []
          for i in a :
               if i in b and i not in c:
                    c.append(i)
          print("List c:",c)
     def createList_6b():
          c = [i for i in b if i in a]
          print("List c:",c)
     createList_6b()
     createList_6a()
createList_6()

                    


