# Find all Palindrome Numbers in a given range

def isPalindrome(n):
    if str(n)[::-1]==str(n):
        return 1
    return 0

if __name__=="__main__":
    min=int(input("Enter min:"))
    max=int(input("Enter max:"))

    for i in range(min,max):
        if (isPalindrome(i)):
            print(i)