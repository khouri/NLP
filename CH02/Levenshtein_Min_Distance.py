# https://www.geeksforgeeks.org/edit-distance-dp-5/
def min_edit_dist(source, target):

	rows = len(source) + 1
	print(rows)
	columns = len(target) + 1
	print(columns)
	print("--"*100)

	mat = [[0 for x in range(columns)] for x in range(rows)]
	print(len(mat))
	print(len(mat[0]))
	print("--" * 100)

	for col in range(1, rows):
		mat[col][0] = col
	print("--" * 100)
	print("--" * 100)

	for r in range(len(mat)):
		print(mat[r])
	print("--" * 100)
	print("--" * 100)
	for row in range(1, columns):
		mat[0][row] = row

	print("--" * 100)
	print("--" * 100)
	for r in range(len(mat)):
		print(mat[r])
	print("--" * 100)
	print("--" * 100)

	for col in range(1, columns):
		for row in range(1, rows):
			if source[row - 1] == target[col - 1]:
				cost = 0
			else:
				cost = 2

			mat[row][col] = min(
								mat[row - 1][col] + 1,
								mat[row][col-1] + 1,
								mat[row-1][col-1] + cost
								)

	return(mat)
pass
