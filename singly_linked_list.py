class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None:
            print("List is empty")
            
        else:
            print("The elements in the Linked list:")
            n = self.head
            
            while(n is not None):
                print(n.data,end=" ")
                n = n.next
                
    def insert_begin(self,data):
        if(self.head is None):
            print("There is no element is present in the Linked list, so your element has been assigned as a head element")
            new_node = Node(data)
            self.head = new_node
            
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def insert_middle(self,data):
        count = 0
        n = self.head
        
        while(n is not None):
           count = count+1
           n = n.next 
           
        if(self.head is None):
            print("There is no element is present in the Linked list, so your element has been assigned as a head element")
            new_node = Node(data)
            self.head = new_node
            
        elif(count == 1):
            print("There is only one element is present in the Linked list, so your element will be assign as 2nd element")
            new_node = Node(data)
            self.head.next = new_node
            
        else:
            position = int(input("Enter the position you want:"))
            
            if(count<position-1):
                print("Invalid position entered")
                
            elif(position==1):
                new_node = Node(data)
                new_node.next = self.head
                self.head = new_node
                
            else:
                n = self.head
                count = 1
                
                while(count != position-1 and n.next is not None):
                    n = n.next
                    count = count+1
                    
                new_node = Node(data)
                
                new_node.next = n.next
                n.next = new_node
    
    def insert_after(self,data):
        n = self.head
        count = 0
        
        while(n is not None):
            count = count+1
            n = n.next
            
        if(self.head is None):
            print("There is no element is present in the Linked list, so your element has been assigned as a head element")
            new_node = Node(data)
            self.head = new_node
            
        elif(count == 1):
            print("Only one element is present in the Linked list, So the given element will be assigned as a 2nd element")
            new_node = Node(data)
            self.head.next = new_node
            
        else:
            position = int(input("Enter the postion:"))
            new_node = Node(data)
            n = self.head
            count = 0
            
            while(n is not None):
                count = count+1
                n = n.next

            if(count < position-1):
                print("Invalid position entered")
            
            else:  
                n = self.head
                count = 1
                
                while(count != position):
                    n = n.next
                    count = count+1
                    
                new_node.next = n.next
                n.next = new_node
                
    def insert_end(self,data):
        if(self.head is None):
            print("There is no element is present in the Linked list, so your element has been assigned as a head element")
            new_node = Node(data)
            self.head = new_node
            
        else:
            n = self.head
            new_node = Node(data) 
               
            while(n.next is not None):
                n = n.next
            n.next = new_node
            
    def delete_begin(self):
        if(self.head is None):
            print("There is no element present in the Linked list")
            
        else:
            self.head = self.head.next
            
    def delete_middle(self):
        if self.head is None:
            print("There is no element present in the Linked list")
            
        else:
            position = int(input("Enter the position which you want to delete:"))
            n = self.head
            count = 1
            
            if(position == count):
                self.head = self.head.next
                
            else:
                while n is not None and count < position-1:
                    n = n.next
                    count = count + 1

                if n is None or n.next is None:
                    print("Invalid position entered")
                    
                else:
                    n.next = n.next.next
                                       
    def delete_end(self):
        if(self.head is None):
            print("There is no element present in the Linked list")
            
        elif(self.head.next is None):
            self.head = None
            
        else:
            n = self.head
            
            while(n.next.next is not None):
                n = n.next
                
            n.next = None

    def count(self):
        count = 0
        n = self.head
        
        if(n is None):
            print("The Linked list is empty")
            
        else:
            while(n.next is not None):
                count = count+1
                n = n.next
                
            print(f"There are {count+1} element present in ths Linked list")
            
    def reverse_display(self):
        if(self.head is None):
            print("There is no element present in the Linked list")
            
        elif(self.head.next is not None):
            n = self.head
            prev_node = None
            
            while n is not None:
                next_node = n.next
                n.next = prev_node
                prev_node = n
                n = next_node
                
            self.head = prev_node
            
            n = self.head
            
            while(n is not None):
                print(n.data,end=" ")
                n = n.next
                
            n = self.head
            prev_node = None
            
            while n is not None:
                next_node = n.next
                n.next = prev_node
                prev_node = n
                n = next_node
            self.head = prev_node
            
    def reverse_element(self):
        if(self.head is None):
            print("There is no element present in the Linked list")
            
        elif(self.head.next is not None):
            n = self.head
            prev_node = None
            
            while n is not None:
                next_node = n.next
                n.next = prev_node
                prev_node = n
                n = next_node
            self.head = prev_node
            
list = LinkedList()

while(True):
    choice = int(input("\nChoice:\n1.Insert the element at beginning\n2.Insert the element at middle\n3.Insert after position\n4.Insert the element at end\n5.Delete the element at beginning\n6.Delete the element at middle\n7.Delete the element at end\n8.print all elements\n9.Count\n10.Display the reversed list\n11.save the reversed element\n12.escape\nEnter the choice:"))
    if(choice == 1):
        element = int(input("Enter the Element:"))
        list.insert_begin(element)
        
    elif(choice == 2):
        element = int(input("Enter the Element:"))
        list.insert_middle(element)
        
    elif(choice == 3):
        element = int(input("Eneter the Element:"))
        list.insert_after(element)
        
    elif(choice == 4):
        element = int(input("Enter the Element:"))
        list.insert_end(element)
        
    elif(choice == 5):
        list.delete_begin()
        
    elif(choice == 6):
        list.delete_middle()
        
    elif(choice == 7):
        list.delete_end()
        
    elif(choice == 8):
        list.display()
        
    elif(choice == 9):
        list.count()
        
    elif(choice == 10):
        list.reverse_display()
        
    elif(choice == 11):
        list.reverse_element()
        
    elif(choice == 12):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")