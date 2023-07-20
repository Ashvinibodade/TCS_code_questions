# Check is a number Palindrome or not

def checkPalindrome(n):
    if str(n)[::-1]==str(n):
        return 1
    return 0

if __name__=="__main__":
    n=int(input("Enter number:"))

    if (checkPalindrome(n)):
        print("Given number is palindrome")
    else:
        print("Given number is not palidrome")