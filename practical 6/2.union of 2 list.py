#Program to find union of 2 lists
print('Elements is 1st list are:\n')
li1 = list(map(int,input().split()))
print('Elements is 2nd list are:\n')
li2 = list(map(int,input().split()))
union = li1+li2
print('The union of two list is:\n')
print(list(set(union)))
