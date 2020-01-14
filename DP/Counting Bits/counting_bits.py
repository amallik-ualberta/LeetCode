
def counting_bits(num):

	table = []

	table.append(0)

	x = 1

	prev_x = 0


	for i in range(1, num+1):

		if(i == x):

			table.append(1)

			prev_x = x

			x = x * 2

			continue;

		p = i - prev_x

		table.append (table[prev_x] + table[p])

	return table


def main():

	num = int(input())

	print(counting_bits(num))

if __name__ == "__main__":
    main()