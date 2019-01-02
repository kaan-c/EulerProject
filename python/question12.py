import math

#Gets the current  triangular number and the next number to be added to this to obtain 
#the next triangular number. Calculates the number of divisors by getting the common denominator and 
#multiplying it with the divisors of the sum of the remaining non-divisible quotients. i.e. 28,8 -> 4* (2+7) 
def numOfDivisors(x, y):
	i = 2
	mult = 1
	num = 0
	while x>i and y>i:
		while x%i == 0 and y%i == 0:
			x = x/i
			y = y/i
			num = num+1
		mult = mult * (num+1)
		num = 0
		i = i+1
		
	return mult*divisors(x+y)
	
def divisors(n):
    totalExpn = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            totalExpn +=2
        else:
            continue
    return totalExpn			

def findNumOfDivisorsOver(n):
	i = 2
	triangNum = 1
	while(1):
		numOfDivs = numOfDivisors(triangNum,i) 
		triangNum = triangNum + i
		if numOfDivs > n:
			break
		else:
			i = i+1
	print(triangNum)

findNumOfDivisorsOver(500)
		
		