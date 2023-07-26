# Find the largest word in a String

def findLargest(str):
    maxi=float('-inf')
    st=""
    for i in str.split():
        maxi=max(maxi,len(i))
        if len(st)!=maxi:
            st=i

    return st

if __name__=="__main__":
    string=input("Enter string:")

    print(findLargest(string))