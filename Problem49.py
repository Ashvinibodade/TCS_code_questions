# Check if the number is an abundant number or not

def abundantNum(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    
    if sum>num:
        print("Abundant number")
    else:
        print("Not Abundant Number")


if __name__=="__main__":
    num=int(input("Enter number:"))

    abundantNum(num)
