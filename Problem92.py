# Change case of each character in a string

def changeCase(str):
    return str.swapcase()

if __name__=="__main__":
    string=input("Enter string:")

    print(changeCase(string))