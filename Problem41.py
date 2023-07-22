# Calculate the Power of a Number : Binary Exponentiation

import math

def findPower(num,p):
    return pow(num,p)

if __name__=="__main__":
    num=int(input("Enter the number:"))
    k=int(input("Enter the power:"))

    print(f"Result is: {findPower(num,k)}")