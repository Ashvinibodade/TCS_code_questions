# Average of all elements in array

n=int(input("Enter no of elements in the array:"))
l=[]
for i in range(n):
    l.append(int(input()))

sum=0
avg=0.0
for i in range(n):
    sum+=l[i]

avg=sum/n
print(f"Average of all elements in array:{avg}")