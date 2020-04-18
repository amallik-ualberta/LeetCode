
def isSubsequence(s,t):

	s_length = len(s)

	t_length = len(t)

	if (t_length < s_length):
		return False

	if (s_length == 0):

		return True

	flag = -1

	j = flag + 1
	for i in range (s_length):

		for j in range (flag+1, t_length):

			if (s[i] == t[j]):

				flag = j

		if (j == t_length):

			return False

	return True
	






def main():

	

	s = str(input())

	t = str(input())

	print(isSubsequence(s,t))

if __name__ == "__main__":
    main()