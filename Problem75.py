# Remove characters from a string except alphabets

def find(string1):
    string2=""
    for i in string1:
        if ((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
            string2+=i

    return string2

if __name__=="__main__":
    string=input("Enter string:")

    print(f"Output string : {find(string)}")