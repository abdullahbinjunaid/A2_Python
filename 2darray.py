#list of list

#initialisation
#method 1
arr1 = [[1,2,3],[4,5,6],[7,8,9]]
print(arr1)

#method 2
col = 3
row = 3         #column                #row         
arr2 = [[0 for j in range(col)] for i in range(row)] #declaration of row and column
#print(arr2)

#accessing elements
print(arr1[0][0]) #[row][column]
 
#Traversing

#method 1
for row in arr1: #going in each row
    for value in row: #going to each column, or you can say for each row all values are being addressed
        print(value, end=" ")
 
print("\n", end = "")       
#method 2
  #Row
for i in range(len(arr1)):
       #column     #len(arr(row))
    for j in range(len(arr1[i])):
        print(arr1[i][j], end = " ")
print("\n", end = "")         

#adding a new row 
arr1.append([10,11,12])

newcol = [100,200,300,400]
for i in range(len(arr1)):
    arr1[i].append(newcol[i])
    
for i in range(len(arr1)):
       #column     #len(arr(row))
    for j in range(len(arr1[i])):
        print(arr1[i][j], end = " ")
