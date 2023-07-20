# Check whether a number is positive or negative

def pos_or_neg(num):
    if num>0:
        print("Number is positive")
    else:
        print("Number is negative")

if __name__=="__main__":
    num=int(input("Enter number:"))

    pos_or_neg(num)