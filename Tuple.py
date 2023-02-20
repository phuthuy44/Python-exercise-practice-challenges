t = (1,2,3)
print(type(t),len(t),t) #<class 'tuple'> 3 (1,2,3)
a = [1,2,3]
t = tuple(a)
print(type(t),len(t),t) #<class 'tuple'> 3 (1,2,3)
'''Create a tuple'''
#khong the thay doi gias tri trong tuple khi da gan(tuong tu nhu chuoi)
t = (1,2,3)
print(t[0])
t[0] = 42 #crash
print(t[0]) #Traceback(most recent call last):
          # TypeError : 'tuple' object does not support item assignment
t = (10,"quan tri mang",2j)
#t[0:2]=(10,'quan tri mang')
print("t[0:2] = ",t[0:2])
#Tuple rong
#Output:()
my_tuple = ()
print(my_tuple)
#tuple so nguyen
#Output:(2,4,16,256)
my_tuple = (2,4,16,256)
print(my_tuple)

#tuple co nhieu kieu du lieu
#Output = (10,"Quantrimang.com",3.5)
print(my_tuple)
#tuple long nhau
#Output:("QTM",[2,4,6],(3,5,7))
my_tuple = ("QTM",[2,4,6],(3,5,7))
print(my_tuple)
#tuple co the duoc tao ma khong can dau()
#con goi la dong goi tuple 
#Output:(10,"Quantrimang.com",3.5)
my_tuple = 10,"Quantrimang.com",3.5 
print(my_tuple)
#mo goi(unpacking) tuple cung co the lam duoc
#Output:
#10
#Quantrimang.com
#3.5
a,b,c = my_tuple
print(a)
print(b)
print(c)
#Parallel(tuple) assignment
(x,y) = (1,2) #1
print(x)       #2
print(y)
(x,y)=(y,x)
print(x)       #2
print(y)       #1
'''Singleton tuple suntax'''
t = (42)
print(type(t), t*5) #<class 'int'> 20
t = (42,)
print (type(t), t*5) #<class 'tuple'>(42,42,42,42,42)
t = (42,2)
print(type(t), t*2)  #<class 'tuple'>(42,2,42,2,42,2,42,2,42,2,42,2)
'''Truy cap vao cac phan tu cua tuple(tuong tu list): dung index[n] hoac [a:b] hoac [-k]'''
#tuple long nhau
n_tuple = ("Quantrimang.com",[2,6,8],(1,2,3))
#index long nhau
#Output:"r"
print(n_tuple[0][5])
#index long nhau 
#Output : 8 
print(n_tuple[1][2])
'''Thay doi mot tuple'''
my_tuple = (1,3,5,[7,9])
#Khong the thay doi phan tu cua tuple 
#ban se nhan duoc loi 
#TypeError : 'tuple' object does not support item assignment
my_tuple[1]=9

my_tuple = (1,3,5,[7,9])
#Nhung phan tu co index 3 trong tuple la list
#list co the thay doi, nen phan tu do co the thay doi 
#Output:(1,3,5,[7,9])
my_tuple[3][0] = 8
print(my_tuple)
#Neu can thay doi tuple hay gan lai cho no 
#Output:('q','u','v','w')
my_tuple = ('q','u','v','w')
print(my_tuple)
'''Noi tuple(+) va lap lai tuple(*)'''
#Noi 2 tuple 
#Output : (2,4,6,3,5,7)
print((2,4,6)+(3,5,7))
#Lap lai tuple
#Output:('Quantrimang.com','Quantrimang.com','Quantrimang.com','Quantrimang.com)
print(("Quantrimang.com",)*3)
'''Xoa tuple'''
QTM =['q','u','v','w']
#khong the xoa phan tu cua tuple 
#TypeError : 'tuple' object does not support item assignment
del QTM[3]
#co the xoa toan bo tuple 
del QTM
'''count(x): dem so phan tu x trong tuple'''
QTM = ['q','u','v','w']
#count
print(QTM.count('w')) #1
'''index(x): tra ve gia tri index cua ohan tu x dau tien ma no gap trong tuple'''
print(QTM.index('w')) #3
'''Toan tu : in va not in'''
QTM = ['q','u','v','w']
#kiem tra phan tu 
print('q' in QTM) #True
print('u' in QTM) #True
print('g' not in QTM) #False
#Vong lap va tuple
for ngonngu in('Python','C','C++','Java'):
     print("Lap trinh",ngonngu)




