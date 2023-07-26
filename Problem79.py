# Capitalize first and last character of each word of a string

def convert(s):
    result=""
    for i in s.split():
        if len(i)>1:
            result =result + i[0].upper()+ i[1:-1] + i[-1].upper() + " "
        else:
            result=result+i[0].upper() + " "
        
    return result

if __name__=="__main__":
    string=input("Enter string:")

    print(f"Output string : {convert(string)}")