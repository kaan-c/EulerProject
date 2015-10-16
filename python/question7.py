#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def findNthPrime(n):
	firstPrime = 2 #First prime number
	arr = [] #Array that incrementally holds the prime numbers
	arr.append(firstPrime) 
	if n == 1:
		return firstPrime
	else:
		k = n-1 #Decrease by 1 since we know the first prime number
		currentNumber = firstPrime+1 #Starting from 3 we will compare only the odd numbers since all prime numbers greater than 2 are odd.
		while k > 0: 
			divisorFound = False 
			for i in range(0,len(arr)): #Search the primes array if there exist a divisor of our current number
				if currentNumber%arr[i] == 0: #If there exist a divisor, stop the loop and ignore the number 
					divisorFound = True
					break
			if not divisorFound: #If none of the prime numbers can divide the current number, then it is a prime number
				arr.append(currentNumber) #Add our new number to the primes array
				k -= 1 #Step down by 1 since we found a prime number
			currentNumber += 2 #Continue with the next odd number
		print (arr[-1])

findNthPrime(10001)