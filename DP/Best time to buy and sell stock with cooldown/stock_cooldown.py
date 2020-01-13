
def stock_cooldown(prices):

	length = len(prices)

	if (length < 2):

		return 0

	buy = []

	sell = []

	buy.append(-prices[0])

	buy.append(max(-prices[0], -prices[1]))

	sell.append(0)


	for i in range(1, length):

		sell.append(max(sell[i-1], buy[i-1] + prices[i])) #Max of dont sell and sell the previous max stock

		if (i-2 >=0):

			buy.append(max(buy[i-1], sell[i-2] - prices[i])) #max of dont buy and buy with 1 cooldown


	return sell[length - 1] 




def main():

	n = int(input())

	prices = []

	for i in range (n):

		element = int(input())

		prices.append(element)

	print(stock_cooldown(prices))

if __name__ == "__main__":
    main()