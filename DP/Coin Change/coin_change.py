
def coin_change(coins, amount):

	length = len(coins)

	if (length == 0 or amount == 0):

		return 0

	coins.sort() #sorting is only required to improve runtime for average case

	table = []

	for i in range (amount+1):

		table.append(amount+1)


	table[0] = 0


	for i in range(1, amount+1):

		for j in range (length):

			if(i >= coins[j]):

				table[i] = min(table[i], 1 + table[i-coins[j]])

			else:

				break

	if(table[amount] > amount):

		return - 1

	return table[amount] 




def main():

	n = int(input())

	coins = []

	for i in range (n):

		element = int(input())

		coins.append(element)

	amount = int(input())

	print(coin_change(coins, amount))

if __name__ == "__main__":
    main()