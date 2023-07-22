# Check if given year is a leap year or not

def leapYear(yr):
    if (((yr%4==0) and (yr%100!=0)) or (yr%400 ==0)):
        return True
    return False

if __name__=="__main__":
    year=int(input("Enter year :"))

    if (leapYear(year)):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")