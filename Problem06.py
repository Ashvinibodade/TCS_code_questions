# Rearrange the array in increasing-decreasing order
# first half-in increasing order
# second half-in decreasing order


def increasing_decreasing(arr,n):
    arr.sort()
    u=int(n/2)
    for i in range(u):
        print(arr[i],end=" ")
    for i in range(n-1,u-1,-1):
        print(arr[i],end=" ")


n=int(input("Enter no of elements in the array:"))
l=[]
for i in range(n):
    l.append(int(input()))

increasing_decreasing(l,n)