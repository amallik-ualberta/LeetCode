
def unique_paths2(obstacleGrid):

	m = len(obstacleGrid)

	n = len(obstacleGrid[0])

	if (obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1): #if start of finish is obstacle

		return 0;

	obstacleGrid[0][0] = 1

	flag = 0

	for i in range (1,m):

		if (obstacleGrid[i][0] == 1):

			obstacleGrid[i][0] = 0

			flag = 1

			continue

		if (flag == 0):

			obstacleGrid[i][0] =1

		else :

			obstacleGrid[i][0] =0

	flag = 0

	for j in range (1,n):

		if (obstacleGrid[0][j] == 1):

			obstacleGrid[0][j] = 0

			flag = 1

			continue

		if (flag == 0):

			obstacleGrid[0][j] = 1

		else :

			obstacleGrid[0][j] = 0


	for i in range (1,m):

		for j in range (1,n):

			if (obstacleGrid[i][j] == 1):

				obstacleGrid[i][j] = 0

				continue

			obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]


	return obstacleGrid[m-1][n-1]



def main():

	m = int(input())

	n = int(input())

	obstacleGrid = []


	for i in range (m):

		row = []

		for j in range (n):

			row.append(int(input()))

		obstacleGrid.append(row)


	print(unique_paths2(obstacleGrid))

if __name__ == "__main__":
    main()