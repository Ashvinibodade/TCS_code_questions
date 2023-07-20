# Find all symmetric pairs in the array of pairs

def symPairs(arr,n):
    ans=[]
    for i in range(n):
        for j in range(i+1,n):
            if((arr[j][0]==arr[i][1]) and (arr[j][1]==arr[i][0]) ):
                ans.append(arr[j])
    return ans

if __name__=='__main__':

    n=int(input("Enter no of pairs u want:"))
    l=[]
    # asp=[(int(input()),int(input()) ) for val in l]

    for val in range(n):
        asp=(int(input()) , int(input()))
        l.append(asp)

    res=symPairs(l,n)
    if len(res) >0:
        print("Symetric pairs:")
        for pair in res:
            print(pair[0],",",pair[1])
    else:
        print("No Symmetric pair found")