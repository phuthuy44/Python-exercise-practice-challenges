'''Phan B'''
import numpy as np
def Mang2Chieu():
     def Cau1():
          n = int(input("Enter n:"))
          matrix = []
          # Creating a matrix of size n x n.
          for i in range(n):
               row = []
               for j in range(n):
                    # Checking if the current index is on the edge of the matrix.
                    if i == 0 or i == n-1 or j == 0 or j == n-1 :
                         row.append(1)
                    else:
                         row.append(0)
               matrix.append(row)
          # Printing the matrix.
          for i in range(n):
               for j in range(n):
                    print(matrix[i][j],end = " ")
               print()
     def Cau2():
          matrix = np.random.randint(1,10, size=(3,5))
          print(matrix)
          def Cau2a():
               row_sums = []
               for row in matrix:
                    row_sum = sum(row)
                    row_sums.append(row_sum)
               print("Sum of rows:",row_sums )
               col_sums = []
              # Summing the columns of the matrix.
               # Iterating through the columns of the matrix.
               ## `matrix[0]` is the first row of the matrix.
               for i in range(len(matrix[0])): # `len(matrix[0])` is the number of columns in the matrix.
                    col_sum = 0
                    # Iterating through the rows of the matrix.
                    for j in matrix :
                         col_sum += j[i]
                    col_sums.append(col_sum)
               print("Sum of columns :", col_sums)
          def Cau2b():
               max_row = [max(row) for row in matrix]
               min_row = [min(row) for row in matrix]
               print("Max row :",max_row)
               print("Min row :",min_row)
          def Cau2c():
               even = []
               odd = []
               for row in matrix:
                    for num in row:
                         if num %2 == 0:
                              even.append(num)
                         else:
                              odd.append(num)
               print("even :",even)
               print("odd :",odd)
          def Cau2d():
               #Để tính trung bình cộng các cột có chỉ số chẵn, chúng ta sử dụng vòng lặp for với bước nhảy là 2 để duyệt qua các cột có chỉ số chẵn, và tính trung bình cộng bằng cách chia tổng cho số lượng phần tử trong cột.
               cold_avg = []
               for j in range(0,len(matrix[0]),2):
                    cold_avg.append(sum(matrix[i][j] for i in range(len(matrix)))/len(matrix))
               print("Average:",cold_avg)
          def Cau2e():
               even_num = 0
               for i in range(len(matrix)):
                    for j in range(len(matrix[0])):
                         if i % 2==0 and j % 2==0:
                              even_num = even_num + matrix[i][j]
               print("Sum:",even_num)
          def Cau2f():
               range_row =[max(row) - min(row) for row in matrix]
               print("Range:",range_row)
          def Cau2a_Numpy():
               sum_rows= np.sum(matrix,axis =1)
               print("Sum of rows :",sum_rows)
               sum_cols= np.sum(matrix,axis =0)
               print("Sum of columns :",sum_cols)
          def Cau2b_Numpy():
               max_rows= np.max(matrix,axis =1)
               max_cols= np.max(matrix,axis =0)
               print("Max of rows :",max_rows)
               print("Max of cols :",max_cols)
               min_rows= np.min(matrix,axis =1)
               min_cols= np.min(matrix,axis =0)
               print("Min of rows :",min_rows)
               print("Max of rows :",min_cols)
          def Cau2c_Numpy():
               even = matrix[matrix % 2 == 0]
               print("Even of matrix:",even)
               odd = matrix[matrix % 2 == 1]
               print("Even of matrix:",odd )
          def Cau2d_Numpy():
               cols =[0,2,4]
               # `matrix[:,cols]` is selecting the columns of the matrix.
               avg_cols = np.mean(matrix[:,cols],axis = 0) # `mean` is calculating the average of the elements in the matrix.
               print("Average of colums only have [0,2,4]:",avg_cols)
          def Cau2e_Numpy():
               even = []
               for i in range(3):
                    for j in range(5):
                         if i % 2 == 0 and j % 2 == 0:
                              even.append((i,j))
               # `matrix[[i for i, j in even]]` is selecting the rows of the matrix.
               even_sum = np.sum(matrix[[i for i, j in even], [j for i, j in even]])
               print("Sum of all elements have slicing is even:", even_sum)
          def Cau2f_Numpy():
               range_rows = np.max(matrix,axis=1) -np.min(matrix,axis=1)
               print("Range of max values and min values are:", range_rows)      
          Cau2a_Numpy()
          Cau2b_Numpy()
          Cau2c_Numpy()
          Cau2d_Numpy()
          Cau2e_Numpy()
          Cau2f_Numpy()
          Cau2a()
          Cau2b()
          Cau2c()
          Cau2d()
          Cau2e()
          Cau2f()
     def Cau3():
          matrix = np.random.randint(0,10, size=(5,5))
          print(matrix)
          def Cau3a():
               sum = 0
               for i in range(5):
                    sum += matrix[i][i]
               print("Sum the elements on the main diagonal:", sum)
               for i in range(5):
                    sum += matrix[i][4-i] # `matrix[i][4-i]` is selecting the elements on the diagonal.
               print("Sum the elements on the sec diagonal:", sum)
          def Cau3b():
               max_main = max(matrix[i][i] for i in range(5) )
               min_main = min(matrix[i][i] for i in range(5))
               print("Max and min on the main diagonal:{},{}".format(max_main,min_main))
               max_sec = max(matrix[i][4-i] for i in range(5))
               min_sec = min(matrix[i][4-i] for i in range(5))
               print("Max and min on the sec diagonal:{},{}".format(max_sec,min_sec))
          def Cau3a_Numpy():
               sum_main = np.trace(matrix)
               sum_sec = np.trace(np.fliplr(matrix))
               print("Sum of all elements on the main diagonal:", sum_main)
               print("Sum of all elements on the sec diagonal:", sum_sec)
          def Cau3b_Numpy():
               max_main = np.max(np.diag(matrix))
               min_main = np.min(np.diag(matrix))
               print("Max and min of all elements on the main diagonal:{},{}".format(max_main, min_main))
               max_sec = np.max(np.diag(np.fliplr(matrix)))
               min_sec = np.min(np.diag(np.fliplr(matrix)))
               print("Max and min of all elements on the sec diagonal :{},{}".format(max_sec, min_sec))
                                
          Cau3a()
          Cau3b()
          Cau3a_Numpy()
          Cau3b_Numpy()

     Cau1()
     Cau2()
     Cau3()
Mang2Chieu()