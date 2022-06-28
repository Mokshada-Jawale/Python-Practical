#python program to compute the difference between two lists
l1 = ['a','b','c','d']
l2 = ['p','q','c','d']
ans1 = list(set(l1)-set(l2))
ans2 = list(set(l2)-set(l1))
print(ans1)
print(ans2)
