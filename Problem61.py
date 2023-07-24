# Convert Decimal to Octal

def decimal_octal(dnum):
    i=0
    bnum=""
    while (dnum) :
        bnum=str(dnum % 8)+bnum
        i=i+1
        dnum //= 8
	
    print(*bnum,sep='')


if __name__=="__main__":
    decimal=int(input("Enter decimal number"))

    decimal_octal(decimal)