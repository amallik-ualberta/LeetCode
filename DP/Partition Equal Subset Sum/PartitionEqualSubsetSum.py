
def canPartition(nums):

	length = len(nums)

	if (length < 2):
		return False

	total = 0

	for num in nums:

		total = total + num

	if (total%2 != 0):

		return False

	dp = []

	for i in range (length):

		row = []

		for j in range (total//2 + 1):

			row.append(False)

		dp.append(row)

	for i in range (length):

		if (nums[i] == 0):

			dp[i][0] = True

	dp[0][nums[0]] = True

	for i in range(1, length):

		for j in range (1, total//2+1):

			dp[i][j] = dp[i-1][j]

			if (j - nums[i] >=0):

				dp[i][j] = dp[i][j] or dp[i-1][j-nums[i]]


	return dp[length-1][total//2]


	






def main():

	nums = []

	n = int(input("How many numbers?\n"))

	for i in range(n):

		element = int(input())

		nums.append(element)

	print(canPartition(nums))

if __name__ == "__main__":
    main()