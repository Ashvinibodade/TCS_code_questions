# Find word with highest number of repeated letters in string

def most_repeating_word(strg):
    words =strg.split()
    
    max_repeat_count = 0
    most_repeated_char=""
    for words1 in words:
        dict1 = {}
        for letter in words1:
            if letter not in dict1:
                dict1[letter] = 1
            else:
                dict1[letter] += 1
            if dict1[letter]> max_repeat_count:
                max_repeat_count = dict1[letter]
                most_repeated_char = letter
                result=words1

    if max_repeat_count>1:
        return result
    else:
        return -1


if __name__=="__main__":
    str=input("Enter string:")

    print(most_repeating_word(str))