# Convert Binary to Octal

# def binary_octal(num):
#     return oct(int(num, 2))[2::]

def binary_octal(num):
    n = len(num)
    if (n % 3 == 1) :
        num = "00" + num
    elif (n % 3 == 2) :
        num = "0" + num
    n = len(num)
    ans=""
    for i in range(0,n,3):
        # temp=(num[i]-'0')*4 + (num[i+1]-'0')*2 + (num[i+2]-'0')*1
        temp = int(num[i:i+3], 2)
        ans+=str(temp)

    return ans

if __name__=="__main__":
    n=input("Enter Binary number:")

    print(f"Binary-{n} to octal-{binary_octal(n)}")