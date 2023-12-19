class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class Doubly:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_begin(self,data):
        if(self.head is None):
            print("There is no element present in the doubly linked list,So the givern element is assigned as head element")
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
            
    def insert_middle(self,data):
        if(self.head is None):
            print("There is no element present in the doubly linked list,So the givern element is assigned as head element")
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

        else:
            position = int(input("Enter the position:"))
            new_node = Node(data)
            count = 1
            n= self.head
            
            while(n is not self.tail):
                count = count+1
                n = n.next
                
            if(count<position):
                print("Invalid position")
                
            elif(1 == position):
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                self.head.prev = self.tail
                self.tail.next = self.head
                
            else:
                n = self.head
                next_node = n.next
                count = 1
                while(count<position-1):
                    count = count + 1
                    n = n.next
                    next_node = next_node.next
                    
                n.next = new_node
                new_node.prev = n
                new_node.next = next_node
                next_node.prev = new_node
                    
    def insert_end(self,data):
        if(self.head is None):
            print("There is no element present in the doubly linked list,So the givern element is assigned as head element")
            new_node = Node(data)
            self.head = new_node
            self.tail = self.head
            
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
            
    def display(self):
        if(self.head is None):
            print("Doubly linked list is empty")
        
        else:
            n = self.head
            print("The elements in the Doubly linked list are")
            while(n is not self.tail):
                print(n.data,end=" ")
                n = n.next
            print(n.data)
            
    def delete_begin(self):
        if(self.head is None):
            print("Doubly linked list empty")
            
        else:
            count = 1
            n = self.head
            while(n is not self.tail):
                count = count+1
                n = n.next
            
            if(count == 1):
                self.head = self.tail = None
            
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
                
    def delete_middle(self):
        if(self.head is None):
            print("Doubly Linked list empty")
            
        else:
            position = int(input("Enter the position:"))
            count = 1
            n= self.head
            
            while(n is not self.tail):
                count = count+1
                n = n.next
                
            if(count<position):
                print("Invalid position")
            
            elif(1 == position):
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            
            elif(count == position):
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail

            else:
                n = self.head
                next_node = n.next
                count = 1
                while(count<position-1):
                    count = count + 1
                    n = n.next
                    next_node = next_node.next   
                
                next_node = next_node.next
                n.next = next_node
                next_node.prev = n
                
    def delete_end(self):
        if(self.head is None):
            print("Doubly linked list empty")
            
        else:
            count = 1
            n = self.head
            while(n is not self.tail):
                count = count+1
                n = n.next
            
            if(count == 1):
                self.head = self.tail = None
            
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
                
    def print_reverse(self):
        if(self.head is None):
            print("Doubly linked list empty")
        
        else:
            count = 1
            n = self.head
            while(n is not self.tail):
                count = count+1
                n = n.next
            
            if(count == 1):
                print("Only one element is present in the Doubly linked list:",self.head.data)
                
            else:
                n = self.tail
                print("The elements in the Doubly Linked list are")
                while(n is not self.head):
                    print(n.data,end=" ")
                    n = n.prev
                    
                print(n.data)
                
    def count(self):
        if(self.head is None):
            print("Doubly linked list empty")
        
        else:
            count = 1
            n = self.head
            
            while(n is not self.tail):
                count = count+1
                n = n.next
            
            print("Number of elements in the Doublt linked list:",count)
            
d = Doubly()
while(True):
    choice = int(input("\n1.Insert the element at beginning\n2.Insert the element at middle\n3.Insert the element at end\n4.Delete the element at beginning\n5.Delete the element at middle\n6.Delete the element at end\n7.print all elements\n8.print elements at reverse order using prev\n9.count\n10.escape\nEnter the choice:"))
    
    if(choice == 1):
        element = int(input("Enter the element:"))
        d.insert_begin(element)
    
    elif(choice == 2):
        element = int(input("Enter the element:"))
        d.insert_middle(element)
        
    elif(choice == 3):
        element = int(input("Enter the element:"))
        d.insert_end(element)
        
    elif(choice == 4):
        d.delete_begin()
        
    elif(choice == 5):
        d.delete_middle()
        
    elif(choice == 6):
        d.delete_end()
        
    elif(choice == 7):
        d.display()
        
    elif(choice == 8):
        d.print_reverse()
        
    elif(choice == 9):
        d.count()
        
    elif(choice == 10):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")