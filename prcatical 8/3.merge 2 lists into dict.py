# Given 2 lists: one containing keys and other containing values. Merge them to form a dictionary

print("Enter the list containing keys")
key=list(map(str,input().split()))
print("Enter the list containing values: ")
val=list(map(int,input().split()))
if len(key)==len(val):
    for i in range(len(key)):
        d = dict(zip(key,val))
    print(d)
else:
    print("Number of keys are not equal to number of values")