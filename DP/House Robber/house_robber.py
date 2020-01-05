
def house_robber(nums):


	length = len(nums)

	if (length == 0):

		return 0

	table = []

	if (length >= 1):

		table.append(nums[0])


	if (length >= 2):

		table.append(max(nums[0], nums[1]))


	for i in range (2,length):

		table.append(max(table[i-2] + nums[i], table[i-1]))



	return table[length-1]






def main():

	nums = []

	n = int(input("How many numbers?\n"))

	for i in range(n):

		element = int(input())

		nums.append(element)

	print(house_robber(nums))

if __name__ == "__main__":
    main()