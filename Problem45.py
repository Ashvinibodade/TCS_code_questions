# Check if a number is Automorphic Number

def isAutomorphic(num):
    sq=num*num

    while num!=0:
        if num%10 != sq%10:
            return False
        
        num=num//10
        sq=sq//10

    return True

if __name__=="__main__":
    num=int(input("Enter number:"))

    if isAutomorphic(num):
        print("Automorphic number")
    else:
        print("Not Automorphic")