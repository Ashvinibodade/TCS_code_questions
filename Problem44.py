# Check if a number is a Strong Number or not

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def strongNum(num):
    temp=num
    sum=0
    rem=0
    while temp!=0:
        rem=temp%10
        sum=sum+factorial(rem)
        temp=temp//10

    if sum==num and sum!=0:
        return 1
    return 0

if __name__=="__main__":
    number=int(input("ENter number:"))

    if strongNum(number):
        print("YES")
    else:
        print("NO")

    