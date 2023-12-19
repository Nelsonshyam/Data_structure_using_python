def selection_sort(lis,n):
    for i in range(n):
        min = i
        temp = 0
        for j in range(i+1,n):
            if (lis[min] > lis[j]):
                min = j
                
        temp = lis[min]
        lis[min] = lis[i]
        lis[i] = temp
        
    return lis

lis = []
n = int(input("Enter the number of element:"))

for i in range(n):
    element = int(input(f"Enter the element{i+1}:"))
    lis.append(element)
    
print("Original list:")
for i in range(n):
    print(lis[i],end=" ")
print("")

lis = selection_sort(lis,n)

print("Sorted list")
for i in range(n):
    print(lis[i],end=" ")