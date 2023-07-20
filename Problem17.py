# Maximum Product Subarray in an Array

def maxProduct(arr,n):
    result=arr[0]

    for i in range(n):
        p=arr[i]
        for j in range(i+1,n,1):
            result=max(result,p)
            p*=arr[j]
        result=max(result,p)
    
    return result


if __name__ =="__main__":
    n=int(input("Enter no of element:"))
    l=[]
    for i in range(n):
        l.append(int(input()))

    print("Maximum Product Subarray:",maxProduct(l,n))