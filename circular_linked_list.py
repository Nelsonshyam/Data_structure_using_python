class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_begin(self,data):
        if(self.head is None):
            print("There is no element present in the Circular list, So the given element is assigned as head element")
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            
    def insert_end(self,data):
        if(self.head is None):
            print("There is no element present in the Circular list, So the given element is assigned as head element")
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def insert_middle(self,data):
        if(self.head is None):
            print("There is no element present in the Circular list, So the given element is assigned as head element")
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            
        else:
            position = int(input("Enter the position:"))
            count = 1
            n = self.head
            while(count != position and n is not self.tail):
                count = count+1
                n = n.next
                
            if(count<position):
                print("Invalid position")
                
            elif(1 == position):
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
                
            else:
                new_node = Node(data)
                count = 1
                n = self.head
                next_node = n.next
                
                while(count < position-1 and n is not self.tail):
                    count = count+1
                    n = n.next
                    next_node = next_node.next
                
                n.next = new_node
                new_node.next = next_node
                
    def delete_begin(self):
        if(self.head is None):
            print("There is no element in the Circular Linked list")
            
        else:
            n = self.head
            count = 1
            while(n.next is not None):
                count = count+1
                n.next
                
            if(count == 1):
                self.head = None
                self.tail = None
                
            else:
                temp = self.head
                self.head = self.head.next
                self.tail.next = self.head
                temp = None
                
    def delete_end(self):
        if(self.head is None):
            print("There is no element in the Circular linked list")
            
        else:
            n = self.head
            count = 1
            
            while(n.next is not None):
                count = count+1
                n = n.next
                
            if(count == 1):
                self.head = None
                self.tail = None
                
            else:
                temp = self.head
                while(temp.next is not self.tail):
                    temp = temp.next
                    
                temp.next = self.head
                self.tail = None
                self.tail = temp    
    
    def delete_middle(self):
        if(self.head is None):
            print("There is no element in the Circular linked list")
            
        else:
            position = int(input("Enter the position which you want to delete:"))
            n = self.head
            count = 1
            if(position == count):
                self.head = self.head.next
                
            else:
                while n is not self.tail and count < position-1:
                    n = n.next
                    count = count + 1

                if n is self.tail or n.next is self.tail:
                    print("Invalid position entered")
                    
                else:
                    n.next = n.next.next
            
    def display(self):
        if(self.head is None):
            print("There is no element in the Circular linked list")
            
        else:
            n = self.head
            print("The element in circular list:")
            
            while(n is not self.tail):
                print(n.data,end=" ")
                n = n.next
            print(n.data)
            
    def count(self):
        count = 0
        n = self.head
        
        if(n is None):
            print("The Linked list is empty")
            
        else:
            while(n is not self.tail):
                count = count+1
                n = n.next
                
            print(f"There are {count+1} element present in ths Circular list")
        
cl = Circular_list()           

while(True):
    choice = int(input("\nChoices:\n1.Insert at Beginning\n2.Insert at End\n3.Insert at Middle\n4.Display the elements\n5.Delete at beginning\n6.Delete at end\n7.Delete at middle\n8.Count the elements from the circular linked list\n9.Escape\nEnter the choice:"))
    
    if(choice == 1):
        element = int(input("Enter the element:"))
        cl.insert_begin(element)
        
    elif(choice == 2):
        element = int(input("Enter the element:"))
        cl.insert_end(element)
        
    elif(choice == 3):
        element = int(input("Enter the element:"))
        cl.insert_middle(element)
        
    elif(choice == 4):
        cl.display()
        
    elif(choice == 5):
        cl.delete_begin()
        
    elif(choice == 6):
        cl.delete_end()
        
    elif(choice == 7):
        cl.delete_middle()
        
    elif(choice == 8):
        cl.count()
        
    elif(choice == 9):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")    
            
            
