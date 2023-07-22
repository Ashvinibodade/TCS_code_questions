# Rotate the array by k elements:Block swap algorithum

# Approach: 
# For given k, 
# Two cases can arise in an array:-

# Case 1: when k<n-k 
# For this, we need to swap the first k elements with the last k elements in the given part of the array.
# By this last k elements come to their correct position.

# Case 2: when k>n-k
# For this, we need to swap the last n-k elements with the first n-k elements in the given part of the array.
# By this first n-k elements come to their correct position.

# Case 3: when k=n-k
# For this, just swap the first half and the second part of the given array.
# And just return 

def swap(arr,a,b,k):
    for i in range(k):
        arr[a+i],arr[b+i]=arr[b+i],arr[a+i]

def blockSwap(arr,k,n):
    if (k==0 or k==n):
        return
    while(k!=n-k):
        if (k<n-k):
            swap(arr,0,n-k,k)
        else:
            swap(arr,0,k,n-k)
    swap(arr,0,n-k,k)

n=int(input("Enter no of elements in the array:"))
l=[]
for i in range(n):
    l.append(int(input()))
k=int(input("Enter after how much step the array should rotate:"))
blockSwap(l,k,n)

print("Array after rotation:")
for i in range(n):
    print(l[i],end=" ")