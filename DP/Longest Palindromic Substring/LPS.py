
def longest_palindromic_substring(s):


	length = len(s)

	if (s== None or length<2):

		return s;

	left = 0

	right = 0

	table = [[0]*length for i in range(length)]

	for i in range (length):

		table[i][i] = 1

	for j in range (1, length):

		for i in range (0, j):

			isinnerpalindrome = (table[i+1][j-1] == 1) or (j-i <=2)

			if (isinnerpalindrome and s[i] == s[j]):

				

				table[i][j] =1

				if (j-i > right-left):

					

					left = i

					right = j

	return s[left:right+1]



def main():

	s = input("Enter a string\n")

	print(longest_palindromic_substring(s))

if __name__ == "__main__":
    main()