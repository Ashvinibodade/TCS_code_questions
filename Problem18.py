# Replace elements by its rank in the array

def findRank(arr,n):
    ans_arr=arr.copy()
    ans_arr.sort()
    ans_arr = list(set(ans_arr))

    for i in range(n):
        for j in range(len(ans_arr)):
            if arr[i]==ans_arr[j]:
                arr[i]=j+1

    return arr

if __name__ =="__main__":
    n=int(input("Enter no of element:"))
    l=[]
    for i in range(n):
        l.append(int(input()))

    ans=findRank(l,n)

    print(ans)