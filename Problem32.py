# Find Sum of AP Series

def sum_of_AP(n,a,d):
    sum=0
    # for i in range(n):
    #     sum+=a
    #     a+=d            #complexity-o(n)

    sum=int((n / 2.0) * (2.0 * a + (n - 1) * d))
    return sum

if __name__=="__main__":
    n=int(input("Enter the number of term in AP series:"))
    a=int(input("Enter first term of an AP series:"))
    d=int(input("Enter the difference between the terms of AP series:"))

    print("Sum of an AP series :",sum_of_AP(n,a,d))