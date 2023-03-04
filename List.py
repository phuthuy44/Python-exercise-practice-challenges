# create list
print ("Two standard ways to crate an empty list:")
a = [] #list is empty
b = list() # list is empty
#List have an element
a= ["hello"]
b= ["42"]
#List have many elements
a= [2,3,5,7]
b = list(range(5))
c= ["mixed types", True, 42]

n = 10
a = [0]*n 
b = list(range(n))
print(type(a),len(a),a) #<class'list'> 10 [0,0,0,0,0,0,0,0,0,0,0]
print(type(b),len(b),b) #<class'list'> 10 [ 0,1,2,3,4,5,6,7,8,9]

a = [2,3,5,2]
print("a =",a)  # a= [2,3,5,2]
print("len = ",len(a))  # len = 4
print("min = ", min(a)) #min = 2
print("max = ", max(a)) #max = 5
print("sum = ", sum(a)) #sum = 12

a = [2,3,5,7,11,13]
print("a = ",a) # a= [2,3,5,7,11,13]
print("a[0] = ",a[0]) # a[0]=2
print("a[1] = ",a[1]) # a[1]=3
print("a[2] = ",a[2]) # a[2]=5
#chi so am
print("a[-3] = ",a[-3]) # a[-3]=7
print("a[-2] = ",a[-2]) # a[-2]=11
print("a[-1] = ",a[-1]) # a[-1]=13
#mot khoang nam trong list
print("a[0:3] = ",a[0:3]) # a[0:3]= [2,3,5]
print("a[1:3] = ",a[1:3]) # a[1:3]= [3,5,7]
print("a[2:3] = ",a[2:3]) # a[2:3]= [5]
print("a[3:3] = ",a[3:3]) # a[3:3]= []
print("a[1:4] = ",a[1:4]) # a[1:4]= [3,5,7]
print("a[1:6:2] =",a[1:6:2]) # a[1:6:2]= [3,7,13]

'''List Aliases: Alias la kha nang ma tai 1 o nho co nhieu doi tuong cung tro toi'''
a = [2,3,5,7] #creatte a list 
b = a #create a copy of a list
#co 2 tham chieu cung 1 luc
a[0] = 42 
b[1] = 99
print(a) #a =[42,99,5,7]
print(b) #b=[42,99,5,7]

'''Tim phan tu trong list : in va not in'''
a = [2,3,5,2,6,2,2,7] 
print("a =",a) # a= [2,3,5,2,6,2,2,7]
print("2 in a =",(2 in a)) # True   
print("4 in a =",(4 in a)) # False
print("2 not in a =",(2 not in a)) # False
print("4 not in a =",(4 not in a)) # True
'''Dem so lan xuat hien: list.count(item)'''
print ("a.count(2) =",a.count(2)) # 4
print ("a.count(4) =",a.count(4)) # 0
print ("a.count(1) =",a.count(1)) # 0
print("a.count(3) =",a.count(3)) #1
'''Tim chi so cua mot phan tu:list.index(item) va list.index(item,start)'''
print ("a.index(6)", a.index(6)) #4
print("a.index(2) = ",a.index(2)) #0
print("a.index(2,1) = ",a.index(2,1)) #3
print("a.index(2,4) = ",a.index(2,4)) #5
##print("a.index(2,7) = ",a.index(2,7)) #Traceback (most recent call last):

'''Them mot phan tu hoac mot list vao list: khi them se thay doi list hoac tao list moi'''
#Them mot phan tu dung: list.append(item)
a = [2,3]
a.append(5)
print("a =",a) # a= [2,3,5]
#Them mot list vao mot list : list += list
a = [2,3]
a +=[11,13]
a += [0]
print("a =",a) # a= [2,3,11,13,0]
#Them mot list dung list.extend(list)
a = [2,3]
a.extend([11,13])
print("a =",a) # a= [2,3,11,13]
#Them mot phan tu tai vi tri cho truoc: dung insert()
a = [ 2,3,5,7,11]
a.insert(2,42) #at index 2, insert 42
print("a =",a) # a= [2,3,42,5,7,11]
#them phan tu hoac list bang cach tao list moi
a = [2,3]
b = a + [13,17]
print(a) # a= [2,3]
print(b) # b= [2,3,13,17]
c = a[:2] +[5] + a[2:]
print(c) # c= [2,3,5]
'''Thay doi cac phan tu trong list'''
letters =['a','b','c','d','e','f','g','h','i']
print("letters =",letters) # letters= ['a','b','c','d','e','f','g','h','i']
#thay the
letters[2:5]=['C','D','E']
print(letters) # letters= ['a','b','C','D','E','f','g','h','i']
#xoa
letters[2:5]=[]
print(letters) # letters= ['a','b','f','g,'h','i']
#xoa list bang cach thay tat ca cac phan tu bang 1 list rong
letters[:]=[]
print(letters)
'''Xoa phan tu dung toan tu del'''
a = [2,3,4,5,6,7,8]
del a[2:4]
print("a =",a) # a= [2,3,6,7,8]
'''Phuong thuc clear() cung duoc dung de lam rong 1 list'''
a = [2,3,4,5,6,7,8]
a.clear()
print("a =",a) # a= []
'''Xoa phan tu dua vao chi so bang cach tao list m'''
a = [2,3,5,3,7,5,11,13]
print("a =",a) #a = [2,3,5,3,7,5,11,13]
b = a[:2] + a[3:]
print("After b =",b)
print(b) #b = [2,3,3,7,5,11,13]
'''Hoan doi cac phan tu(swapping)'''
#Failed swap
a = [2,3,5,7]
print("a =",a) # a= [2,3,5,7]
a[0] = a[1]
a[1] = a[0]
print("After failed swap of a[0] and a[1]:")
print(a)    # a =[3,3,5,7]
'''swap dung bien temp'''
a = [2,3,5,7]
print("a =",a) # a  = [2,3,5,7]
temp = a[0]
a[0] = a[1]
a[1] = temp
print("After swap of a[0] and a[1]:")
print(a)    # a = [2,3,5,7]
'''swap dung paralled assignment'''
a = [2,3,5,7]
print(a)
a[0],a[1]=a[1],a[0]
print("After swap of a[0] and a[1]:")
print(a) # a = [3,2,5,7]
'''Vong lap fỏ otrong list'''
#Vong lap dung phan tu trong list: for item in list
a = [2,3,5,7]
print("Here are the items in a:")
for pt in a:
    print(pt) # 2,3,5,7
#Vong lap dung chi so trong list: for index in range(len(list))
a = [2,3,5,7]
print("Here are the items in a with their indexs:")
for i in range(len(a)):
    print("a[",i,"]=",a[i]) # a[0]=2, a[1]=3, a[2]=5, a[3]=7
#Duyet nguoc list dung chi so 
a = [2,3,5,7]
print("And here are the items in reverse:")
for index in range(len(a)):
     revIndex = len(a)-1-index
     print("a[",revIndex,"]=",a[revIndex]) # a[3]=7, a[2]=5, a[1]=3, a[0]=2
#Duyet nguoc list dung ham reversed()
a = [2,3,5,7]
print("And here are the items in reversed:")
for item in reversed(a):
     print(item) # 7, 5, 3, 2
print(a) # a = [2,3,5,7]
'''So sanh list'''
#create some list 
a = [2,3,5,3,7]
b = [2,3,5,3,7] #same a
c = [2,3,5,3,8] #different in last element
d =[2,3,5] #prefix of a
print("a =",a) # a= [2,3,5,3,7]
print("b =",b) # b= [2,3,5,3,7]
print("c =",c) # c= [2,3,5,3,8]
print("d =",d) # d= [2,3,5]
print("--------------------")
print("a == b =",a == b) # True
print("a == c =",a == c) # False
print("a != b =",a != b) # False
print("a!= c =",a!= c) # True
print("--------------------")
print("a < c",(a<c)) #True
print("a<d",(a<d)) #False
'''Coppy list voi List Aliasses'''
import copy
#create a list
a = [2,3]
#try to copy it
b = a # Error! Not a copy, but an alias
c = copy.copy(a)
print("At first....")
print("a =",a) # a= [2,3]
print("b =",b) # b= [2,3]
print("c =",c) # c= [2,3]
#Now modify a[0]
a[0] = 42
print("But affter a[0] = 42")
print("a =",a) # a= [42,3]
print("b =",b) # b= [42,3]
print("c =",c) # c= [2,3]
'''Cac cach sao chep list'''
a = [2,3]
b = copy.copy(a)
c = a[:]
d = a + []
e = list(a)
f = sorted(a)
a[0] = 42
print(a,b,c,d,e,f) #[42,3][2,3][2,3][2,3][2,3][2,3]
'''Sap xep tren list'''
#sap xep va thay doi list dung list.sort(): iterable.sort(key =None,reverse = False)
a = [7,2,5,3,5,11,7]
b = list(a) #copy of a
print("At first a =",a) # a= [7,2,5,3,5,11,7]
a.sort()
print("After sorting a =",a) # a= [2,3,5,5,7,7,11]
print("At first b =",b) # b= [7,2,5,3,5,11,7]
b.sort(reverse=True)
print("After b:sort(reverse=True) =",b) # b= [11,7,7,5,5,3,2]
'''Sap xep nhung khong thay doi list(tao ra list moi) dung sorted(list):sorted(iterable,key=None,reverse=False)'''
a = [7,2,5,3,5,11,7]
print("At first a =",a) # a= [7,2,5,3,5,11,7]
b = sorted(a)
c = sorted(a,reverse=True)
print("After b = sorted(a)") 
print("a =",a) # a= [7,2,5,3,5,11,7]
print("b =",b) # b= [2,3,5,5,7,7,11]
print("c =",c) # c= [11,7,7,5,5,3,2]
'''Sap xep voi key function'''
#Dung abs()
a = [10,2,-5,8,-3,7,1]
print(sorted(a)) # [-5,-3,1,2,7,8,10]
print(sorted(a,key = abs)) #[1,2,-3,-5,7,8,10]
'''Sort dua vao chieu dai cua chuoi'''
a = ['a','ab','aab','ac','abccc']
print(sorted(a)) # ['a','ab','aab','ac','abccc']
def mylensort(a):
     return len(a)
print(sorted(a,key = mylensort)) #['a','ac','ab','aab','abccc']
'''List va function: list duoc dung nhu input cua mot ham'''
def countOdds(a):
     count = 0
     for item in a:
          if(item % 2 == 1):
               count += 1 
     return count
print(countOdds([2,3,7,8,21,23,24]))
'''Dung ham de thay doi cac gia tri cua list'''
def fill(a,value):
     for i in range(len(a)):
          a[i]== value
a =[1,2,3,4,5]
print("At first a =", a) # a= [1,2,3,4,5]
fill(a,42)
print("After filling a =", a) # a= [42,42,42,42,42]
'''List comprehension:cach tao list moi ngan gon- la mot bieu thuc di kem voi lenh for duoc dat trong cap dau ngoac vuong'''
cub3 = [3**x for x in range(9)]
#output:[1,3,9,27,81,243,729,2187,6561]
print(cub3)
#or 
cub3 =[]
for x in range(9):
     cub3.append(3**x)
print(cub3)

cub3 =[3**x for x in range(9) if x >4]
#output:[243,729,2187,6561]
print(cub3)
sole=[x for x in range(18) if x%2==1]
#output:[1,3,5,7,9,11,13,15,17]
print(sole)
noilist = [x +y for x in ['Ngon ngu','lap trinh'] for y in['Python','c++']]
#Output:['Ngon ngu python', 'lap trinh c++','Laptrinh Python,'Ngon ngu C++]
print(noilist)
'''converting Betwwen List and Stirngs'''
#use list(s) to convert a string to a list of characters
a = list ("wahoo!")
print(a) # ['w','a', 'h', '', 'o', '!']
a = "How are you?".split("")
print(a) #['How', 'are', 'you', '?']
a = ["parsley"," ","is"," ","fun"]
s = "".join(a)
print(s) #parsley is fun

'''2D list'''
#cap phat tinh 
#tao 2D list voi cac gia tri co dinh 
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a) #[[1,2,3],[4,5,6],[7,8,9]]
#wrong:cannot use *
rows = 3
cols = 2
a = [[0]*cols]*rows #Error
#chi tao duy nhat mot dong(unique row), phan con lai la aliases !
print("This seems ok. At first:")
print("a =",a) # a = [[0,0],[0,0],[0,0]]
a[0][0]=42
print("But see what happens after a[0][0] = 42")
print("a=",a) # a = [[42,0],[42,0],[42,0]]
#mo rong mot dong 
rows = 3
cols = 2
a = []
for row in range(rows):
     a += [[0]*cols]
print("This is ok. At first:")
print("a=",a) # a = [0,0],[0,0],[0,0]
a[0][0]= 42
print("And now see what happens after a[0][0]=42")
print("a=",a) # a = [[42,0],[0,0],[0,0]
# dung list comprehension
rows = 3
cols = 2
a =[([0]*cols) for row in range(rows)]
print("This is ok. At first:")
print("a=",a) # a = [[0,0],[0,0],[0,0]]
a[0][0]=42
print("And now see what happens after a[0][0]=42")
print("a=",a) # a = [[42,0],[0,0],[0,0]]
#tim so chieu cua 2D list : dung len()
a = [[2,3,5],[1,4,7]]
print("a =",a) # a = [[2,3,5],[1,4,7]]
rows = len(a)
cols = len(a[0])
print("rows = ",rows) # rows = 2
print("cols = ",cols) # cols = 3
#vong lap
a = [[2,3,5],[1,4,7]]
print("Before a =",a) # a = [[2,3,5],[1,4,7]]
rows = len(a)
cols = len(a[0])
for row in range(rows):
     for col in range(cols):
          a[row, col] += 1
print("After a =",a) # a = [[3,4,6],[2,5,8]]
'''Truy cap 2D list bang dong hoac cot'''
#truy cap mot dong
#alias(not a copy!); no new list created
a =[[1,2,3],[4,5,6]]
row = 1
rowList = a[row]
print(rowList) # [4,5,6]
rowList[0] = 100
print(rowList) # [100,5,6]
print(a) # [[1,2,3],[100,5,6]]
#truy cap mot cot 
#copy(not an alias!); new list created
a = [[1,2,3],[4,5,6]]
col = 1
colList = []
for i in range(len(a)): # co the dung list comprehension => colList = a[i][col] for i in range(len(a))
     colList += [a[i][col]]
print(colList) # [2,5]
'''So luong phan tu moi dong co the khac nhau'''
#2D list do not have to be rectangular 
a =[
     [1,2,3],
     [4,5],
     [6],
     [7,8,9,10]
]
rows = len(a)
for row in range(rows):
     col = len(a[row])#now cols depend on each row 
     print("Row",row,"has",cols,"columns",end="")
     for col in range(cols):
          print(a[row][col],end=" ")
     print()




    










