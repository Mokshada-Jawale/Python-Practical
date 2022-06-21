#Program to Sort elements in ascending and descending order
l=list(map(int,input("Enter a list: ").split()))
l.sort()
print("Array in ascending order is: ",l)
print("Array in descending order is: ",l[::-1])
