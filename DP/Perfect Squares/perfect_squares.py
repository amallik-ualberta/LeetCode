
def perfect_squares(n):

	if (n<=0):

		return 0;

	table = []

	for i in range (n+1):

		table.append(n)

	table[0] = 0

	for i in range (1, n+1):

		j = 1

		while (j*j <= i):

			table[i] = min (table[i], table[i-j*j] +1)

			j += 1


	return table[n]




def main():

	n = int(input())

	print(perfect_squares(n))

if __name__ == "__main__":
    main()