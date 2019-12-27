
def climbing_stairs(n):

	if (n<=2):

		return n;

	table = []

	table.append(1)

	table.append(2)

	for i in range (2,n):

		table.append(table[i-1] + table[i-2])
	
	return table[n-1]



def main():

	n = int(input())

	print((n))

if __name__ == "__main__":
    main()