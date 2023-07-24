# Merge Sort Algorithm

def merge(arr,low,high,mid):
    l=arr[low:mid+1]
    r=arr[mid+1:high+1]

    l_index=0
    r_index=0
    sorted_index=low

    while l_index<len(l) and r_index<len(r):
        if l[l_index]<=r[r_index]:
            arr[sorted_index]=l[l_index]
            l_index=l_index+1
        else:
            arr[sorted_index]=r[r_index]
            r_index=r_index+1

        sorted_index=sorted_index+1

    while l_index<len(l):
        arr[sorted_index] = l[l_index]  
        l_index = l_index + 1  
        sorted_index = sorted_index + 1  

    while r_index<len(r):
        arr[sorted_index] = r[r_index]  
        r_index = r_index + 1  
        sorted_index = sorted_index + 1 

    return arr 

def mergeSort(arr,low,high):
    if low>=high:
        return
    
    mid=(low+high)//2

    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)

    merge(arr,low,high,mid)

if __name__=="__main__":
    n=int(input("Enter number of element in the array:"))
    l=[]
    for i in range(n):
        l.append(int(input()))

    mergeSort(l,0,n-1)
    print(l)