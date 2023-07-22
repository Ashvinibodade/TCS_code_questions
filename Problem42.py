# Factors of a Given Number

def findFactors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    
    return l

if __name__=="__main__":
    n=int(input("Enter number:"))

    ans=findFactors(n)
   
    print(*ans , sep=",")