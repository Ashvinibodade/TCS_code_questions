# Greatest of two numbers

def greatest(n1,n2):
    return max(n1,n2)

if __name__=='__main__':
    n1=input("Enter n1:")
    n2=input("Enter n2:")

    print(f"Greter no is: {greatest(n1,n2)}")