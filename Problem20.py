# Finding Equilibrium index in an array

def equilibrium_Index(arr,n):
    for i in range(n):
        leftSum=0
        for j in range(i):
            leftSum+=arr[j]
        rightSum=0
        for j in range(i+1,n):
            rightSum+=arr[j]
        
        if leftSum==rightSum:
            return i
        
    return -1


if __name__=="__main__":
    n=int(input("Enter no of element:"))
    l=[]
    for i in range(n):
        l.append(int(input()))
    
    print("Equilibrium Index:",equilibrium_Index(l,n))
