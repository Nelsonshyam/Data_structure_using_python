def enqueue(queue,n):
    element = int(input("Enter the element:"))
    
    if(queue is None):
        queue.append(element)
        
    elif(len(queue) == n):
        print("Queue is Full")
        
    else:
        queue.append(element)
        
    return queue

def dequeue(queue,n):
    if(queue is None):
        print("Queue is empty")
        
    elif(len(queue) == n):
        del queue[0]
        
    else:
        del queue[0]
        
    return queue

def display(queue):
    if(queue is None):
        print("The queue is empty")
        
    else:
        print("The Queue list:")
        for i in range(len(queue)):
            print(queue[i],end=" ")
            
def front(queue):
    if(queue is None):
        print("Queue is empty")
        
    else:
        print(queue[0])
        
def isempty(queue):
    if(queue is None):
        print("Queue is Empty")
        
    elif(len(queue)==n):
        print("Queue is full")
        
    else:
        print("Something element is present")
        
def size(queue):
    if(queue is None):
        print("Queue is empty")
        
    else:
        print("The size is",len(queue))
        
queue = []
n = int(input("Enter the size of the Queue:"))

while(True):
    choice = int(input("\nEnter the choice 1.enqueue 2.dequeue 3.display 4.front 5.isempty 6.size 7.escape:"))
    if(choice == 1):
        queue = enqueue(queue,n)
        
    elif(choice == 2):
        queue = dequeue(queue,n)
        
    elif(choice == 3):
        display(queue)
        
    elif(choice == 4):
        front(queue)
        
    elif(choice == 5):
        isempty(queue)
        
    elif(choice == 6):
        size(queue)
        
    elif(choice == 7):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")