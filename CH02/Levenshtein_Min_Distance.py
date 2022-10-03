
def min_edit_dist(source, target):

	rows = len(source) + 1
	columns = len(target) + 1
	mat = [[0 for x in range(columns)] for x in range(rows)]

	for col in range(1, rows):
		mat[col][0] = col

	for row in range(1, columns):
		mat[0][row] = row

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
