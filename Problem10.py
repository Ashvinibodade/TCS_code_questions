# Find the median of given array

n=int(input("Enter no of elements in the array:"))
l=[]
for i in range(n):
    l.append(int(input()))

l.sort()
if(n%2==0):
    c=int(n/2)
    ans=(l[c]+l[c-1])/2
else:
    c=round(n/2)
    ans=l[c]

print(f"Median of given array:{ans}")