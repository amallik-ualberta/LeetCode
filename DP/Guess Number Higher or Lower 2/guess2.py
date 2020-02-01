
import sys

def guess2(n):

	"""
	Let say there are 5 numbers, the host picked an unknown number X. The player has to guess a number,

if he guesses number 3, what is the worst case that can happen? the worst case money = max(money needed to win if X is in [1,2] range, money needed to win if X is in range [4,5]). Since if he has worse case money, it doesn't matter if X is in left or right of 3, since he will have enough money to win either case.
Similarly, if he guesses 2, he needs worse case money to win no matter X is in [1] or [3,5] ranges.
Note, that he purposely computes the worst case money for every guess in range [1,n] to guarantee a win for every guess. Now the final thing to do, is finding the guess with minimal worst case money. If he chooses that guess and brings its worst case money, he will win the game with minimal cost. This is the best thing he can do.
	"""

	table = []

	for i in range (n+1):

		row = []

		for j in range (n+1):

			row.append(0)

		table.append(row)


	for i in range (1,n):

		table[i][i+1] = i

	for length in range (3, n+1):

		for i in range (1, n-length+2):

			cost = sys.maxsize

			j = i + length -1

			
			for pivot in range (i, j+1):

				term2 = 0

				if (i <= pivot-1):

					term2 = table[i][pivot-1]

				term3 = 0

				if (pivot+1 <= j):

					term3 = table[pivot+1][j]

				

				cost = min(cost, pivot + max(term2, term3))


			table[i][j] = cost


			


	return table[1][n]




def main():

	n = int(input())

	print(guess2(n))

if __name__ == "__main__":
    main()