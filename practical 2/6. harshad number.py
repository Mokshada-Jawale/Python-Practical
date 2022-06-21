#Program to print harshad number
n = int(input())
li = list(map(int,str(n)))
z = sum(li)
if n%z == 0:
    print(n,'is a Harshad Number')
else:
    print(n,'is not a Harshad Number')
    
