# Quick Sort Algorithm

def quickSort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)

        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    print(i,pivot)

    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            print(i,j,pivot)
            arr[i],arr[j]=arr[j],arr[i]
            print(i,j)
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

if __name__=="__main__":
    n=int(input("Enter number of element in the array:"))
    l=[]
    for i in range(n):
        l.append(int(input()))

    quickSort(l,0,n-1)
    print(l)