# Reverse the array

# -------------case1----------------
# def Reversed_array(arr,n):
#     start=0
#     end=n-1
#     while start<end:
#         arr[start],arr[end]=arr[end],arr[start]
#         start+=1
#         end-=1
#     return arr

# ------------case2---------------
# def Reversed_array(arr,start,end):
#     if(start<end):
#         arr[start],arr[end]=arr[end],arr[start]
#         Reversed_array(arr,start+1,end-1)
#     return arr


n=int(input("Enter no of elements in the array:"))
l=[]
for i in range(n):
    l.append(int(input()))

# ans=Reversed_array(l,n)
# print("Reversed array:")
# for i in range(n):
#     print(ans[i],end=" ")

# ans=Reversed_array(l,0,n-1)
# for i in range(n):
#     print(ans[i],end=" ")

# ------------------case3------------
l.reverse()
for i in range(n):
    print(l[i],end=" ")


