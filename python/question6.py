#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def findSquareSumsDifference(number):
	sumOfSquares = number * (number+1) * (2*number+1)/6 #Sum of squares of numbers i.e. 1^2+2^2+3^2+...n^2 = n*(n+1)*(2n+1)/6
	sumOfNumbers = number * (number+1)/2 #Sum of numbers from 1 to n i.e. (1+2+3+...n) = n*(n+1)/2
	squareOfSum = sumOfNumbers*sumOfNumbers #Calculate squares of sum
	result = squareOfSum-sumOfSquares
	print("%.0f" % result)

findSquareSumsDifference(20)