k = int(input())
li = list(map(int,input().split()))
li2 = []
for i in li:
    freq = li.count(i)
    if freq > k:
        if i not in li2:
            li2.append(i)
print(li2)
