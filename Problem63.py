# Convert Octal to Decimal

import math

def octal_Decimal(num):
    ans=0
    re=num[::-1]
    for i in range(len(re)):
        digit=int(re[i])
        power=8**i
        res=digit*power
        ans+=res

        print(digit,power,res,ans)
    return ans

if __name__=="__main__":
    n=input("Enter octal number:")

    print(f"Octal-{n} to Decimal-{octal_Decimal(n)}")