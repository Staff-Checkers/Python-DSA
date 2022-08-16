# SUM OF DIGITS 

N = int(input())

def sumOfDigits(N):

	if N==0:
		return N   
	else:
		return N%10 + sumOfDigits(N//10)

print(sumOfDigits(N))

# TIME COMPLEXITY - O(M) where M is the number if digits in a number 


# EXAMPLES 
# print(sumOfDigits(123)) -> 6 
# print(sumOfDigits(543)) -> 12


# CONTRIBUTOR - Hridyansh Pareek(github.com/WORLDSAVER)