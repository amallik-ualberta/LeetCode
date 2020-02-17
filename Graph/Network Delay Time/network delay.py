import sys

import heapq

class pair:
	"""docstring for pair"""
	def __init__(self, first,second):
		self.first = first
		self.second = second
	
	def __lt__(self, other):

		return self.second < other.second

def networkDelayTime(times, N, K):

	matrix = {}

	for time in times :

		if (time[0] not in matrix):

			matrix[time[0]] = {}

		matrix[time[0]][time[1]] = time[2]

	heap_value = {}

	binaryheap = []

	for i in range (1, N+1):

		binaryheap.append(pair(i, sys.maxsize))

		heap_value[i] = sys.maxsize

	heap_value[K] = 0

	for x in binaryheap:

		if(x.first == K):

			binaryheap.remove(x)

	binaryheap.append(pair(K, 0))

	heapq.heapify(binaryheap)

	max_val = 0

	while(len(binaryheap)!= 0):

		extracted = heapq.heappop(binaryheap)

		extracted_key = extracted.first

		extracted_value = extracted.second

		del heap_value[extracted_key]

		if (extracted_value > max_val):

			max_val = extracted_value

		if (extracted_key in matrix):

			adjacent_list = matrix[extracted_key]

			for key in adjacent_list.keys():

				new_value = extracted_value + adjacent_list[key]

				if (key in heap_value and heap_value[key] > new_value):

					heap_value[key] = new_value

					for x in binaryheap:

						if (x.first == key):

							binaryheap.remove(x)

					binaryheap.append(pair(key, new_value))

					heapq.heapify(binaryheap)

	if (max_val < sys.maxsize):

		return max_val

	return -1

def main():


	number_of_edges = int(input())

	edges = []

	for i in range (number_of_edges):

		row = []

		for j in range(3):

			element = int(input())

			row.append(element)

		edges.append(row)


	N = int(input())

	K = int(input())

	print(networkDelayTime(edges, N, K))




if __name__ == "__main__":
    main()