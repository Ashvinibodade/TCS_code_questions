# Calculate the sum of the elements in array

n=int(input("Enter no of elements in the array:"))
l=[]
for i in range(n):
    l.append(int(input()))

sum=0
for i in range(n):
    sum+=l[i]

print("Sum of the array is:",sum)