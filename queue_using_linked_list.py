class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        
    def enqueue(self,data):
        if(self.rear is None and self.front is None):
            new_node = Node(data)
            self.front = new_node
            self.rear = self.front
            
        else:
            new_node = Node(data)
            n = self.front
            
            while(n is not self.rear):
                n = n.next
                
            n.next = new_node
            self.rear = new_node
            
    def dequeue(self):
        if(self.rear is None and self.front is None):
            print("There is no element present in the queue")
            
        else:
            count = 1
            n = self.front
            
            while(n is not self.rear):
                count = count+1
                n = n.next
                
            if(count == 1):
                self.front = self.rear = None
                
            else:
                self.front = self.front.next
            
    def display(self):
        if(self.rear is None and self.front is None):
            print("There is no element present in the queue")
            
        else:
            n = self.front
            print("The elements in the queue are")
            
            while(n is not self.rear):
                print(n.data,end=" ")
                n = n.next
                
            print(n.data)
            
    def first(self):
        if(self.rear is None and self.front is None):
            print("There is no element present in the queue")
            
        else:
            print("The front of the queue is",self.front.data)
            
    def isempty(self):
        if(self.rear is None and self.front is None):
            print("There is no element present in the queue")
            
        else:
            print("There is some element present in the queue")
            
    def size(self):
        if(self.rear is None and self.front is None):
            print("There is no element present in the queue")
            
        else:
            count = 1
            n = self.front
            
            while(n is not self.rear):
                count = count+1
                n = n.next

            print("The number of elements present in the queue is",count)
            
q = Queue()
while(True):
    choice = int(input("\nEnter the choice 1.enqueue 2.dequeue 3.display 4.front 5.isempty 6.size 7.escape:"))
    
    if(choice == 1):
        element = int(input("Enter the element:"))
        q.enqueue(element)
        
    elif(choice == 2):
        q.dequeue()
        
    elif(choice == 3):
        q.display()
        
    elif(choice == 4):
        q.first()
        
    elif(choice == 5):
        q.isempty()
        
    elif(choice == 6):
        q.size()
        
    elif(choice == 7):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")