# SUM OF DIGITS 


def sumOfDigits(N):

	if N==0:
		return N   
	else:
		return N%10 + sumOfDigits(N//10)


# TIME COMPLEXITY - O(M) where M is the number off digits in a number 
# SPACE COMPLEXITY - O(M) where M is the number of digts in a number

# EXAMPLES 
# print(sumOfDigits(123)) -> 6 
# print(sumOfDigits(543)) -> 12


# CONTRIBUTOR - Hridyansh Pareek(github.com/WORLDSAVER)