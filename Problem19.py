# Sort Elements of an Array by Frequency

def sort_by_frequency(arr,n):
    # result = sorted(arr, key = arr.count,reverse = True)
    # return result

    mp = {}
    for i in set(arr):
      x=arr.count(i)
      try:
        mp[x].append(i)
      except:
        mp[x]=[i]
    ans=[]

    for i in sorted(mp, reverse=True):
      for j in sorted(mp[i], reverse=True):
        ans.extend([j]*i)
    return ans

if __name__ =="__main__":
    n=int(input("Enter no of element:"))
    l=[]
    for i in range(n):
        l.append(int(input()))

ans=sort_by_frequency(l,n)
print( ans)