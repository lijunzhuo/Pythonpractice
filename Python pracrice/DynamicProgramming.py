#      python D:\Pythonpractice\DynamicProgramming.py

#Find the biiggest sum of several elements of an array that each element ftom the array cannot be togetehr
#ex: [1,2,1,4,6] biggest sum is 8 ; 

#import numpy as np

def optimalsubproblem(position, array):
	position = int(position) 
	if  position == 0:
		return array[0]
	elif position == 1:
		return max(array[0], array[1])
	else:
		temp1 = optimalsubproblem(position - 2, array) + array[position]
		temp2 = optimalsubproblem(position - 1, array)
		return max(temp1, temp2)


#optimization: big O of above function is 2^n, which is very slow, we can create a 
# list to store all values of subproblems. So if we do not need to calculate repeatly.

def optimal(oparray):
	#solution = np.zeros(len(array))
	#opposition = int(opposition)
	solution = []
	for i in range (len(oparray)):
		solution.append(0)
	#print(solution)
	solution[0] = oparray[0]
	solution[1] = max(oparray[0], oparray[1])
	for i in range (2, len(array), 1):
		optemp1 = solution[i - 2] + oparray[i]
		optemp2 = solution[i - 1]
		solution[i] = max(optemp1, optemp2)
	print(solution)
	return solution





if __name__ == "__main__":
	array = [1, 2, 4, 1, 7, 8, 3]
	position = input("Please enetr position: ")
	position = int(position) -1
	if position > len(array):
		print("input is out of range")
	maxnumber = optimalsubproblem(position, array)
	solution = optimal(array)
	print("none optimal solution is :" + str(maxnumber))
	print("optimal solution is :" + str(solution[position]))






