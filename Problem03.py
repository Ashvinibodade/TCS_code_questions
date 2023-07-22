#find second smallest and second largest element in array

n=int(input("Enter no of elements in the array:"))
l=[]
for i in range(n):
    l.append(int(input()))

# ---------------case1
# l.sort()
# print(f"Second smallest :{l[1]}")
# print(f"second largest: {l[-2]}")

# ---------------case2
if n==0 or n==1:
    print("-1")
else:
    min=float('inf')
    max=float('-inf')
    sec_min=float('inf')
    sec_max=float('-inf')

    for i in range(n):
        if l[i]<min:
            min=l[i]
        if l[i]>max:
            max=l[i]

    for i in range(n):
        if l[i]<sec_min and l[i]!=min:
            sec_min=l[i]
        if l[i]>sec_max and l[i]!=max:
            sec_max=l[i]
    print(f"Second smallest :{sec_min}")
    print(f"Second largest: {sec_max}")

# ---------------case3

def sec_smallest(l,n):
    if n<2:
        return -1
    small=float('inf')
    sec_small=float('inf')
    for i in range(n):
        if l[i]<small:
            sec_small=small
            small=l[i]
        elif (l[i]<sec_small and l[i]!=small):
            sec_small=l[i]
    return sec_small

def sec_largest(l,n):
    if n<2:
        return -1
    large=float('-inf')
    sec_large=float('-inf')
    for i in range(n):
        if l[i]>large:
            sec_large=large
            large=l[i]
        elif (l[i]>sec_large and l[i]!=large):
            sec_large=l[i]
    return sec_large



print("Second smallest:",sec_smallest(l,n))
print("Second largest:",sec_largest(l,n))