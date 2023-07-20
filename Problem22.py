# Check if array is subset of another array

def subset_or_not(arr1,arr2,n1):
    for i in range(n1):
        if arr1[i] not in arr2:
            return 0
    return 1

if __name__=="__main__":
    n1=int(input("Enter no of element for first array:"))
    l1=[]
    for i in range(n1):
        l1.append(int(input()))
    n2=int(input("Enter no of element for second array array:"))
    l2=[]
    for i in range(n2):
        l2.append(int(input()))

    if (subset_or_not(l1,l2,n1)):
        print("Array1 is subset of Array2")
    else:
        print("Array1 is not subset of Array2")