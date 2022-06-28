#Program to find union of 2 lists
li1 = list(map(int,input().split()))
li2 = list(map(int,input().split()))
union = li1+li2
print(list(set(union)))
