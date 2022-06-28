# Python program to find the length of a list using recursion
len = 0
def length(a):
   global len
   if a:
      len = len + 1
      length(a[1:])
   return len

a = ['Hello', 'World', 'list' , 'Python', 'Program']

len = length(a)

print("The length of a list is :", len)
