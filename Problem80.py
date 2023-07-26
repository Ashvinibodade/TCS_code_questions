# Calculate Frequency of characters in a String

def calcCharacter(str):
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
        print(d[i],end=" ")


if __name__=="__main__":
    string=input("Enter string:")

    calcCharacter(string)
