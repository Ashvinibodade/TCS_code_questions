# Sum Of Digits of A Number

def find_Digit_Sum(num):
    rem=0
    sum=0
    while(num!=0):
        rem=num%10
        sum+=rem
        num//=10

    return sum

if __name__=='__main__':
    num=int(input("Enter number:"))

    print("Sum of digit is :",find_Digit_Sum(num))