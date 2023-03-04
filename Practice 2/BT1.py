'''Phan A'''
#Cau 1
print("================Cau 1================")
l= [2,4,9,3,5]
print(l[2])
print(l[-1])
print(len(l))
print(l[0:2])
print( 0 in l)
print(l + [24,1,4])
print(tuple(l))
print("\n")
print("================Cau 2================")
#Cau 2
l = [2,4,9,3,5]
print("List:",l)
l[0]= -2
print("Thay the phan tu dau tien:",l)
l = l + [20]
print("Them 20 vao cuoi danh sach:",l)
l.insert(3,0)
print("Them so 0 vao vi tri so 3 trong danh sach:",l)
del l[4]
print("Xoa phan tu tai vi tri so 4 torgn dnah sach:",l)
l = l + [0,0,0]
print("Them list[0,0,0] vao danh sach tren:",l)
l.sort(reverse=True)
print("Sap xep danh sach giam dan:",l)
