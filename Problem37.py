# Reverse digits of a number

def reverseNum(num):
    rem=0
    rev=0
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10

    return rev

if __name__=="__main__":
    n=int(input("Enter the number to reverse:"))

    print(f"Reverse of the number-{n} is {reverseNum(n)}")