# Search the element in array

def printIndex(arr,k):
    ans=arr.index(k)
    return ans

if __name__=="__main__":
    n=int(input("Enter no of element:"))
    l=[]
    for i in range(n):
        l.append(int(input()))
    k=int(input("Enter element to be searched:"))

    print(f"{k} is present at position {printIndex(l,k)}")