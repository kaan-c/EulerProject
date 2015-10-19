#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Solution: With the given information it can be inferred that: 
# b = 500 - 500a / 1000-a  So since b is a natural number, 500*a should be divisible by 1000-a. Secondly, it must be ensured that a<b<c is true

def pythagoranTriplet():
	for a in range(1,1000):
		aDiff = 1000-a
		bComponent = (500*a) / aDiff
		bRemainder = (500*a) % aDiff
		b = 500-bComponent
		c = aDiff-b
		if bRemainder == 0 and b > 0: 
			if a < b and b < c:
				print ("a: %d, b: %d, c: %d" % (a,b,c))
				print ("The product is: %.0f" % (a*b*c))
				return

pythagoranTriplet()