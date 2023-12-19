def enqueue(stack1,n):
    if(len(stack1) == n):
        print("Queue is full")
        
    else:
        element = int(input("Enter the element:"))
        stack1.append(element)
    
    return stack1
   
def dequeue(stack1,stack2,n):
    if(stack1 is None):
        print("Queue is empty")
        
    else:
        
        
stack1 = []
stack2 = []
n = int(input("Enter the size of the Queue:"))   

while(True):
    choice = int(input("\nEnter the choice 1.enqueue 2.dequeue 3.display 4.front 5.isempty 6.size 7.escape:"))
    if(choice == 1):
        queue = enqueue(stack1,n)
        
    elif(choice == 2):
        queue = dequeue(,n)
        
    elif(choice == 3):
        display()
        
    elif(choice == 4):
        front()
        
    elif(choice == 5):
        isempty()
        
    elif(choice == 6):
        size()
        
    elif(choice == 7):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")