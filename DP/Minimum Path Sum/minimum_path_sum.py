
def min_path_sum(grid):


	m = len(grid)

	n = len(grid[0])

	#first cell remains as it is
	
	for i in range (1,m):

		grid[i][0] += grid[i-1][0]

	for j in range (1,n):

		grid[0][j] += grid[0][j-1]


	for i in range (1,m):

		for j in range (1,n):


			grid[i][j] += min(grid[i-1][j], grid[i][j-1])


	return grid[m-1][n-1]



def main():

	m = int(input())

	n = int(input())

	grid =[]

	for i in range(m):

		row = []

		for j in range(n):

			row.append(int(input()))

		grid.append(row)

	print(min_path_sum(grid))

if __name__ == "__main__":
    main()