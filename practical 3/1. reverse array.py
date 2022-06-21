# To print the elements of array in reverse order.
l=list(map(int,input("Enter an array: ").split()))
length=len(l)
print("Array elements in reverse order are: ")
for i in range(-1,-length-1,-1):
    print(l[i],end=' ')
