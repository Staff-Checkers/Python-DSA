# GCD USING EUCLIDEAN ALGORITHM

def gcd(a, b):

	if b==0:
		return a  
	else:
		return gcd(b, a%b)   

# TIME COMPLEXITY - O(log(min(a, b)))

# EUCLIDEAN ALGORITHM 

# EXAMPLES  
# print(gcd(2, 5)) -> 1 
# print(gcd(10, 2)) -> 2 

# CONTRIBUTOR - Hridyansh Pareek(github.com/WORLDSAVER)