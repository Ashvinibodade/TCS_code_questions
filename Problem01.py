# Smallest no in array

# complexity-NlogN
n=int(input("Enter no of elements in the string:"))
l=[]
for i in range(n):
    l.append(int(input()))
# l.sort()
# print(f"Smallest number in the array :{l[0]}")

# complexity-n
min=l[0]
for i in range(n):
    if l[i]<min:
        min=l[i]
print(f"Smallest number in the array :{min}")