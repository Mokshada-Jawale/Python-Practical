li = list(map(int,input('The given list is: ').split()))
length = len(li)
for i in range(length-2):
    if li[i]==li[i+1] and li[i+1]==li[i+2]:
        print('The 3 consecutive common number is: ',li[i])
