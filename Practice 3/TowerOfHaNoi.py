def TowerHanoi(n, col1, col2, col3):
     if n == 1 :
          print("Move",col1,"qua",col3)
     else :
          TowerHanoi(n-1,col1,col3,col2)
          TowerHanoi(1,col1,col2,col3)
          TowerHanoi(n-1,col2,col1,col3)
n = int(input("Enter number n:"))
col1, col2, col3 = 1, 2 ,3
TowerHanoi(n,col1,col2,col3)