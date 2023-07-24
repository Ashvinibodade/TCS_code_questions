# Convert Octal to Binary

def decimal_binary(dnum):
    dnum=int(dnum)
    bnum=""
    if dnum==0:
        bnum='000'
    while (dnum!=0) :
        bnum=str(dnum % 2)+bnum
        dnum //= 2

    n=len(bnum)
    if (n % 3 == 1) :
        bnum = "00" + bnum
    elif (n % 3 == 2) :
        bnum = "0" + bnum
    
    return bnum
	
def octal(num):
    ans=""
    ty=len(num)

    for i in range(ty):
        ans=ans+decimal_binary(num[i])

    return ans



if __name__=="__main__":
    n=input("Enter Binary number:")

    print(octal(n))