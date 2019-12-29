
class TreeNode:

	def __init__(self, x):

		self.val = x

		self.left = None

		self.right = None

def unique_bst2(start, end):

	treelist = []

	if (start > end):

		treelist.append(None)

		return treelist

	for i in range (start, end+1):

		leftlist = unique_bst2(start, i-1)

		rightlist = unique_bst2(i+1, end)


		for j in range (len(leftlist)):

			for k in range (len(rightlist)):

				node = TreeNode(i)

				node.left = leftlist[j]

				node.right = rightlist[k]

				treelist.append(node)


	return treelist


def preorder(root):

	if (root != None):

		print(root.val ," ", end ='')

		preorder (root.left)

		preorder (root.right)



def main():

	n = int(input())

	a = unique_bst2(1,n)

	for i in range (len(a)):

		preorder(a[i])

		print()

if __name__ == "__main__":
    main()