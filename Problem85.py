# Print all the duplicates in the string

def findDuplicates(str):
    d={}
    for i in str:
        if i!=" ":
            if i in d:
                d[i]+=1
            else:
                d[i]=1

    for i in d:
        if d[i]>1:
            print(i,"-",d[i])

if __name__=="__main__":
    string=input("Enter string:")

    findDuplicates(string)