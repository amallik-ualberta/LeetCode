
def unique_bst(n):


	table = []

	table.append(1) #for 0 elements, there is only 1 tree. that is empty tree

	table.append(1) #for 1 element, there is 1 tree

	for i in range (2,n+1):

		to_append = 0

		for j in range (0,i):

			to_append += table[j] * table[i-j-1] #suppose n = 5 and keys ar 11,12,13,14,15. Take each of them as root and simulate. Catalan number

		table.append(to_append)
		
	
	return table[n]



def main():

	n = int(input())

	print(unique_bst(n))

if __name__ == "__main__":
    main()