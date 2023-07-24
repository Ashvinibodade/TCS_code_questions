# Convert Decimal to Binary Number

def decimal_binary(dnum):
    i=0
    bnum=""
    while (dnum) :
        bnum=str(dnum % 2)+bnum
        i=i+1
        dnum //= 2
	
    print(*bnum,sep='')


if __name__=="__main__":
    decimal=int(input("Enter decimal number"))

    decimal_binary(decimal)