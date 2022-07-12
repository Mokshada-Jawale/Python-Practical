#Program to find intersection of 2 lists
print("Enter the elements of list A: ")
a=list(map(int,input().split()))
print("Enter the elements of list B: ")
b=list(map(int,input().split()))
li = []
for i in a:
    if i in b:
        li.append(i)
print("Intersection of 2 lists is: ",li)
