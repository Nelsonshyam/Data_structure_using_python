def linear_search(lis,n,target):
    pos = -1
    
    for i in range(len(lis)):
        if(target == lis[i]):
            pos = i+1
            index = i
            
    if(pos == -1):
        print("element is not present in the list")
        
    else:
        print(f"Index is \'{index}\' And postion is \'{pos}\'")
        
lis = []
n = int(input("Enter the number of elements:"))

for i in range(n):
    element = int(input(f"Enter the element {i+1}:"))
    lis.append(element)
    
target = int(input("Enter the element you want to search:"))

linear_search(lis,n,target)