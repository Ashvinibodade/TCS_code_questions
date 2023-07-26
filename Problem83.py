# Maximum occurring character in a string

def Max_occ_character(str):
    d={}
    result=""
    for i in str:
        if i!=" ":
            if i in d:
                d[i]+=1
            else:
                d[i]=1
    maxi=max(d,key=d.get)
    return maxi

if __name__=="__main__":
    string=input("Enter string:")

    print(Max_occ_character(string))
