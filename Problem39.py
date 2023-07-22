# Print Fibonacci Series up to Nth term

def fibo(n):
    fib=[]
    if n==0:
        fib.append(0)
    if n==1:
        fib.append(0)
        fib.append(1)
    else:
        fib.append(0)
        fib.append(1)
        for i in range(2,n+1):
            fib.append(fib[i-1]+fib[i-2])
    return fib

if __name__=="__main__":
    num=int(input("Enter the term up to which you have to print fibonacci series:"))

    ans=fibo(num)
    print("Fibonacci Series:")
    for i in ans:
        print(i,end=" ")
        