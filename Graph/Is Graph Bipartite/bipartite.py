from collections import deque

def isBipartite(graph):

	color = {}

	for i in range (len(graph)):

		color[i] = -1

	for i in range (len(graph)):

		if (color[i] == -1) and (bfs(i, graph, color) == False):

			return False

	return True


def bfs (i, graph, color):

	node_queue = deque()

	node_queue.append(i)

	color[i] = 0

	while(len(node_queue)!=0):

		current_vertex = node_queue.popleft()

		current_color = color[current_vertex]

		adjacent_list = graph[current_vertex]

		for vertex in adjacent_list:

			if (color[vertex] == current_color):

				return False

			if (color[vertex] == -1):

				if (current_color == 0):

					color[vertex] = 1

				else :

					color[vertex] = 0

				node_queue.append(vertex)


	return True


def main():


	number_of_entries = int(input())

	entries = []

	for i in range (number_of_entries):

		row = []

		entry_length = int(input())

		for j in range(entry_length):

			element = int(input())

			row.append(element)

		entries.append(row)


	print(isBipartite(entries))




if __name__ == "__main__":
    main()