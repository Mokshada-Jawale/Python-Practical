#program to convert binary number to decimal number
binary = int(input('Enter binary number: '))
binary1 = binary
decimal, i, n = 0, 0, 0
while (binary != 0):
    dec = binary % 10
    decimal = decimal + dec * pow(2, i)
    binary = binary // 10
    i += 1
print('The decimal number equivalent to binary number',binary1,'is',decimal)
