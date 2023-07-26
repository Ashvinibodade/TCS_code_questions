# Reverse a String

def reverse_string(inp_string):
    return inp_string[::-1]

if __name__=="__main__":
    string=input("Enter string:")

    print(f"Output string : {reverse_string(string)}")