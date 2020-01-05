
def house_robber2(nums):


	length = len(nums)

	if (length == 0):

		return 0

	if (length == 1):

		return nums[0]

	if (length == 2):

		return max(nums[0], nums[1])

	table = []

	table.append(nums[0])

	table.append(max(nums[0], nums[1]))


	for i in range (2, length-1):

		table.append(max(table[i-2] + nums[i], table[i-1]))

	

	other_table = []

	#in case of other table, we are leaving out the first element. That's why everying with nums will be + 1

	other_table.append(nums[1])

	other_table.append(max(nums[1], nums[2]))

	for i in range (2, length-1):

		other_table.append(max(other_table[i-2] + nums[i+1], other_table[i-1]))


	return max(table[length-2], other_table[length-2])






def main():

	nums = []

	n = int(input("How many numbers?\n"))

	for i in range(n):

		element = int(input())

		nums.append(element)

	print(house_robber2(nums))

if __name__ == "__main__":
    main()