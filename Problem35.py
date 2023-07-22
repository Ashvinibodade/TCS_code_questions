# Greatest of three number
def greatest(n1,n2,n3):
    l=[n1,n2,n3]
    return max(l)

if __name__=='__main__':
    n1=input("Enter n1:")
    n2=input("Enter n2:")
    n3=input("Enter n3:")

    print(f"Greter no is: {greatest(n1,n2,n3)}")