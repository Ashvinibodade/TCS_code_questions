# Remove brackets from an algebraic expression

def removeBrackets(inp_string):
    out_string=""
    for i in inp_string:
        if i=='(' or i==')' or i=='{' or i=='}' or i=='[' or i==']':
            pass
        else:
            out_string=out_string+i

    return out_string

if __name__=="__main__":
    string=input("Enter string:")

    print(f"Output string : {removeBrackets(string)}")