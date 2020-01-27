
def largestDivisbleSubset(nums):

	
	length = len(nums)

	if (length < 2):

		return nums

	nums.sort()

	result = []

	table = []

	next_pointers = []

	for i in range (length):

		table.append(-1)

		next_pointers.append(-1)


	table[length - 1] = 1

	overall_max_length = 1

	overall_max_index = length - 1


	for i in range (length - 2, -1, -1):

		
		max_for_this_cell = 0

		for j in range (i+1, length, 1):

			
			if (nums[j] % nums[i] == 0):

				if (table[j] > max_for_this_cell):

					next_pointers[i] = j

				max_for_this_cell = max (max_for_this_cell, table[j])

				


		table[i] = 1 + max_for_this_cell

		if (overall_max_length < table[i]):

			overall_max_length = table[i]

			overall_max_index = i

	index = overall_max_index

	while (index != -1):

		result.append(nums[index])

		index = next_pointers[index]


	return result
	






def main():

	nums = []

	n = int(input("How many numbers?\n"))

	for i in range(n):

		element = int(input())

		nums.append(element)

	print(largestDivisbleSubset(nums))

if __name__ == "__main__":
    main()