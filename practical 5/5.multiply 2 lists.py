li1 = [1,2,3,4]
li2 = [4,5,6,7]
print('Print the elements of 1st list: ',str(li1))
print('Print the elements of 2nd list: ',str(li2))
li = []
for i in range(len(li1)):
    li.append(li1[i]*li2[i])
print('List after multiplying two lists is: ',str(li))
