def push(lis,n):
    element = int(input("Enter the element:"))
    if(lis is None):
        lis.append(element)
        
    elif(len(lis)==n):
        print("Stack is full")
        
    elif(len(lis)!=n):
        lis.append(element)
        
    return lis

def pop(lis,n):
    if(lis is None):
        print("Stack is empty")
        
    elif(len(lis)==n):
        del lis[n-1]
        
    elif(len(lis)!=n):
        del lis[(len(lis)-1)]
        
    return lis

def peek(lis):
    if(lis is None):
        print("Stack is empty")
        
    elif(len(lis)==n):
        print(lis[n-1])
        
    elif(len(lis)!=n):
        print(lis[len(lis)-1])
        
def show(lis):
    if(lis is None):
        print("Stack is empty")
        
    elif(len(lis)==n):
        for i in range(n-1,-1,-1):
            print(lis[i],end=" ")
            
    elif(len(lis)!=n):
        for i in range(len(lis)-1,-1,-1):
            print(lis[i])
            
def isempty(lis):
    if(lis is None):
        print("Stack is empty")
        
    elif(len(lis)==n):
        print("Stack is Full")
        
    elif(len(lis)!=n):
        print("Some value has present")
        
def size(lis):
    print("The number of elements in the stack:",len(lis))

lis = []

n = int(input("Enter the stack size:"))
while(True):
    choice = int(input("\nEnter the choice 1.Push 2.Pop 3.peek 4.Show 5.isempty 6.size 7.escape:"))
    
    if(choice == 1):
        lis = push(lis,n)
        
    elif(choice == 2):
        lis = pop(lis,n)
        
    elif(choice == 3):
        peek(lis)
        
    elif(choice == 4):
        show(lis)
        
    elif(choice == 5):
        isempty(lis)
        
    elif(choice == 6):
        size(lis)
        
    elif(choice == 7):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")