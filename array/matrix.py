def sum():
    matrix1 = []
    print("Enter for matrix 1")
    row1 = int(input("Enter the number of rows:"))
    column1 = int(input("Enter the number of columns:"))

    for i in range(row1):
        a = []
        for j in range(column1):
            element = int(input(f"Enter the row {i+1} and column {j+1}:"))
            a.append(element)
        matrix1.append(a)
    
    matrix2 = []
    print("Enter for matrix 2")
    row2 = int(input("Enter the number of rows:"))
    column2 = int(input("Enter the number of columns:"))

    for i in range(row2):
        a = []
        for j in range(column2):
            element = int(input(f"Enter the row {i+1} and column {j+1}:"))
            a.append(element)
        matrix2.append(a)
    
    print("Matrix 1:")
    for i in range(row1):
            for j in range(column1):
                print(matrix1[i][j],end=" ")
            print("")
    
    print("Matrix 2:")
    for i in range(row2):
            for j in range(column2):
                print(matrix2[i][j],end=" ")
            print("")
            
    if((row1 == row2) and (column1 == column2)):
        matrix3 = []
        
        for i in range(row1):
            a = []
            for j in range(column1):
                a.append((matrix1[i][j]+matrix2[i][j]))
            matrix3.append(a)  
              
        print("The sum of matrix:")
        for i in range(row1):
            for j in range(column1):
                print(matrix3[i][j],end=" ")
            print("")
            
    else:
        print("Dimensions are not same for the matrices")

def multiply():
    matrix1 = []
    print("Enter for matrix 1")
    row1 = int(input("Enter the number of rows:"))
    column1 = int(input("Enter the number of columns:"))

    for i in range(row1):
        a = []
        for j in range(column1):
            element = int(input(f"Enter the row {i+1} and column {j+1}:"))
            a.append(element)
        matrix1.append(a)
    
    matrix2 = []
    print("Enter for matrix 2")
    row2 = int(input("Enter the number of rows:"))
    column2 = int(input("Enter the number of columns:"))

    for i in range(row2):
        a = []
        for j in range(column2):
            element = int(input(f"Enter the row {i+1} and column {j+1}:"))
            a.append(element)
        matrix2.append(a)
    
    print("Matrix 1:")
    for i in range(row1):
            for j in range(column1):
                print(matrix1[i][j],end=" ")
            print("")
    
    print("Matrix 2:")
    for i in range(row2):
            for j in range(column2):
                print(matrix2[i][j],end=" ")
            print("")
        
    if(column1 == row2):
        matrix3 = []
        
        for i in range(row1):
            a = []
            for j in range(column2):
                sum_value = 0
                for k in range(column1):
                    sum_value += matrix1[i][k] * matrix2[k][j]
                a.append(sum_value)
            matrix3.append(a)
        
        print("Multiplied Matrix:")
        for i in range(row1):
            for j in range(column2):
                print(matrix3[i][j],end=" ")
            print(" ")
            
    else:
        print("Dimensions are not equal for multiple the given matrices")
        
def inverse():
    matrix = []
    
    print("Enter the matrix elements")
    row = int(input("Enter the number of rows:"))
    column = int(input("Enter the number of columns:"))

    for i in range(row):
        a = []
        for j in range(column):
            element = int(input(f"Enter the row {i+1} and column {j+1}:"))
            a.append(element)
        matrix.append(a)
        
    inverse_matrix = []
    
    for i in range(len(matrix[0])):
        a = []
        for j in range(len(matrix)):
            a.append(matrix[j][i])
        inverse_matrix.append(a)
        
    print("Original Matrix:")  
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print("")
    
    print("Inversed Matrix:")   
    for i in range(len(inverse_matrix)):
        for j in range(len(inverse_matrix[0])):
            print(inverse_matrix[i][j],end=" ")
        print("")
        
while(True):
    choice = int(input("Choices:\n1.sum the matrix\n2.multiply the matirx\n3.Inverse\n4.Escape\nEnter the choice:"))
    if(choice == 1):
        sum()
        
    elif(choice == 2):
        multiply()
        
    elif(choice == 3):
        inverse()
        
    elif(choice == 4):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")