
def findSubstringInWraproundString(p):

	length = len(p)

	if (length < 2):
		return length

	pre = p[0]

	pre_val = ord(pre)-ord('a')

	dp = []

	for i in range(26):
		dp.append(0)

	dp[pre_val] = 1

	count = 1
	for i in range(1,length):

		cur = p[i]

		cur_val = ord(cur)-ord('a')

		if ((pre_val + 1) %26 == cur_val):

			count += 1
			dp[cur_val] = max(dp[cur_val], count)

		else:

			count = 1
			dp[cur_val] = max(dp[cur_val], 1)

		pre = cur

		pre_val = cur_val

	return sum(dp)






def main():


	p = str(input("Enter String\n"))

	print(findSubstringInWraproundString(p))

if __name__ == "__main__":
    main()