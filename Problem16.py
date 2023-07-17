# Find all symmetric pairs in the array of pairs

def symPairs(arr,n):
    ans=[]
    for i in range(n):
        for j in range(i+1,n):
            if((arr[j][0]==arr[i][1]) and (arr[j][1]==arr[i][0]) ):
                print(arr[j])
                a=tuple(arr[j])
                ans.append(a)
    return ans

if __name__=='__main__':

    n=int(input("Enter no of pairs u want:"))
    l=[]
    asp=[(int(input()),int(input()) ) for val in l]


    res=symPairs(asp,n)
    print(",".join(map(str,res)))