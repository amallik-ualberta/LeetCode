
def integer_break(n):

	table = []

	for i in range (n+1):

		table.append(0)


	for i in range (1, n+1):

		for j in range (1, i):

			table[i] = max(table[i], j * (i-j), table[j] * (i-j))

			#j* (i-j) means just picking the numbers such as 6*4 for 10
			#dp[j] * (i-j) means picking j as a sum of numbers suuch as 3*3*4 for 10


	return table[n]

def main():

	n = int(input())

	print(integer_break(n))

if __name__ == "__main__":
    main()