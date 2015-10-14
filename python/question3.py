#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def findLargestPrimeFactor(number):
	if number <= 1:
		print ("Largest prime factor doesn't exist for that number")
		return
	i=2 #Smallest prime number
	while number>1:
		if number%i == 0: #Check if divisible by prime number
			largestPrimeFactor = i #Set as current largest prime factor
			number = number/i 	   #Divide by that number and continue loop
		elif i>2: #Increment by 1 for i=2 to continue checking with the odd numbers, otherwise add 2.
			i+=2
		else:
			i+=1
	print (largestPrimeFactor)

findLargestPrimeFactor(600851475143)