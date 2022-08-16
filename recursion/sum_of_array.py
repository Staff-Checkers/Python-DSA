# SUM OF ARRAY USING RECURSION

def sumArray(A):

	if len(A)==1:
		return A[0]
	else:
		return A[0] + sumArray(A[1:])

# TIME COMPLEXITY - O(N) where N is the length of the array
# SPACE COMPLEXITY - O(N)


# EXAMPLES 
# print(sumArray([1, 2, 3])) -> 6
# print(sumArray([0, 9, 4, 5])) -> 18


# CONTRIBUTOR - Hridyansh Pareek(github.com/WORLDSAVER)