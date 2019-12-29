
def decode_ways(s):


	length = len(s)

	table = []

	#doing the first character
	if (s[0] != '0'):

		table.append(1)

	else :

		return 0 #if the first char is 0, there is no point in going further


	#doing the second character
	if (length >=2):

		to_append =0

		if (s[1] >= '1'): #can this character be decoded by itself?

			to_append = 1 

		if (s[0] == '1' or (s[0]=='2' and s[1] <= '6')): #taking 2 characters with 2nd one being this one.

			to_append += 1

		table.append(to_append)


	
	#doing the rest of the characters
	for i in range (2,length):

		to_append = 0

		if (s[i] >= '1'): #can this character be decoded by itself?

			to_append = table[i-1] #coming from last character

		if (s[i-1] == '1' or (s[i-1]=='2' and s[i] <= '6')): #taking 2 characters with 2nd one being this one.

			to_append += table[i-2] #coming from 2nd last character

		table.append(to_append)

		
	return table[length-1]


def main():

	s = str(input())

	print(decode_ways(s))

if __name__ == "__main__":
    main()