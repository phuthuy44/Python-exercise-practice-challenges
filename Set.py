s = set([2,3,5])
print(3 in s) #print True 
print(4 in s) #print False
for x in range(7):
    if x not in s :
        print(x) #print 0 1 4 6
'''Creating a set'''
s = set()
print(s) #print set()
'''Create a set from a list'''
s = set(["Cat","cow","dog"])
print(s) # set(["Cat","cow","dog"])
'''Create a set form object'''
s = set("wahoo")
print(s) # set(["w","a","h","o"])

s = {2,3,5}
print(s) #set([2,3,5])
ss = {1,2,1,5,4,2,3,6,4,5}
print(ss) #set([1,2,5,4,3,6}
# {}: is not an empty set
s = {}
print(type(s) == set) #False 
print(type(s)) #This is a dictionary => <class 'dict'>

#Vi set la tap hop cac phan tu khong co thu tu nen chi muc cha co y nghia gi voi set. Do do toan tu cat [] se ko lam viec tren set
s = set([2,4,8])
print(s) #set([2,4,8])
for i in s :
    print(i) # 2 4 8 
print(s[0]) #Error
print(s[:3]) #Error
#Cac phan tu la duy nhat(ko turng nhau)
s = set([2,2,2])
print(s) #set([2,2,2])
print(len(s)) #1
#Set khong the chua phan tu cos the thay doi duoc nhu list hay tuple
a = ["lists","are","mutable"]
s = [a]
print(" s :",s) #s : [lists,are,mutable]
s1 = set(a)
print(" s1 :",s1) #s1 : set({lists,are,mutable})
s2 = set([a]) #Error : khong the tao set
print(" s2 :",s2) #Error : khong the tao set

'''Set thi hieu qua hon list: Set dung co che ham bam(hasing) de kiem tra su ton tai cua phan tu '''
import time 
n = 500 
#1. Create a list [2,4,6,...,n] then check for membership #among[1,2,3,...n] in that list. Dont count thee list creation in the timing
a = list(range(2,n+1,2))
print("Using a list:",end = " ")
start = time.time()
count = 0 
for x in range(n+1):
    if x in a :
        count += 1
end = time.time()
elapsed1 = end - start
print("count = ",count,"and time %0.4f seconds" %elapsed1)
#2. Repeat, using a set 
print("Using a set:",end = " ")
start = time.time()
s = set(a)  
count = 0
for x in range(n+1):
     if x in s:
         count += 1
end = time.time()
elapsed2 = end - start
print("count = ",count,"and time %0.4f seconds" %elapsed1)
print("With n = %d, sets ran about %0.1f times faster than lists"%(n,elapsed1/elapsed2))
print("Try a larger n to see an even greater saving!")
#Output : Using a list... count = 250 and time = 2.5040 seconds
#         Using a set... count = 250 and time = 0.1520 seconds
#         With n = 500, sets ran about 16.5 times faster than lists
#         Try a larger n to see an even greater saving!
'''Kich thuoc cua set :len()'''
s = {2,3,2,4,3}
print(len(s)) #4
'''Cop set:copy()'''
s ={1,2,3}
t = s.copy()
s.add(4)
print(s) #set([1,2,3,4])
print(t) #set([1,2,3,3])
'''Xoa set:clear()'''
s = {1,2,3}
s.clear()
print(s,len(s)) #set(), 0
'''Cac phep toan tren set va phan tu trong set'''
#Toan tu : in and not in
s = {1,2,3}
print( 0 in s) #False
print(1 in s) #True
#Them phan tu : add()
s = {1,2,3}
print(s, 4 in s) #set({1,2,4}) False 
s.add(4)
print(s, 4 in s) #set({1,2,3,4}) True
#Xoa phan tu : remove() vs discard()
s = {1,2,3}
print(s, 3 in s) #set({1,2,3}) True
s.remove(3)
print(s, 3 in s) #set({1,2}) False
s.remove(3) #crashes; Error

s = {1,2,3}
print(s, 3 in s) #set({1,2,3}) True
s.discard(3)
print(s, 3 in s) #set({1,2}) False
s.discard(3) #does not crash; No Error
print(s, 3 in s) #set({1,2 }) False
'''Cac phep toan tren 2 sets'''
#s.issubset(t) tuong duong s <= t
print({1,2} <= {1},{1,2}.issubset({1})) #False False
print({1,2} <= {1,2},{1,2}.issubset({1,2})) #True True
print({1,2} <= {1,2,3},{1,2}.issubset({1,2,3})) #True True
#s.issuperset(t) tuong duong s >= t
print({1,2} >= {1},{1,2}.issuperset({1})) #True True
print({1,2} >= {1,2},{1,2}.issuperset({1,2})) #True True
print({1,2} >= {1,2,3},{1,2}.issuperset({1,2,3})) #False False
#s.union(t) tuong duong s| t
print({1,2} | {1},{1,2}.union({1})) #set({1, 2}) set({1, 2})
print({1,2} | {1,3},{1,2}.union({1,3})) #set({1, 2, 3}) set({1, 2, 3})
s = {1,2}
t = s | {1,3}
print(s,t) #set({1, 2}) set({1, 2, 3})
#s.difference(t) tuong duong s- t
print({1,2} - {1},{1,2}.difference({1})) #set({2}) set({2})
print({1,2} - {1,3},{1,2}.difference({1,3})) #set({2}) set({2})
s = {1,2}
t = s - {1,3}
print(s,t) #set({1, 2}) set({1, 2})
#s.symmetric_difference(t) tuong duong s^ t
a = {1,2,3,4,5}
b ={4,5,6,7,8}
print(a^b) #{1,2,3,6,7,8}
print(a.symmetric_difference(b)) #{1,2,3,6,7,8
#s.update(t) tuong duong s |= t
s = {1,2}
t ={1,3}
u = {2,3}
s.update(u)
t |= u
print(s,t,u) #set({1, 2, 3}) set({1, 3,2}) set({2, 3})
'''Set chua cac phan tu khong theo thu tu'''
s1 = [1,2,3]
s2 = [3,2,1]
print(s1 == s2) #False
t1 = set(s1)
t2 = set(s2)
print(t1 == t2) #True




