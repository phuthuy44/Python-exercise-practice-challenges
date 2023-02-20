#Nhập một số nguyên, đếm xem số đó có bao nhiêu chữ số và tính tổng các chữ số
def demsonguyen():
    #n = int(input("Enter interger a:"))
    count = 0
    s = 0
    while True :
        try :
            n = int(input("Enter interger a:"))
            if n <= 0 :
                print("Error: N must be bigger than 0")
                continue
            while (n > 0):
                s += n%10
                n = int(n/10)
                count += 1
            print("Co :",count)
            print("Tong cac chu so la:",s)
            break
        except ValueError :
            print("Error: N must be bigger than 0!2")
    ''''if (n <= 0):
        print("Error: N must be bigger than 0")
        n=int(input("Eter another number :"))
        # Adding the digits of a number.
        while(n > 0):
            s += n%10
            n = int(n/10)
            count += 1
        print("Co :",count)
        print("Tong cac chu so la:",s)
    else :
        while(n > 0):
            s += n%10
            # Dividing the number by 10 and then converting it to an integer.
            n = int(n/10)
            count += 1
        print("Co :",count)
        print("Tong cac chu so la:",s)'''
            

demsonguyen()




