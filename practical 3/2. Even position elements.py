#Print elements of An array present on even position
l=list(map(int,input("Enter an array: ").split()))
length=len(l)
print("Array elements at even position are: ")
for i in range(1,length,2):
    print(l[i],end=' ')

