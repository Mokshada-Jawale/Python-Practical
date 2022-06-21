# Program to print largest and smallest element in an array
arr=list(map(int,input("Enter an array: ").split()))
length=len(arr)
min=arr[0]
max=arr[0]
for i in arr:
    if i<min:
        min=i
    if i>max:
        max=i
print("The largest element in array is ",max)
print("The smallest element in array is ",min)
