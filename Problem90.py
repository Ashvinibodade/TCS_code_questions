# Count the number of words in a given string

def count(str):
    count=1
    for i in str:
        if i==" ":
            count+=1

    return count

if __name__=="__main__":
    str=input("Enter string:")

    print(f"Number of words:{count(str)}")