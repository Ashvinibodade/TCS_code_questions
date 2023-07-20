# Check if a number is Armstrong Number or not

import math

def checkArmstrong(num):
    temp=num
    rem=0
    sum=0
    count=len(str(num))
    while temp!=0:
        rem=temp%10
        sum+=pow(rem,count)
        temp=temp//10
    
    if sum==num:
        return 1
    else:
        return 0

if __name__=="__main__":
    num=int(input("Enter number:"))

    if checkArmstrong(num):
        print("Number is Armstrong")
    else:
        print("Number is not Armstrong")