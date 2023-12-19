class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        if(self.top is None):
            new_node = Node(data)
            self.top = new_node
            
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
            
    def pop(self):
        if(self.top is None):
            print("The stack is empty")
            
        else:
            self.top = self.top.next 
            
    def peek(self):
        if(self.top is None):
            print("The stack is empty")
            
        else:
            print("The peek element is",self.top.data)
            
    def show(self):
        if(self.top is None):
            print("The stack is empty")
            
        else:
            n = self.top
            print("The elements in the stack are")
            
            while(n is not None):
                print(n.data,end = " ")
                n = n.next
    
    def isempty(self):
        if(self.top is None):
            print("The stack is empty")
            
        else:
            print("Something element is present in the stack")
            
    def size(self):
        if(self.top is None):
            print("The stack is empty")
            
        else:
            n = self.top
            count = 1
            
            while(n.next is not None):
                count = count+1
                n = n.next
            print("The number elements present in the stack are",count)
        
s = Stack()
    
while(True):
    choice = int(input("\nEnter the choice 1.Push 2.Pop 3.peek 4.Show 5.isempty 6.size 7.escape:"))
    if(choice == 1):
        element = int(input("Enter the element:"))
        s.push(element)
        
    elif(choice == 2):
        s.pop()
        
    elif(choice == 3):
        s.peek()
        
    elif(choice == 4):
        s.show()
        
    elif(choice == 5):
        s.isempty()
        
    elif(choice == 6):
        s.size()
        
    elif(choice == 7):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")