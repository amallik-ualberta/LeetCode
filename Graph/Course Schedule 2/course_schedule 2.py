

from collections import deque

def canfinish(numCourses, prerequisites):

	if (numCourses == 0):

		return [];

	if (len(prerequisites) == 0 or numCourses == 1):

		result = []

		for i in range (numCourses):

			result.append(i)

		return result

	schedule = {}

	for i in range (numCourses):

		schedule[i] = []

	course_queue = deque()

	indegree = []

	result = []

	count = 0

	for i in range (numCourses):

		indegree.append(0)

	for i in range (len(prerequisites)):

		schedule[prerequisites[i][1]].append(prerequisites[i][0])

		indegree[prerequisites[i][0]] += 1

	for i in range (numCourses):

		if (indegree[i] == 0):

			course_queue.append(i)

			result.append(i)

			count +=1

	while (len(course_queue) != 0):

		free_vertex = course_queue.popleft()

		for i in range (len(schedule[free_vertex])):

			indegree[schedule[free_vertex][i]] -= 1

			if (indegree[schedule[free_vertex][i]] == 0):

				course_queue.append(schedule[free_vertex][i])

				result.append(schedule[free_vertex][i])

				count += 1

	if (count == numCourses):

		return result

	return []

def main():

	numCourses = int(input())

	n = int(input())

	prerequisites = []

	for i in range (n):

		row = []

		for j in range(2):

			element = int(input())

			row.append(element)

		prerequisites.append(row)


	print(canfinish(numCourses, prerequisites))




if __name__ == "__main__":
    main()