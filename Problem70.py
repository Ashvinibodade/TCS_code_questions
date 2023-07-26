# Check if the given String is Palindrome or not

def chcekPalindrome(st):
    left = 0
    right = len(st)-1
    while left < right:
        if not st[left].isalnum():
            left += 1
        elif not st[right].isalnum():
            right -= 1
        elif st[left].lower() != st[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


if __name__=="__main__":
    str=input("Enter string:")

    if chcekPalindrome(str):
        print("Palindrome")
    else:
        print("Not Palindrome")