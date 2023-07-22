# Program to find Sum of GP Series
import math

def sum_of_GP(n,a,r):
    sum=0
    # for i in range(n):
    #     sum+=a
    #     a*=r
    # return sum
    return (a * (1 - pow(r, n))) / (1 - r)
    

if __name__=="__main__":
    n=int(input("Enter the number of term in AP series:"))
    a=int(input("Enter first term of an AP series:"))
    r=float(input("Enter the difference between the terms of AP series:"))

    print("Sum of an GP series :",sum_of_GP(n,a,r))