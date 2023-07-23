# Program to Find Roots of a quadratic equation

import math
def findRoots(a,b,c):
    d=(b*b)-4*a*c
    sqrt_val=math.sqrt(abs(d))

    if d>0:
        print("Roots are real and different:")
        r1=(-b+sqrt_val)/2*a
        r2=(-b-sqrt_val)/2*a
        print(r1,",",r2)
    elif d==0:
        print("Root are real and same:")
        r1=-b/(2*a)
        r2=-b/(2*a)
        print(r1,",",r2)
    else:
        print("Roots are complex:")
        r1=-b/(2*a)
        r2=-b/(2*a)
        print(r1,"+i",sqrt_val,",",r2,"-i",sqrt_val)

if __name__=="__main__":
    a=int(input("Enter a:"))
    b=float(input("Enter b:"))
    c=float(input("Enter c:"))

    findRoots(a,b,c)
