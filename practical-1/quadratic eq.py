#solve quadratic equation
import math
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
D=(math.pow(b,2)-(4*a*c))
if(D<0):
    print("The roots of quadratic equation ",a,"x^2+",b,"x+",c," are imaginary",sep="")
    exit()
b*=-1
root1=(b+D)/(2*a)
root2=(b-D)/(2*a)
print("The determinant of the quadratic equation",d)
