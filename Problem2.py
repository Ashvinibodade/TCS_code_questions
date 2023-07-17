# Largest element in the array

# complexity-NlogN
n=int(input("Enter no of elements in the string:"))
l=[]
for i in range(n):
    l.append(int(input()))
# l.sort()
# print(f"Largest number in the array :{l[-1]}")

# complexity-n
max=l[0]
for i in range(n):
    if l[i]>max:
        max=l[i]
print(f"Largest number in the array :{max}")