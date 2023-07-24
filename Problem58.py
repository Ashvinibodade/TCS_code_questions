# Convert Binary to Decimal

import math

def binary_Decimal(num):
    ans=0
    re=num[::-1]
    for i in range(len(re)):
        digit=int(re[i])
        power=2**i
        res=digit*power
        ans+=res
    return ans

if __name__=="__main__":
    n=input("Enter Binary number:")

    print(f"Binary-{n} to Decimal-{binary_Decimal(n)}")