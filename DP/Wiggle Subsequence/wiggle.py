
def wiggle(nums):

	length = len(nums)

	if (length < 2):

		return length

	up = 1

	down = 1

	for i in range (1, length):

		if (nums[i] < nums[i-1]):

			down = up + 1

		elif (nums[i] > nums[i-1]):

			up = down + 1


	return max (up, down)

	






def main():

	nums = []

	n = int(input("How many numbers?\n"))

	for i in range(n):

		element = int(input())

		nums.append(element)

	print(wiggle(nums))

if __name__ == "__main__":
    main()