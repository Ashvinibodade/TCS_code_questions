# Express given number as Sum of Two Prime Numbers

def sum(num):
    arr = []
    # find prime numbers
    if num<=1:
        return 0
    for i in range(2, num):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
        # append prime numbers to array
        if flag == 0:
            arr.append(i)
    # possible combinations
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            # if condition is True Print numbers
            if arr[i] + arr[j] == num:
                return 1
                break
    return 0

if __name__=="__main__":
    num=int(input("Enter num:"))

    if sum(num):
        print("YES")
    else:
        print("NO")