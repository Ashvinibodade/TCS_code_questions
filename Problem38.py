# Maximum and Minimum Digit in a Number

def minmax(num):
    mini=float('inf')
    maxi=float('-inf')

    while(num!=0):
        rem=num%10
        mini=min(mini,rem)
        maxi=max(maxi,rem)
        num=num//10

    print("Minimum-",mini)
    print("Maximum-",maxi)

if __name__=='__main__':
    n=int(input("Enter number:"))

    minmax(n)

    