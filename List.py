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
print("a.index(2,7) = ",a.index(2,7)) #Traceback (most recent call last):

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











