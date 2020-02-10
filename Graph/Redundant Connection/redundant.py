
class DisjointSet():
	"""docstring for DisjointSet"""
	def __init__(self, n):
		
		self.parents = []

		self.rank = []

		for i in range (n):

			self.parents.append(i)

			self.rank.append(0)

	def find (self, x):

		if (self.parents[x] == x):

			return x

		self.parents[x] = self.find(self.parents[x]) #path compression

		return self.parents[x]


	def union(self,x, y):

		parentx = self.find (x)

		parenty = self.find (y)

		if (parentx == parenty):

			return False

		if (self.rank[x] >= self.rank[y]): #union by rank

			if(self.rank[x] == self.rank[y]):

				self.rank[x] += 1

			self.parents[parenty] = parentx

		else:

			self.parents[parentx] = parenty
		

		return True

def findRedundantConnection(edges):

	ds = DisjointSet(len(edges) + 1)

	for edge in edges :

		if (ds.union(edge[0], edge[1]) == False):

			answer = edge

	return answer
	

def main():


	number_of_edges = int(input())

	edges = []

	for i in range (number_of_edges):

		row = []

		for j in range(2):

			element = int(input())

			row.append(element)

		edges.append(row)


	print(findRedundantConnection(edges))




if __name__ == "__main__":
    main()