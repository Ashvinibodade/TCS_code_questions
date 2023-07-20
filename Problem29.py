# Check whether a given number is even or odd

def even_or_odd(num):
    if num%2==0:
        return 1
    return 0

if __name__=="__main__":
    num=int(input("Enter number:"))

    if even_or_odd(num):
        print("Number is even")
    else:
        print("Number is odd")