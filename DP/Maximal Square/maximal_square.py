
def maximal_square(matrix):

	rows = len(matrix)

	if (rows == 0):

		return 0

	columns = len(matrix[0])

	table = []

	for i in range(rows + 1):

		row = []

		for j in range (columns + 1):

			row.append(0)

		table.append(row)

	max = 0

	for i in range (1, rows + 1):

		for j in range (1, columns + 1):

			if (matrix[i-1][j-1] == '1'):

				table[i][j] = min(table[i-1][j-1], table[i-1][j], table[i][j-1]) + 1
				
				if (table[i][j] > max):

					max = table[i][j]



	return max*max





def main():

	rows = int(input())

	columns = int(input())

	matrix = []

	for i in range (rows):

		row = []

		for j in range (columns):

			element = str(input())

			row.append(element)

		matrix.append(row)




	print(maximal_square(matrix))

if __name__ == "__main__":
    main()