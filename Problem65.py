# Bubble Sort Algorithum

def bubbleSort(arr,n):
    temp=0
    for i in range(n-1,-1,-1):
        for j in range(0,i,1):
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr

if __name__=="__main__":
    n=int(input("Enter number of element in the array:"))
    l=[]
    for i in range(n):
        l.append(int(input()))

    print(bubbleSort(l,n))