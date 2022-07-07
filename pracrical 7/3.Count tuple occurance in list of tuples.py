#Count tuple occurance in list of tuples:

li=[(1,2,3,4,5),(6,7,8,9,0),"mokshada",(6,7,8,9,0),"MOKSHADA",(1,2,3,4),"mokshada",(4,6,8,9),(6,7,8,9,0),(1,2,3,4,5)]
x=list(set(li))
for i in x:
    print(i,'occurs',li.count(i),'times')
