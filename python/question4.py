#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindromeNumber(number):
	numberString = str(number) #Convert the number to string and compare with the reversed string
	return numberString == numberString[::-1]

def findPalindromeNumber():
	i=999
	j=999
	currentMax = 0 #Current maximum result
	while i > 99: #Both numbers should have 3 digits
		while j > 99:
			currentNumber = i*j
			if isPalindromeNumber(currentNumber):
				if currentNumber > currentMax: #If the result is greater than our current maximum, update it with the new maximum
					currentMax = currentNumber
					maxI = i
					maxJ = j
			j-=1
		i-=1
		j=i #Set i to j to prevent duplicate multiplications e.g. 999*998 and 998*999

	print (currentMax)
	print(maxI,maxJ)

findPalindromeNumber()
		