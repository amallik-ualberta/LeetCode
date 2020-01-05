
def word_break(s, wordDict):

	if (s== None or wordDict == None):

		return False;

	max_length = 0

	for a in wordDict:

		if (len(a) > max_length):

			max_length = len(a)


	length = len(s)

	table = []

	for i in range (length):

		table.append(False)

	
	if(s[0] in wordDict):

		table[0] = True

	for i in range (1, length):

		this_string = s[0:i+1]

		if(this_string in wordDict):

			
			table[i] = True;

			continue;

		a = max(0, i - max_length)

		for j in range (a, i):

			this_string = s[j+1 : i+1]

			if (table[j] == True and this_string in wordDict):

				
				table[i] = True



	return table[length-1]


	




def main():

	s = str(input())

	n = int(input())

	wordDict = []

	for i in range (n):

		element = str(input())

		wordDict.append(element)

	print(word_break(s, wordDict))

if __name__ == "__main__":
    main()