li = [1,2,3,4]
li2 = [4,5,6,7]
print(str(li))
print(str(li2))
li0 = []
for i in range(len(li)):
    li0.append(li[i]*li2[i])
print(str(li0))
