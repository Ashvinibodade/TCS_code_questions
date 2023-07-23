# LCM of two numbers

def lcm(n1,n2):
    ans=1
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            ans=i
    
    lcm=(n1*n2)//ans
    return lcm

if __name__=="__main__":
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))

    print(f"LCM of {n1} and {n2} is {lcm(n1,n2)}")