def bubble_sort(lis):
    for i in range(0,len(lis)):
        for j in range(i+1,len(lis)):
            if(lis[i]>lis[j]):
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
                
    return lis

def binary_search(lis,n,target):
    low = 0
    high = n-1
    while(low<=high):
        mid = round((low+high)/2)
        
        if(lis[mid]==target):
            index = mid
            return index
        
        elif(lis[mid]<target):
            low = mid+1
            
        elif(lis[mid]>target):
            high = mid-1
            
    return -1

lis = []
n = int(input("Enter the number of elements:"))
for i in range(n):
    element = int(input(f"Enter the element {i+1}:"))
    lis.append(element)

lis = bubble_sort(lis)  

target = int(input("Enter the element you want to search:"))

index = binary_search(lis,n,target)

if(index == -1):
    print("The element is not present")
    
else:
    print(f"The element is found the index:{index} and position:{index+1}")