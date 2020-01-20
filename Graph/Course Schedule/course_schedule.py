

from collections import deque

def canfinish(numCourses, prerequisites):

	if (numCourses <= 1):

		return True;

	if (len(prerequisites) == 0):

		return True;

	schedule = {}

	for i in range (numCourses):

		schedule[i] = []

	course_queue = deque()

	indegree = []

	for i in range (numCourses):

		indegree.append(0)

	for i in range (len(prerequisites)):

		schedule[prerequisites[i][1]].append(prerequisites[i][0])

		indegree[prerequisites[i][0]] += 1

	for i in range (numCourses):

		if (indegree[i] == 0):

			course_queue.append(i)

	count = 0

	while (len(course_queue) != 0):

		free_vertex = course_queue.popleft()

		count += 1

		for i in range (len(schedule[free_vertex])):

			indegree[schedule[free_vertex][i]] -= 1

			if (indegree[schedule[free_vertex][i]] == 0):

				course_queue.append(schedule[free_vertex][i])


	if (count == numCourses):

		return True

	return False

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