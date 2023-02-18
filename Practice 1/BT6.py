#Tìm tất cả các số chia hết cho 7 nhưng không phỉa bội sô của 5 nằm trong đoạn[[99,999]
a=[] #tao list
for i in range(99,1000):
    if(i % 7 == 0) and (i % 5 !=0):
        a.append(str(i)) #su dung appenf de them gia tri vua tim vao mang

print(','.join(a)) #su dung join de ket hop chuoi
