'''Create a dictionary'''
#create a empty dictionary : dict() or {}
d = dict()
print(d) #prints {}
#create dic from a list(key,value)
pairs = [('a',1),('b',2),('c',3)]
d = dict(pairs)
print(d) #prints {'a': 1, 'b': 2, 'c':3}
#create dic
d ={"cow":5,"dog":92,"cat":1}
print(d) #prints {'cow': 5, 'dog': 92, 'cat': 1}
d1 = {1:'Quantrimang',2:'congnghe'}
d2 = {'ten':'QTM',1:[1,3,5]}
d3 = dict({1 : "QTM",2:"Python"})
d4 = dict([('ten','QTM'),(1,'Python')])
#Tu dien anh xa mot khoa den mot gia tri
ages = dict()
key = "tom"
value = 38
ages[key] = value #"tom" is the key and 38 is the value
print(ages) #prints {'tom': 38}
print(ages[key]) #prints 38
'''Cac tu khoa bieu dien theo kieu tap hop'''
#Khong co thu tu
d = dict()
d[2] = 100
d[4] = 200
d[8] = 300 
print(d) #prints {2: 100, 4:200 , 8:300} #unpredictable order
#Duy nhat
d = dict()
d[2] = 100
d[2] = 200
d[2] = 400
print(d) #{2:400}
#Cac tu khoa khong the thay doi 
d = {}
a =[1] # list are mutable, so...
d[a] = 42 #Error: unhashable type: 'list'
#Cac gia tri co the thay doi 
d = {}
a = [1,2]
d["fred"] = a
print(d) #prints {"fred": [1, 2]}
print(d["fred"]) #prints [1, 2]
a += [3]
print(d["fred"]) #prints [1, 2, 3]
#but keys may not mutable
d[a]= 42 #TypeError: unhashable type: 'list'
'''Cac phep toan trn tu dien'''
#Find length of a dictionary:len()
d = { 1 :[1,2,3,4,5],2:"abcd"}
print(len(d)) #prints 2
#create a copy of a dictionary:copy()
a1 = {1:"a"}
d2 = d1.copy()
d1[2] = "b"
print(d1) #prints {1:"a", 2:"b}
print(d2) #prints {1:"a"}
#Delete all elements from a dictionary:clear()
d = {1:"a",2:"b",3:"c"}
d.clear()
print(d,len(d)) # {} 0
#Interaction with a dictionary
d = {1:"a",2:"b",3:"c"}
for key in d :
    print(key,d[key])     #prints 1 a
                         #prints 2 b
                         #prints 3 c
#Toan tu : in and not in
d = {1:"a",2:"b",3:"c"}
print(0 in d) #prints False
print(1 in d) #prints True
print("a" in d) #surprised? False
d = {1:"a",2:"b",3:"c"}
print( 0 not in d) #prints True
print(1 not in d) #prints False
print("a" not in d) #True
#Toantu [Key]: return the value of a key
d = {1:"a",2:"b",3:"c"}
print(d[1]) #prints "a"
print(d[4]) #crash!
#Toan tu gan = : gan gia tri cho tu khoa tuong ung
d = {1:"a",2:"b",3:"c"}
print(d[1]) #a
d[1] = 42
print(d[1]) #prints 42
'''Cac ham tren dictionary'''
#Ham get(): get(key, value) returns the value of a key or id not exist in the dictionary returns default(None if Default is not work)
d = {1:"a",2:"b",3:"c"}
print(d.get(1)) #prints "a"   <=>tuong duong d[1]
print(d.get(1,42)) #default khong duoc dung  => return a
print(d.get(0)) #doesnt crash! No Errors  => return None
print(d.get(0,42)) #default khong duoc dung =>return 42
#Toan tu del: delete(key) delete a key from the dictionary
d = {1:"a",2:"b",3:"c"}
print(1 in d) #prints True
del d[1]
print(1 in d) #prints False
del d[1] #crash! Error
#Change the value of a key in a dictionary and Add a element
d2 = {1 : "QTM","qtm":"Difficult"}
d2['qtm'] ='Quantrimang'
print(d2) #prints {1: 'QTM', 'qtm': 'Quantrimang'}
d2[2]='Python'
print(d2) #prints {1: 'QTM', 'qtm': 'Quantrimang', 2: 'Python'}
#Return the list using items() or keys()
d = {1:"a",2:"b",3:"c"}
print(d) #prints {1:"a",2:"b",3:"c}
print(list(d.items())) #prints [(1, 'a'), (2, 'b'),(3, 'c')
print(list(d.keys())) #prints [1, 2, 3]
#Swap keys in a dictionary
dict = {'Tim': 18,'Charlie' : 12,'Tiffany' : 15}
student = list(dict.items())
student.sort() 
print(student) #prints ['Charlie','Tiffany','Tim']
for s in student:
     print(":".join(s,str(dict[s]))) #Charlie:18,Tiffany:15,Tim:18

#Update a dictionary:update()
d1 = {1:"a",2:"b",3:"c"}
d2 = {4:"d"}
d1.update(d2)
d2[5] = "e"
print(d1) #prints {1:"a",2:"b",3:"c",4:"d"}
print(d2) #prints {4:"d",5:"e"}
#Dictionary comprehension
lapphuong ={x : x*x*x for x in range(6)}
print(lapphuong) #prints {0: 0, 1: 1,2:8,3:27,4:64,5:125}
lapphuongchan ={x:x*x*x for x in range(10) if x % 2 ==0}
print(lapphuongchan) #prints {0: 0, 2: 8,4:64,6:216;8:512}
'''Change type of data in a dictionary'''
print(float(11)) #11.0
print(int(18.6)) #18
print(set([2,4,6])) #set({2,4,6})
print(tuple({3,5,7})) #(3,5,7)
print(list('hello')) #['h', 'e', 'l', 'l', 'o']
print(dict([[2,4],[1,3]])) #{'2': 4, '1': 3}
print(dict([(3,9),(4,16)])) #{'3': 9, '4': 16}




