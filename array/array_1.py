lis = []

def insert_element(lis):
    element = int(input("Enter the value:"))
    pos = int(input("Enter the position:"))
    
    if(lis is None):
        lis.append(element)
        
    else:
        lis.insert((pos-1),element)
        
    return lis

def display(lis):
    for i in range(len(lis)):
        print(lis[i],end=" ")

def insert_end(lis):
    pos = len(lis)
    element = int(input("Enter the element:"))
    lis.insert(pos,element)
    return lis
    
def insert_begin(lis):
    element = int(input("Enter the element:"))
    lis.insert(0,element)
    return lis

def delete_element(lis):
    if(lis is None):
        print("The list is empty")
        
    else:
        pos = int(input("Enter the position:"))
        del lis[(pos-1)]
        
    return lis

def delete_begining(lis):
    if(lis is None):
        print("The list is empty")
        
    else:
        del lis[0]
        
    return lis

def delete_ending(lis):
    if(lis is None):
        print("The list is empty")
        
    else:
        del lis[(len(lis)-1)]
        
    return lis

while(True):
    choice = int(input("\nChoice:\n1.Insert the element\n2.Dsiplay\n3.Insert at begining\n4.Insert at ending\n5.Delete the element from the list\n6.Delete the begining element\n7.Delete the ending element\n8.Escape\nEnter the choice:"))
    if(choice == 1):
        lis = insert_element(lis)
        
    elif(choice == 2):
        display(lis)
        
    elif(choice == 3):
        lis = insert_begin(lis)
        
    elif(choice == 4):
        lis = insert_end(lis)
        
    elif(choice == 5):
        lis = delete_element(lis)
        
    elif(choice == 6):
        lis = delete_begining(lis)
        
    elif(choice == 7):
        lis = delete_ending(lis)
        
    elif(choice == 8):
        break
    
    else:
        print("You were eneterd a wrong choice, try again")