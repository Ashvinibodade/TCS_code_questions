# Check if the given number is Harshad(Or Niven) Number

def harshadNum(num):
    temp=num
    sum=0
    rem=0
    while temp!=0:
        rem=temp%10
        sum+=rem
        temp=temp//10

    if num%sum==0:
        return 1
    return 0

if __name__=="__main__":
    num=int(input("Enter number:"))

    if harshadNum(num):
        print("Given number is harshad number")
    else:
        print("Given number is not harshad number")