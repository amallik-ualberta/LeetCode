
def maxSubarray(nums):


	length = len(nums)

	table = []


	table.append(nums[0])

	max = table[0]


	for i in range (1, length):

		if (table[i-1] + nums[i] > nums[i]):

			table.append(table[i-1]+nums[i])

		else :

			table.append(nums[i])


		if (table[i] > max):

			max = table[i]


	return max






def main():

	nums = []

	n = int(input("How many numbers?\n"))

	for i in range(n):

		element = int(input())

		nums.append(element)

	print(maxSubarray(nums))

if __name__ == "__main__":
    main()