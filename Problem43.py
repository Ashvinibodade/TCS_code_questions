# Print all Prime Factors of the given number

import math
def primeFactor(num):
    while num%2==0:
        print(2 ,end=" ")
        num=num//2

    for i in range(3,int(math.sqrt(num))+1,2):
        while num%i==0:
            print(i ,end=" ")
            num=num//i

    if num>2:
        print(num)

if __name__=="__main__":
    num=int(input("Enter the number:"))

    primeFactor(num)