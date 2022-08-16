# BUBBLE SORT 

def bubbleSort(A):

	for i in range(len(A)):
		for j in range(len(A) - i - 1):
			if A[j+1]<A[j]:
				A[j], A[j+1] = A[j+1], A[j] 

	return A  

# TIME COMPLEXITY - O(N^2)
# SPACE COMPLEXITY - O(1)

# EXAMPLES 
# print(bubbleSort([5, 4, 3, 2, 6])) -> [2, 3, 4, 5, 6]
# print(bubbleSort([1, 2, 3, 4, 6])) -> [1, 2, 3, 4, 6]

# CONTRIBUTOR - Hridyansh Pareek(github.com/WORLDSAVER)