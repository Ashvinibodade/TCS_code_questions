# Prime Numbers in a given range

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
    min=int(input("Enter min:"))
    max=int(input("Enter max:"))

    for i in range(min,max):
        if(isPrime(i)):
            print(i)