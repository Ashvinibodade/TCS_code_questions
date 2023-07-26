# Write a program to sort characters in a string

def sorting(str):
    str=sorted(str)
    
    for i in str:
        print(i,end="")

if __name__=="__main__":
    string=input("Enter string:")

    sorting(string)