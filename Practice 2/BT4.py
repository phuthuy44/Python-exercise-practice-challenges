'''Phan B'''
#Cau 1:
print("========Cau 1========")
def cau1():
     s = set(range(0,200))
     print("Print all element form 0 to 200:",s)
cau1()
print("\n")
#Cau 2:
print("========Cau 2========")
def cau2():
     def check_prime(n):
          if n < 2:
               return False
          for i in range(2,n):
               if n % i == 0:
                    return False
          return True
     def print_prime():
          s = set()
          for i in range(11,2000):
               if check_prime(i):
                    s.add(i)
          print("Print set of prime number:",s)
     print_prime()
cau2()
print("\n")
#Cau 3
import random
print("========Cau 3========")
def cau3():
     s1 = set(random.randint(10,2000) for i in range(random.randint(5,50)))
     s2 = set(random.randint(10,2000) for i in range(random.randint(5,50)))
     intersection = s1.intersection(s2) #intersection(Phep giao)
     union = s1.union(s2) #union(Phep hoi)
     different = s1.difference(s2) #difference
     sym_dic = s1.symmetric_difference(s2) #symmetric_difference
     print("Set 1:",s1)
     print("Set 2:",s2)
     print("Intersection of set 1 and set2:",intersection)
     print("Union of set 1 and set2:",union)
     print("Difference of set 1 and set2:",different)
     print("Symmetric difference of set 1 and set2:",sym_dic)
cau3()
print("\n")
#Cau 4 
print("========Cau 4========")
def cau4():
     n = int(input("Enter n key - value:"))
     d = {}
     for i in range(0,n):
          key = input("Enter key:")
          d[key] = input("Enter value:")
     print(d)
     s = set()
     for value in d.values():
          s.add(value)
     print("Print all different values:")
     for value in s:
          print(value , end =" ")
cau4()
print("\n")
#Cau 5
print("========Cau 5========")
def cau5():
     n = int(input("Enter n key - value:"))
     d ={}
     for i in range(0,n):
          key = input("Enter key:")
          d[key] = input("Enter value:")
     print(d)
     max_value = max(d.values())
     print("Maximum value in the dictionary:",max_value)
cau5()
print("\n")
#Cau 6
print("========Cau 6========")
def cau6():
     n = int(input("Enter n key - value:"))
     d ={}
     for i in range(0,n):
          key = input("Enter key:")
          d[key]= input("Enter value:")
     print(d)
     def find(dic):
          First_key = None
          second_key = None
          for key in d:
               # Checking if the first key is none or if the value of the key is greater than the
               # value of the first key.
               if First_key is None or d[key] > d[First_key]:
                    second_key = First_key
                    First_key = key
               elif second_key is None or d[key] > d[second_key]:
                    second_key = key
          return (First_key, second_key)
     First_key, second_key = find(d)
     print("The largest key is: ",First_key)
     print("The second largest key is: ",second_key)
cau6()
