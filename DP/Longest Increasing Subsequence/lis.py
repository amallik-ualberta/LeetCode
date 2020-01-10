
def lis(nums):


	length = len(nums)

	if (length == 0):

		return 0

	table = []


	for i in range (length):

		table.append(1)

	max_length = 1

	for i in range (1,length):

		for j in range (0,i):

			if (nums[i] > nums[j]):

				table[i] = max(table[i], table[j] +1)

				if (table[i] > max_length):

					max_length = table[i]

	

	return max_length






def main():

	nums = []

	n = int(input("How many numbers?\n"))

	for i in range(n):

		element = int(input())

		nums.append(element)

	print(lis(nums))

if __name__ == "__main__":
    main()