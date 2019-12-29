
def min_sum(triangle):

	
	table = []

	m = len(triangle)

	n = len(triangle[m-1])

	

	for i in range(n):

		table.append(triangle[m-1][i])

	

	for i in range(m-2,-1,-1): #from the 2nd last to first row

		for j in range(len(triangle[i])):

			table[j] = triangle[i][j] + min(table[j],table[j+1])

		

	return table[0]



def main():

	n = int(input())

	matrix = []

	count = 1

	for i in range(n):

		row = []

		for j in range(i+1):

			element = int(input())

			row.append(element)

		matrix.append(row)

		count +=1




	print(min_sum(matrix))

if __name__ == "__main__":
    main()