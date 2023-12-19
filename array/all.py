def particular(lis,par):
    print("The element in the position is:",lis[par-1])

def element_set(lis,x,y):
    print("The set of elements are")
    for i in range(x-1,y):
        print(lis[i],end=" ")

def display(lis,n):
    print("The elements are:")
    for i in range(n):
        print(lis[i],end=" ")
 
def max_min(lis,n):
    max = lis[0]
    min = lis[0]
     
    for i in range(n):
        if(max<lis[i]):
            max = lis[i]
            
    for i in range(n):
        if(min>lis[i]):
            min = lis[i]
    
    print("The maximun element from the array is",max)
    print("The minimum element from the array is",min)
    
def sum_avg(lis,n):
    sum = 0
    for i in range(n):
        sum = sum + lis[i]
        
    avg = sum/n
    print("The sum is",sum)
    print("The average is",avg)
    
def reverse(lis):
    print("The reversed elements are:")
    for i in range(n-1,-1,-1):
        print(lis[i],end=" ")

def rotate(lis,n,pos):
    temp = []
    for i in range(n):
        if(i>=pos):
            temp.append(lis[i])
            
    for i in range(n):
        if(i<pos):
            temp.append(lis[i])
            
    lis = temp
    return lis

def duplicate(lis,n):
    duplicate = []
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (lis[i] == lis[j]):
                duplicate.append(lis[i])
                count = count+1
    
    print("Number of duplicate elements are",count)
    print("The duplicate elements are:")
    for i in range(len(duplicate)):
        print(duplicate[i],end=" ")
        
def reversed_element(lis,n):
    reverse = []
    for i in range(n-1,-1,-1):
        reverse.append(lis[i])
        
    lis = reverse
    return lis 

lis = []
n = int(input("Enter the number of elements:"))
for i in range(n):
    a = int(input(f"Enter the element {i+1}:"))
    lis.append(a)

print("The elements are:")
for i in range(n):
    print(lis[i],end=" ")
   
while(True):
    
    choice = int(input("\nChoices:\n1.Print particular element in the position\n2.Print set of elements\n3.Print all the element\n4.Finding maximum and minimum element from the array\n5.Find sum and average\n6.print the reverse element\n7.Rotate the element position\n8.Print dupilacte elements\n9.Reverse the element\n10.Escape\nEnter the choice:"))
    if(choice == 1):
        par = int(input("Enter the position:"))
        particular(lis,par)
        
    elif(choice == 2):
        x = int(input("Enter the starting position:"))
        y = int(input("Enter the ending position:"))
        element_set(lis,x,y)
        
    elif(choice == 3):
        display(lis,n)
        
    elif(choice == 4):
        max_min(lis,n)
        
    elif(choice == 5):
        sum_avg(lis,n)
        
    elif(choice == 6):
        reverse(lis)
        
    elif(choice == 7):
        pos = int(input("Enter the position:"))
        lis = rotate(lis,n,pos)
        
    elif(choice == 8):
        duplicate(lis,n)
        
    elif(choice == 9):
        lis = reversed_element(lis,n)
        
    elif(choice == 10):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")