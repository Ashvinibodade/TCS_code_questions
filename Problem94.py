# Find the Position of a Substring within a String

def find_Position(str1,str2):
    return str1.find(str2)

if __name__=="__main__":
    str1=input("Enter string:")
    str2=input("Enter substring:")

    print(find_Position(str1,str2))