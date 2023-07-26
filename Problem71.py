# Count number of vowels, consonants, spaces in String

def solve(str,n):
    vowel=0
    consonant=0
    space=0

    str=str.lower()

    for i in range(n):
        if (str[i]=='a') or (str[i]=='e') or (str[i]=='i') or (str[i]=='o') or (str[i]=='u'):
            vowel+=1
        elif str[i]>='a' and str[i]<='z':
            consonant+=1
        elif str[i]==' ':
            space+=1

    print("Vowels:",vowel)
    print("Constants:",consonant)
    print("whitespace:",space)

if __name__=="__main__":
    str=input("Enter string:")
    n=len(str)
    solve(str,n)