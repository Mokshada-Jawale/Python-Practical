# Program to print armstrong number
n = int(input())
sum = 0
flag = n
o = len(str(n))
while flag > 0:
    d = flag % 10
    sum += d ** o
    flag //= 10
if n == sum:
    print(n,"is armstrong number")
else:
    print(n,"is not armstrong number")
