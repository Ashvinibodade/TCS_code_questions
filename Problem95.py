# Reverse Words in a String

def reverseWords(str):
    str=str.split()[::-1]
    for i in str:
        print(i,end=" ")

if __name__=="__main__":
    string=input("Enter string:")

    reverseWords(string)