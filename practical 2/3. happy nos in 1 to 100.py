#Program to print happy numbers between 1 to 100.
def HappyNumber(n):
    digit = 0
    sum = 0
    while n>0:
        digit = n%10
        sum = sum + (digit * digit)
        n = n//10
    return sum
for i in range(1,101):
    result=i
    while result != 1 and result != 4:
        result = HappyNumber(result)

    if result==1:
        print(i)
