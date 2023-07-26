# Remove All Duplicates from a String

def remove_Duplicates(str):
    d={}
    result=""
    for i in str:
        if i!=" ":
            if i in d:
                d[i]+=1
            else:
                d[i]=1

    for i in d:
        print(i,end="")

if __name__=="__main__":
    string=input("Enter string:")

    remove_Duplicates(string)