#Python program to find tuples which have all element divisible by k:
print('The given tuple is:\n')
a=tuple(map(int,input().split()))
print('The value of k is:\n')
k=int(input())
li = []
for i in a:
    if i%k==0:
        li.append(i)
print('The tuple elements divisible by',k,'are:\n')
print(tuple(li))

