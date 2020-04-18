
def combinationSum4(nums, target):

	length = len(nums)



	if (length == 0 and target > 0):

		return 0

	if (target == 0):

		return 1

	dp = []

	for i in range (target+1):

		dp.append(0)

	nums.sort()

	dp[0] = 1

	for i in range (1, target + 1):

		for j in range (length):

			if (nums[j] > i):

				break

			dp[i] += dp[i - nums[j]]

	return dp[target]
	



def main():

	n = int(input("How many numbers?\n"))

	nums = []

	for i in range(n):

		element = int(input())

		nums.append(element)

	target = int(input("Enter Target\n"))



	print(combinationSum4(nums,target))

if __name__ == "__main__":
    main()