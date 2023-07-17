# Remove duplicates in-place from unsorted array

def removeDuplicates(arr,n):
    mark=[]
    for i in range(n):
        mark.append(1)
  
    for i in range(n):
        if(mark[i]==1):
            for j in range(i+1,n):
                if arr[i]==arr[j]:
                    mark[j]=0

    print("After removing duplicates ,array would be:")
    for i in range(n):
        if mark[i]==1:
            print(arr[i],end=" ")


if __name__=="__main__":
    
    n=int(input("Enter no of elements in the array:"))
    l=[]
    for i in range(n):
        l.append(int(input()))

    removeDuplicates(l,n)
    
