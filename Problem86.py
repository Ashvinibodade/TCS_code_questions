# Remove Characters from first String present in the Second String

def findDiff(str1,str2):
    d={}
    for i in str1:
        if i!=" ":
            if i in d:
                d[i]+=1
            else:
                d[i]=1

    for i in str2:
        if i!=" ":
            if i in d:
                d[i]+=1
            else:
                d[i]=1

    for i in d:
        if d[i]==1:
            print(i,end="")

if __name__=="__main__":
    str1=input("Enter first string:")
    str2=input("Enter second string:")

    findDiff(str1,str2)
