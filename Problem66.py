# Selection Sort Algorithm

def selectionSort(arr,n):
    for i in range(n):
        mini=i
        for j in range(i+1,n,1):
            if arr[j]<arr[mini]:
                mini=j
        temp=arr[mini]
        arr[mini]=arr[i]
        arr[i]=temp

    return arr

if __name__=="__main__":
    n=int(input("Enter number of element in the array:"))
    l=[]
    for i in range(n):
        l.append(int(input()))

    print(selectionSort(l,n))