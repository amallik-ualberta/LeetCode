from collections import deque

def eventualSafeNodes(graph):

	visited = {}

	for i in range (len(graph)):

		visited[i] = -1

	node_stack = deque()

	for i in range (len(graph)):

		if (visited[i] == -1):

			dfs(i, visited, graph, node_stack)

	result = []

	for i in range (len(graph)):

		if (visited[i] == 2):

			result.append(i)

	return result

def dfs (i, visited, graph, node_stack):

	node_stack.append(i)

	visited[i] = 1

	for vertex in graph[i] :

		if (visited[vertex] == 1 or visited[vertex] == 0):

			visited[i] = 0

			while(len(node_stack) != 0):

				visited[node_stack.pop()] = 0

		elif (visited[vertex] == -1):

			dfs(vertex, visited, graph, node_stack)

	if(len(node_stack)!= 0):

		visited[node_stack.pop()] = 2


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


	print(eventualSafeNodes(entries))




if __name__ == "__main__":
    main()