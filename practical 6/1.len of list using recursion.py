# Python program to find the length of a list using recursion
len = 0
def length(a):
   global len
   if a:
      len = len + 1
      length(a[1:])
   return len

print('Enter the elements of list:\n')
a = list(map(int,input().split()))

len = length(a)

print("The length of a list is :", len)
