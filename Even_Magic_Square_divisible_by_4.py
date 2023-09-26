
def Even_magic_div4(N):

	matrix = [[0 for item in range(N)] for item in range(N)]

	num = 1
	for item in range(N):
		for elements in range(N):
			if (item == 0 or (item%4 == 0) or ((item+1)%4 == 0)) and (elements == 0 or (elements%4 == 0) or ((elements+1)%4 == 0)):
				matrix[item][elements] = num
			else:
				if (item != 0 and (item%4 != 0) and ((item+1)%4 != 0)) and (elements != 0 and (elements%4 != 0) and ((elements+1)%4 != 0)):
					matrix[item][elements] = num
			num += 1

	matrix = [item[::-1] for item in matrix]
	matrix = matrix[::-1]

	num = 1
	for item in range(N):
		for element in range(N):
			if matrix[item][element] == 0:
				matrix[item][element] = num
			num += 1

	matrix = [item[::-1] for item in matrix]
	matrix = matrix[::-1]

	for item in matrix:
		print(*item)
		print("-------------------------------------")
