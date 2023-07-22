# Sum of first N Natural Numbers

def sum_of_NN(n):
    sum=0
    # for i in range(1,n+1):
    #     sum+=i          we have complexity-o(n)

    sum=int(n*(n+1)/2)              #now we have complexity-o(1)
    return sum

if __name__=='__main__':
    num=int(input("Enter a natural number upto which u want to get the sum:"))

    print(f"The sum of first {num} natural number is : {sum_of_NN(num)}")