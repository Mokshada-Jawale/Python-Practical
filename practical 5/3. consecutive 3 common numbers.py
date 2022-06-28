li = list(map(int,input().split()))
length = len(li)
for i in range(length-2):
    if li[i]==li[i+1] and li[i+1]==li[i+2]:
        print(li[i])
