
class Node:
	"""docstring for Node"""
	def __init__(self, value):
		self.val = value
		self.neighbors = []


from collections import deque

def create_node(val):

	mynode = Node(val)

	mynode.neighbors = []

	return mynode


def clone_graph(node):

	if(node == None):

		return None

	node_map = {}

	node_queue = deque()

	node_map[node] = create_node(node.val) 

	node_queue.append(node)

	while(len(node_queue) != 0):

		current_node = node_queue.popleft()

		for i in range (len(current_node.neighbors)):

			neighbor = current_node.neighbors[i]

			if neighbor not in node_map.keys():

				node_map[neighbor] = create_node(neighbor.val)

				node_queue.append(neighbor)


			node_map[current_node].neighbors.append(node_map[neighbor])


	return node_map[node]





def main():

	node = Node(1)

	second_node = Node(2)

	third_node = Node(3)

	fourth_node = Node(4)

	node.neighbors.append(second_node)
	node.neighbors.append(fourth_node)

	second_node.neighbors.append(node)
	second_node.neighbors.append(third_node)

	third_node.neighbors.append(second_node)
	third_node.neighbors.append(fourth_node)

	fourth_node.neighbors.append(node)
	fourth_node.neighbors.append(third_node)

	cloned = clone_graph(node)




if __name__ == "__main__":
    main()