#PRODUCT OF NUMBERS

def productOfDigits(N):

	if N//10==0:
		return N  
	else:
		return N%10 * productOfDigits(N//10)

# TIME COMPLEXITY - O(M) where M is length of digits of number N.
# SPACE COMPLECITY - O(M) where M is length of digits of number N.

# EXAMPLES 
# print(productOfDigits(123)) -> 6 
# print(productOfDigits(222)) -> 8

# CONTRIBUTOR - Hridyansh Pareek(github.com/WORLDSAVER)