# Remove Spaces from a String

def remove_space(inp):
    return inp.replace(" ","")

if __name__=="__main__":
    string=input("Enter string:")

    print(f"String without space: {remove_space(string)}")