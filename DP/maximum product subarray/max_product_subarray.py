
def maxProductSubarray(nums):


	length = len(nums)

	current_max = []

	current_min = []

	current_max.append(nums[0])

	current_min.append(nums[0])

	final_max = nums[0];


	for i in range (1,length):

		current_max.append(max(max(nums[i], current_max[i-1]*nums[i]), current_min[i-1]* nums[i]))

		current_min.append(min(min(nums[i], current_max[i-1]*nums[i]), current_min[i-1]* nums[i]))

		if (current_max[i] > final_max):

			final_max = current_max[i]



	return final_max






def main():

	nums = []

	n = int(input("How many numbers?\n"))

	for i in range(n):

		element = int(input())

		nums.append(element)

	print(maxProductSubarray(nums))

if __name__ == "__main__":
    main()