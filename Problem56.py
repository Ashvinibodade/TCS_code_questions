# Calculate the Area of the Circle

def calcArea(radius):
    return 3.14 *radius*radius

if __name__=="__main__":
    radius=int(input("Enter radius:"))

    print(calcArea(radius))