# Find GCD of two numbers

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

def gcd(n1,n2):
    ans=1
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            ans=i
    
    return ans

if __name__=="__main__":
    n1=int(input("Enter n1"))
    n2=int(input("Enter n2"))

    print(f"GCD of {n1} and {n2} is {gcd(n1,n2)}")