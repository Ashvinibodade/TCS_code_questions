# Check if a number is prime or not

def isPrime(num):
    if num==1 or num==0:
        return 0
    flag=False

    for i in range(2,num):
        if num%i==0:
            flag=True
    
    if flag==False:
        return 1

    return 0

if __name__=="__main__":
    num=int(input("Enter number:"))

    if(isPrime(num)):
        print("Number is prime")
    else:
        print("Number is not prime")