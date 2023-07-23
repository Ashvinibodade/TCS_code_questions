# Program to Add two fractions

def gcd(a, b):
	if (a == 0):
		return b
	return gcd(b % a, a)

def lowest(den3, num3):
	common_factor = gcd(num3, den3)

	den3 = int(den3 / common_factor)
	num3 = int(num3 / common_factor)
	print(num3, "/", den3)

def addFraction(num1, den1, num2, den2):
	den = gcd(den1, den2)
	den3 = (den1 * den2) / den
	
	num3 = ((num1) * (den3 / den1) +
			(num2) * (den3 / den2))
	
	lowest(den3, num3)

if __name__=="__main__":
	num1=int(input("Enter num1:"))
	den1=int(input("Enter den1:"))
	num2=int(input("Enter num2:"))
	den2=int(input("Enter den2:"))
	
print(num1, "/", den1, " + ", num2, "/",den2, " is equal to ", end = "")
addFraction(num1, den1, num2, den2)

