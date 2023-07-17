# Remove duplicates in-place from sorted array

# -----------case1-----
# def removeDuplicate(arr,n):
#     st=set()
#     for i in range(n):
#         st.add(arr[i])
    
#     k=len(st)
#     j=0
#     for x in st:
#         arr[j]=x
#         j+=1
#     return k

# --------------case2--------
def removeDuplicates(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1


if __name__=="__main__":
    n=int(input("Enter no of elements in the array:"))
    l=[]
    for i in range(n):
        l.append(int(input()))
    
    # k=removeDuplicate(l,n)
    k=removeDuplicates(l)
    print(f"Number of element after removing duplicate:{k}")
    print("After removing duplicates ,array would be:")
    for i in range(k):
        print(l[i],end=" ")
