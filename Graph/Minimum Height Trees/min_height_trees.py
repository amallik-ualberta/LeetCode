
from collections import deque

def findminheighttrees(n, edges):

	if (n == 0):

		return [];

	result = []

	if (n <= 2):

		for i in range (n):

			result.append(i)

		return result

	adj_list = {}

	for i in range (n):

		adj_list[i] = []

	node_queue = deque()

	degree = []

	for i in range (n):

		degree.append(0)

	for i in range (len(edges)):

		adj_list[edges[i][0]].append(edges[i][1])

		adj_list[edges[i][1]].append(edges[i][0])

		degree[edges[i][0]] += 1

		degree[edges[i][1]] += 1

	for i in range (n):

		if (degree[i] == 1):

			node_queue.append(i)

	while (n > 2):

		length = len(node_queue)

		for x in range (length):

			a = node_queue.popleft()

			n -= 1

			for i in range (len(adj_list[a])):

				degree[adj_list[a][i]] -= 1

				if (degree[adj_list[a][i]] == 1):

					node_queue.append(adj_list[a][i])


	while (len(node_queue) > 0):

		result.append(node_queue.popleft())
	

	return result

def main():

	n = int(input())

	number_of_edges = int(input())

	edges = []

	for i in range (number_of_edges):

		row = []

		for j in range(2):

			element = int(input())

			row.append(element)

		edges.append(row)


	print(findminheighttrees(n, edges))




if __name__ == "__main__":
    main()