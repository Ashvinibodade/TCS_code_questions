# Find the ASCII value of a character

def find_Ascii_val(inp):
    return ord(inp)

if __name__=="__main__":
    inp=input("Enter character to get ascii value:")

    print(f"ASCII value of {inp} is {find_Ascii_val(inp)}")