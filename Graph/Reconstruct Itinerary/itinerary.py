
from collections import deque

from queue import PriorityQueue

def itinerary(tickets):

	if (len(tickets) == 0):

		return None

	result = []

	if (len(tickets) == 1):

		result.append(tickets[0][0])

		result.append(tickets[0][1])

		return result

	ticket_map = {}


	for ticket in tickets:

		source = ticket[0]

		dest = ticket[1]

		if (source not in ticket_map):

			ticket_map[source] = PriorityQueue();

		ticket_map[source].put(dest)


	stack = deque()

	dfs (stack, ticket_map, "JFK")

	while (len(stack)!=0):

		result.append(stack.pop())

	return result


def dfs (stack, ticket_map, source):

	if (source in ticket_map):

		dest_queue = ticket_map[source]

		while not dest_queue.empty():

			dest = dest_queue.get()

			dfs (stack, ticket_map, dest)

	stack.append(source)
	

def main():


	number_of_tickets = int(input())

	tickets = []

	for i in range (number_of_tickets):

		row = []

		for j in range(2):

			element = str(input())

			row.append(element)

		tickets.append(row)


	print(itinerary(tickets))




if __name__ == "__main__":
    main()