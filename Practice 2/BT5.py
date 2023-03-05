def BT5() :
     n = int(input("Enter n elements in list:"))
     a = []
     for i in range(0,n) :
          x = int(input("Enter element %d :"%(i+1)))
          a.append(x)
     print("List a:",a)
     def EX1():
          sum = 0
          for i in range(0,n) :
               sum += a[i]
          print("Sum of elements in list a:",sum)
     def EX2():
          count = 0
          sum = 0
          for i in range(0,n) :
               if a[i] > 0 :
                    count += 1
                    sum += a[i]
          print("Co {} number larger than 0".format(count))
          print("Sum of elements > 0 in list a:",sum)
     def EX3():
          average = 0
          sum = 0
          for i in range(0,n) :
               sum += a[i]
               average = sum/n
          print("Average of elements in list a:",average)
          for i in range(0,n) :
               if a[i] > 0 :
                    sum += a[i]
                    average = sum/n
          print("Sum of elements in list a:",average)
     def EX4():
          i = 0
          while a[i] >= 0:
               i += 1
               if i == n :
                    break
          if i == n :
               print("No negative element")
          else :
               print("Position of the first negative element:",i+1)
     def EX5():
          i = n-1
          while a[i] < 0:
               i -= 1
               if i == -1 :
                    break
          if i == -1 :
               print("No element")
          else :
               print("Position of the last positive element:",i+1)
     def EX6():
          max = a[0]
          positive = 0
          for i in range(1,n-1):
               if a[i] > max:
                    max = a[i]
                    positive = i
          print("Max of elements in list a:",max)
          print("Position of the max element:",positive+1)
     EX1()
     EX2()
     EX3()
     EX4()
     EX5()
     EX6()
BT5()
