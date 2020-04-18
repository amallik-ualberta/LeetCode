
def numberOfArithmeticSlices(A):

	length = len(A)

	if (length<3):

		return 0

	dp = []

	for i in range(length):

		dp.append(0)

	to_add = 1
	for i in range(2, length):

		if(A[i] - A[i-1] == A[i-1] - A[i-2]):

			dp[i] = dp[i-1] + to_add

			to_add += 1

		else:

			dp[i] = dp[i-1]

			to_add = 1


	return dp[length-1]



def main():

	n = int(input("How many numbers?\n"))

	A = []
	for i in range (n):

		element = int(input())

		A.append(element)

	print(numberOfArithmeticSlices(A))

if __name__ == "__main__":
    main()