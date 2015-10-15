#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isAllNumsEqual(numArray):
	arrayLength = len(numArray)
	for j in range(0,arrayLength-1):
		if j+1 < arrayLength: #Make sure we dont get out of array boundaries
			if numArray[j] != numArray[j+1]: #Compare 2 values. They should be equal.
				return False
	return True


def findSmallestCommonMultiplier(number):
	numArr = []
	divisors = 1
	primeDivisor = 2
	for i in range(2,number): #Put numbers consecutively in numArr. 1 is omitted since we don't need it.
		numArr.append(i)
	while 1:
		divisibleNumFound = False
		for j in range(0,number-2): #Trace all numbers in array
			if numArr[j]%primeDivisor == 0: #Divide the ones that are divisible by current prime divisor
				numArr[j] = numArr[j] / primeDivisor
				divisibleNumFound = True
		if divisibleNumFound: #We have a divider, so, multiply it with the divisor.
			divisors *= primeDivisor
		elif isAllNumsEqual(numArr): #Check whether all of the values are 1, if so, print the result and stop
			print (divisors)
			return 
		else:
			if primeDivisor > 2: #Set the next divisor. If 2, continue with 3, else increment by 2 to go on dividing with the odd numbers
				primeDivisor+=2
			else:
				primeDivisor=3

findSmallestCommonMultiplier(20)