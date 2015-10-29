#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import math
def findPrimesUpTo(number):
	if number<2: #Check for the lower limit values
		print(0)
		return
	elif number <= 3:
		print(2)
		return

	primesArr = [2,3] #Since we will only check numbers having the form 6k+1 and 6k-1, we are adding the prime numbers which can't be written in those forms in advance.
	primesArrLen = 2
	sqrtNumber = math.sqrt(number) #First we will find the prime divisors of the number in order to apply the Sieve of Eratosthenes. 
								   #The maximum limit for the prime divisors of a number is its square root.
	i=5		#Starting from 5 since we eliminated 2 and 3
	while i < sqrtNumber: #Search for the numbers which can't be divided by any of our prime numbers list and add them to the prime numbers list.
		primesArrLen = len(primesArr)
		divisorFound = False
		for j in range(0,primesArrLen): #Searching our prime numbers array
			if i%primesArr[j]==0:       #Skip any numbers that are divisible by a prime number
				divisorFound=True
				break
		if not divisorFound:
			primesArr.append(i)
		if i%6==5: #Since prime numbers have the form 6k+1 and 6k-1, increment the loop counter accordingly.
			i+=2
		elif i%6==1:
			i+=4

	numArr = [0 for h in range(0,number+1)] #Sieve of Eratosthenes algorithm. The array of zeros. We will mark the composite numbers as 1
	for k in range(0,primesArrLen):         #Loop in all prime numbers list
		m = primesArr[k]
		x=0
		while True:
			multValue = m*(m+x)		#Starting from its square, mark all of its multipliers with 1 to mark them as composite number. Ex: for 7 -> 49,56,63,70...
			if multValue > number:  #Limit control
				break
			numArr[multValue] = 1
			x +=1

	sum = 5 #Start with sum=2+3=5
	for y in range(5,number,2): #Check only odd numbers, since there doesn't exist any even prime number except 2.
		if numArr[y] == 0:
			sum += y
	print(sum)

findPrimesUpTo(2000000)