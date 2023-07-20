# Check whether a number is Perfect Number or not

def isPerfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i 
    return sum

if __name__=="__main__":
    num=int(input("Enter number:"))

    ans=isPerfect(num)

    if ans==num:
        print("Number is a perfect number")
    else:
        print("Number is not perfect number")