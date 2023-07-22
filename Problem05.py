# count frequency of each element in an array

def frequency(arr,n):
    d={}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
    for x in d:
        print(x , d[x])

n=int(input("Enter no of elements in the array:"))
l=[]
for i in range(n):
    l.append(int(input()))

frequency(l,n)
