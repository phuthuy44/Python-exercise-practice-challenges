#cau1
print("======Cau 1======")
input_s = input("Enter your String:")
split_words = input_s.split()
split_words.sort()
for word in split_words:
     print("".join(word))
print("\n")
#Cau 2
print("======Cau 2======")
input_binary = input("Enter your Binary:")
binary_list = input_binary.split(",")
lists = []
for binary in binary_list:
     dec = int(binary,2)
     lists.append(dec)
print("Cac gia tri thap phan tuong ung la:")
for dec in lists:
     print(" ".join(str(dec)))
print("\n")

#Cau 3
print("======Cau 3======")
s = input("Enter your String:")
s_count = {}
for s1 in s :
     if s1.isalpha():
          s_count[s1] = s_count.get(s1, 0) + 1

for char, count in s_count.items():
     print(char,":",count)
print("\n")
#Cau 4 
print("======Cau 4======")
s = input("Enter your String:")
s = s.title()
print(s)
print("\n")
#Cau 5
print("======Cau 5======")
s = input("Enter your String:")
upper = 0 
lower = 0
for string in s:
     if string.isupper():
          upper += 1
     elif string.islower():
          lower += 1
print("So luong chu in hoa và in thuong lan luot la:",str(upper),str(lower))
print("\n")
#Cau 6
import math
def is_prime(n):
     if n < 2 : return False
     k = int(math.sqrt(n))
     for i in range(2,k+1):
          if n % i == 0: return False
     return True
s = input("Enter your number_string:")
list =s.split(",")
lists=[]
for number in list:
     if is_prime(int(number)):
          lists.append(number)
print("Cac so nguyen to trong chuoi la: [",",".join(lists),"]")
print("\n")
#Cau 7
print("======Cau 7======")
s = input("Enter your String:")
s_split = s.split()
count = {} 
for word in s_split:
     if word in count :
          count[word] +=1 
     else:
          count[word] = 1

for word, countt in count.items():
     print(word,":",countt)
     

