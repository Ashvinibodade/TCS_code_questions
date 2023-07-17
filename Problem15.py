# # Find all non repeating elements in list

def findReapeting(arr):
    d={}
    ar=[]
    for i in range(len(arr)):
        if arr[i] in d.keys():
            d[arr[i]]+=1
        else:
            d[arr[i]]=1

    for i in d:
        if d[i]==1:
            ar.append(i)
    # print(arr)
    # print(d)
    # print(ar)
    return ar


if __name__=="__main__":
    
    n=int(input("Enter no of elements in the array:"))
    l=[]
    for i in range(n):
        l.append(int(input()))

    res=findReapeting(l)
    # print(res)
    # print(res)
    print(','.join(map(str,res)))