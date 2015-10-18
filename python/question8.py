#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

def findMaxConsecutiveProduct(number):
	numArr = [int(k) for k in str(number)] #Convert the number into string and finally to int array
	arrLen = len(numArr)
	resultArr = []
	currentMax = 0
	nextIterOk = False
	multResult = 1
	multArr = []
	for i in range(0,arrLen-12): #Iterate until i+12 is smaller than aray length
		zeroFound = False
		if nextIterOk: #Is it safe to shift 1 to the right 
			multResult /= numArr[i-1] #Divide the multiplication of 13 numbers by the previous array's first number and multiply by our new 13th number
			multResult *= numArr[i+12] # Example for 4 tuple calculation: [2,3,4,5,6] First 4 numbers ->120 Shift 1 to the right means dividing it by 2 and multiply by 6 -> 360
			del multArr[0] #Delete the shifted out int from the list
			multArr.append(numArr[i+12]) #Add the shifted in int to the list
			if multResult > currentMax:
				currentMax = multResult
				resultArr = multArr
		else:						#We have a zero on the left so we can't make division. Multiply all the numbers in the row
			for j in range(i,i+13):
				if numArr[j] == 0: #If we encounter zero, stop and break
					zeroFound = True
					break
				else:
					multResult *=numArr[j]
					multArr.append(numArr[j])
			if zeroFound: #Shift until we reach the zeroth term. When the loop continues, it will go on with the i+1 th term.
				i = j
			elif multResult > currentMax: #If we have a new max value, make the updates accordingly.
				currentMax = multResult
				resultArr = multArr

		if zeroFound: #We have zero in our array and we will shift i to next value in array. So in the next iteration we won't be able to divide by i-1th term since it is zero
			nextIterOk = False
			multResult = 1 #Reset multipliers and multiplication array
			multArr = []
		elif i+13 < len(numArr) and numArr[i+13] != 0: #When we shift right, the last term in array shouldn't be zero and we shouldn't pass the boundaries also.
			nextIterOk = True
		else:              #We either reached the boundaries or the last item in the array will be zero when we shift to the right
			nextIterOk = False
			multResult = 1
			multArr = []

	print ("%.0f" % currentMax) 
	print(resultArr)

findMaxConsecutiveProduct(96983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
