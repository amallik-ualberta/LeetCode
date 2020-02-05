def calcEquation(equations, values, queries):

	graph = {}

	i = 0

	for equation in equations:

		first_term = equation[0]

		second_term = equation[1]

		if (first_term not in graph):

			graph[first_term] = {}

		if (second_term not in graph):

			graph[second_term] = {}

		graph[first_term][second_term] = values[i]

		graph[second_term][first_term] = 1/values[i]

		i += 1

	result = []


	for query in queries:

		first_term = query[0]

		second_term = query[1]

		if (first_term not in graph or second_term not in graph) :

			result.append(-1.0)

		elif (first_term == second_term):

			result.append(1.0)

		else :

			result.append(dfs([], first_term, second_term, graph, 1))


	return result

def dfs (visited, first_term, second_term, graph, result):

	visited.append(first_term)

	adjacents = graph[first_term]

	if (second_term in adjacents):

		return result * adjacents[second_term]

	answer = -1.0

	for adjacent in adjacents.keys():

		if (adjacent not in visited):

			temp_ans = dfs(visited, adjacent, second_term, graph, result* adjacents[adjacent])

			if (temp_ans > 0):

				answer = temp_ans


	return answer
	

def main():


	number_of_equations = int(input())

	equations = []

	for i in range (number_of_equations):

		row = []

		for j in range(2):

			element = str(input())

			row.append(element)

		equations.append(row)

	values = []

	for i in range (number_of_equations):

		element = float(input())

		values.append(element)

	number_of_queries = int(input())

	queries = []

	for i in range (number_of_queries):

		row = []

		for j in range (2):

			element = str(input())

			row.append(element)

		queries.append(row)



	print(calcEquation(equations, values, queries))




if __name__ == "__main__":
    main()