
def stock(prices):

	max_profit = 0

	min_price = float('inf')


	length = len(prices)

	for i in range (length):

		if (prices[i] < min_price):

			min_price = prices[i]

		max_profit = max(max_profit, prices[i] - min_price)


	return max_profit




def main():

	n = int(input())

	prices = []

	for i in range (n):

		element = int(input())

		prices.append(element)

	print(stock(prices))

if __name__ == "__main__":
    main()