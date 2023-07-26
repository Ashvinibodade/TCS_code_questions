# Check if two Strings are anagrams of each other

def find(str1,str2):
    str1=sorted(str1.lower())
    str2=sorted(str2.lower())

    print(str1,str2)

    for i in range(len(str1)):
        if str1[i] !=str2[i]:
            return False
        
    return True

if __name__=='__main__':
    string1=input("Enter first string:")
    string2=input("Enter second string:")

    if find(string1,string2):
        print("True")
    else:
        print("False")