# Permutations in which N people can occupy R seats

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def permutation(n,r):
    ans=factorial(n) //factorial(n-r)
    return ans

if __name__=="__main__":
    n=int(input("Enter number of people:"))
    r=int(input("Enter number of seats:"))

    print(permutation(n,r))