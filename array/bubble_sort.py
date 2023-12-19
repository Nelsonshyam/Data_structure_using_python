def bubble_sort(lis):
    for i in range(0,len(lis)):
        for j in range(i+1,len(lis)):
            if(lis[i]>lis[j]):
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
    return lis

def display(lis):
    for i in range(len(lis)):
        print(lis[i],end=" ")
        
lis = []
n = int(input("Enter the number of elements:"))

for i in range(n):
    element = int(input(f"Enter the element {i+1}:"))
    lis.append(element)

lis = bubble_sort(lis)
display(lis)