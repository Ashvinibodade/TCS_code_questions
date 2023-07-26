# Remove all vowels from the String

def find(inp):
    l=['a','e','i','o','u']
    str_ans=""

    for i in range(len(inp)):
        if inp[i].lower() not in l:
            str_ans=str_ans+inp[i]

    return str_ans

if __name__=="__main__":
    inp=input("Enter string:")

    print(f"Output string: {find(inp)}")