# Sum of the Numbers in a String

def find_sum(string):
    temp=''
    sum=0

    for i in string:
        if i.isdigit():
            temp+=i
        else:
            sum+=int(temp)
            temp="0"

    return sum+int(temp)

if __name__=="__main__":
    string=input("Enter string:")

    print(f"Output string : {find_sum(string)}")