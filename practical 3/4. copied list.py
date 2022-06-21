# Copy all elements of one array into another
l1=list(map(int,input("Enter a list: ").split()))
l2=[]
for i in l1:
    l2.append(i)
print("The copied array is ",l2)
