# Factorial of a Number : Iterative and Recursive

def ItFact(n):
    ans=1
    for i in range(1,n+1):
        ans*=i

    return ans

def ReFact(n):
    if n==0:
        return 1
    else:
        return n*ReFact(n-1)

if __name__=="__main__":
    num=int(input("Enter a number:"))

    print("Iterative Approach:")
    print(f"Factorial of {num} is {ItFact(num)}")

    print("Recursive Approach:")
    print(f"Factorial of {num} is {ReFact(num)}")