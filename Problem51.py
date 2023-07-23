# Find the sum of numbers in the given range

def findSum(l,h):
    sum=0
    for i in range(l,h+1):
        sum+=i

    return sum

if __name__=='__main__':
    l=int(input("Enter lower range:"))
    h=int(input("Enter higher range:"))

    print(f"sum: {findSum(l,h)}")