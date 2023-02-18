#Tìm số đầu tiên chia hết cho 9 và chia hết cho 7 nằm trong đoạn [M,N]
m = int(input("Enter m:"))
n = int(input("Enter n:"))
a = []
def lietke(m,n):
    for i in range(m,n+1):
        if i % 9 == 0 and i % 7 == 0:
        # Appending the string representation of `i` to the list `a`.
            a.append(str(i))
            #print("Số đầu tiên chia hết cho 9 và chia hết cho 7 là :",i)
    if not a:
        print('Khong co so thoa man')
    else:
        print("["," , ".join(a),"]")
        print("Số đầu tiên chia hết cho 9 và chia hết cho 7 là :",a[0])

        
lietke(m,n)
