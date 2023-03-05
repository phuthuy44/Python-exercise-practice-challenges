'''Phan A'''
#Cau 2 :
print("========Cau 2========")
d = {'b':200,'a':100, 'c':1}
print(d['a'])
print(d.get('e',None))
print(len(d))
print(d.keys())
print(d.values())
print(d.pop('b'))
print(d.values())
print("\n")
#Cau 3:
print("========Cau 3========")
d = {'b':200,'a':100, 'c':1}
d["b"] = -200
print("Thay the gia tri cua khoa b thanh so am tuong ung :",d)
d["e"] = 500
print("Them mot khoa 'e' co gia tri 500 vao tu dien :",d)
del d["b"]
print("Xoa khoa b ra khoi tu dien(theo cach an toan):",d)
dic = list(d.items())
dic.sort()
for i,value in dic:
    print(" {} : {} ".format(i,value), end="  ")
