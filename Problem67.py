# Insertion Sort Algorithm

def insertionSort(arr,n):
    if n<=1:
        return arr
    
    for i in range(1,n):
        key=arr[i]
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

if __name__=="__main__":
    n=int(input("Enter number of element in the array:"))
    l=[]
    for i in range(n):
        l.append(int(input()))

    print(insertionSort(l,n))