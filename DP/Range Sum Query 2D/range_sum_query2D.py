
class NumArray:
	"""docstring for NumArray"""
	def __init__(self, matrix):

		self.matrix = matrix

		length = len(matrix)

		self.table = []

		if (length > 0):

			row_length = len(matrix[0])

			for i in range (length): #Making all 0s

				row = []

				for j in range (row_length):

					row.append(0)

				self.table.append(row)


			for i in range (length): #Frist entry of every row is as it is from the matrix

				self.table[i][0] = self.matrix[i][0]

			for i in range (length): #We are doing row_wise sum for every row

				for j in range (1, row_length):

					self.table[i][j] = self.table[i][j-1] + self.matrix[i][j]


	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

		sum_region = 0

		for i in range (row1, row2+1):

			if (col1 == 0):

				sum_region += self.table[i][col2]

			else :

				sum_region += self.table[i][col2] - self.table[i][col1-1]

		return sum_region
		





def main():

	matrix = []

	m = int(input())

	n = int(input())


	for i in range(m):

		row = []

		for j in range (n):

			element = int(input())

			row.append(element)

		matrix.append(row)

	obj = NumArray(matrix)

	print(obj.sumRegion(2,1,4,3))

if __name__ == "__main__":
    main()