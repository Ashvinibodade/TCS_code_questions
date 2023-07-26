# Change every letter with next lexicographic alphabet

def findLexicographicAlpha(str):
    for i in str:
        if i=='z':
            print("a",end="")
        else:
            print(chr(ord(i)+1),end="")

if __name__=="__main__":
    string=input("Enter string:")

    findLexicographicAlpha(string)