#Program to find intersection of 2 lists
from sys import stdin, stdout, setrecursionlimit
from collections import Counter
print("Enter the elements of list A: ")
a=list(map(int,input().split()))
print("Enter the elements of list B: ")
b=list(map(int,input().split()))
A=Counter(a)
B=Counter(b)
print("Intersection of the given lists is: ")
for i in A:
    if i in B:
        x=min(A[i],B[i])
        for j in range(x):
            print(i,end=' ')
