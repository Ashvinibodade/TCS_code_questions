# Replace all the 0’s with 1 in a given integer

def replace0(num):
    ans=0
    temp=1
    
    while(num!=0):
        rem=num%10
        if rem==0:
            ans=temp*1+ans
            temp=temp*10
        else:
            ans=temp*rem+ans
            temp=temp*10
        num=num//10

    return ans

if __name__=="__main__":
    num=int(input("Enter number:"))

    print(replace0(num))