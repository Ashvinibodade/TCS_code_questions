# Adding element in array
# ---at starting point
# ---at ending point
# ---at specific position

def insertAtBegin(arr,n):
    value=int(input("Enter value to be insert:"))
    arr.insert(0,value)

def insertAtEnd(arr,n):
    value=int(input("Enter value to be insert:"))
    arr.append(value)

def insertAtPosition(arr,n):
    value=int(input("Enter value to be insert:"))
    pos=int(input("Enter position where u want to insert:" ))

    arr.insert(pos,value)


if __name__=="__main__":
    
    max=100
    n=int(input("Enter no of elements in the array:"))
    l=[]
    for i in range(n):
        l.append(int(input()))
    
    print("Inserting at begining:")
    insertAtBegin(l,n)
    n=n+1

    print("Inserting at end")
    insertAtEnd(l,n)
   

    print("Inserting at specific position")
    insertAtPosition(l,n)
   

    print("Final array:")
    print(",".join(map(str,l)))

    