def insertion_sort(lis):
    for i in range(1,len(lis)):
        temp = lis[i]
        j = i - 1
        
        while (j >= 0 and lis[j] > temp):
            lis[j + 1] = lis[j]
            j = j - 1
        lis[j + 1] = temp
        
    return lis
    
def display(lis):
    for i in range(len(lis)):
        print(lis[i],end=" ")
        
lis = []
n = int(input("Enter the number of elements:"))

for i in range(n):
    element = int(input(f"Enter the element {i+1}:"))
    lis.append(element)

lis = insertion_sort(lis)
display(lis)