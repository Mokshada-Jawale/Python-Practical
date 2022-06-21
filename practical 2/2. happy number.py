#Program to print happy number
def HappyNumber(n):
    digit = 0
    sum = 0
    while n>0:
        digit = n%10
        sum = sum + (digit * digit)
        n = n//10
    return sum

num = int(input())
result = num

while result != 1 and result != 4:
    result = HappyNumber(result)
if result==1:
    print(num,'is a Happy Number')
else:
    print(num,'is not a Happy Number')
