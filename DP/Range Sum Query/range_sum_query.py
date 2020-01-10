
class NumArray:
	"""docstring for NumArray"""
	def __init__(self, nums):

		self.nums = nums

		length = len(nums)

		self.table = []

		if (length > 0):

			self.table.append(nums[0])

		for i in range (1, length):

			self.table.append(self.table[i-1] + nums[i])

	def sumRange(self, i: int, j: int) -> int:

		if (i==0):

			return self.table[j]

		return self.table[j] - self.table[i-1]
		





def main():

	nums = []

	n = int(input("How many numbers?\n"))

	for i in range(n):

		element = int(input())

		nums.append(element)

	obj = NumArray(nums)

	print(obj.sumRange(1,3))

if __name__ == "__main__":
    main()