#       python D:Pythonpractice\KMP.py



#match = ["A", "B", "A", "B", "C"]
#longlist = ["A", "B", "A", "A", "C", "A", "B", "A", "B", "C", "A", "C"]
#[-1, 0,0,1,2]

matchlist = ["A", "B", "A", "B", "C", "A", "A"]
present = ["A", "C", "B", "A", "B", "A", "A", "A", "B", "A", "B", "C", "A", "A", "A", "C"]







def prefixindex(match):
	count = 2
	prefix = []
	temp1 = []
	temp1.append(match[0])
	prefix.append(temp1)
	while len(prefix[-1]) != len(match) - 1:
		temp2 = []
		for i in range (count):
			temp1 = match[i]
			temp2.append(temp1)
		count = count + 1	
		prefix.append(temp2)
	#prefix.append(present)
	return prefix


def biggestcommonprefix(match):
	prefix = prefixindex(match)
	prefix_table = []
	prefix_table.append(0)
	temp = 0
	#prefix.pop(0)
	#print("prefix before pop is :" + str(prefix))
	while len(prefix) != 0:
		temp1 = prefix.pop(0)
		left = []
		right =[]
		count = []
		count.append(0)
		temp2 = []
		#print("prefix after pop is :" + str(prefix))
		for i in range ((len(temp1)) - 1):
			count.append(0)
			left.append(temp1[i])
			#print("left is: " + str(left))
			temp2.append(temp1[-i - 1])
			right = temp2[::-1]
			#print("right is: " + str(right))
			if left == right:
				count.append(i + 1)
		#print("the count is: " + str(count))
		prefix_table.append(max(count))
	#prefix_table.insert(1,0)

	return prefix_table

def matching(match,present):
	prefix_table = biggestcommonprefix(match)
	#print(prefix_table)
	tail = len(match) - 1
	head = 0
	matchposition = []
	found = False
	while tail <= len(present) - 1:
		count = 0
		matchposition = []
		for i in range (len(match)):
			if match[i] != present[head + i]:
				head = head + prefix_table[i] + 1
				tail = tail + prefix_table[i] + 1
				break
			else:
				count = count + 1
				matchposition.append(head + i)
		if count == len(match):
			found = True
			break

	return matchposition, found




if __name__ == "__main__":
	matchposition, found = matching(matchlist,present)
	#matchposiiton, found = matching(match, longlist)
	#print(matchposition)
	if found == False:
		print("CANNOT found the common sublist!!!")
	else: 
		print("Found the common sublist? " + str(found))
		print("position of common sublist: " + str(matchposition))













