from collections import Counter


def search_pascal_multiples_fast(row_limit):
    counter = Counter()

    p_row = [1] * row_limit
    p_row[0] = 3
    for i in range(4, row_limit, 2):
        p_row[i // 2 - 1] += p_row[i // 2 - 2] # Replace with i (row number)
        for j in range(i // 2 - 2, 0, -1):
            p_row[j] += p_row[j - 1]
            counter[p_row[j]] += 2
        p_row[0] *= 2
        counter[p_row[0]] += 1

        i += 1
        for j in range(0, i // 2 - 1):
            p_row[j] = p_row[j] + p_row[j + 1]
            counter[p_row[j]] += 2
        p_row[i // 2 - 1] += p_row[i // 2] # Replace with i (row number)

    return sorted([k for k, v in counter.items() if v > 3])

#----------- DO NOT CHANGE ANYTHING BELOW THIS LINE


def search_pascal_multiples_slow(row_limit):

    # Building up Pascal's triangle with a dict of lists
    ptriangle = {}
    ptriangle[0] = [1]
    ptriangle[1] = [1,1]
    ptriangle[2] = [1,2,1]
    for r in range(3, row_limit):
        ptriangle[r] = []
        for i in range(len(ptriangle[r-1])+1):
            if i == 0: # on left border, so we just add 1
                ptriangle[r].append(1)
            elif i == len(ptriangle[r-1]): # on right border, so we just add 1
                ptriangle[r].append(1)
            else: # not on border, so we sum up the two numbers above
                ptriangle[r].append(ptriangle[r-1][i-1] + ptriangle[r-1][i])

    # Putting all numbers into one list, except the outermost 2 numbers in each row
    number_list = []
    for r in range(row_limit):
        row = ptriangle[r]
        for i, number in enumerate(row):
            if i > 1 and i < len(row)-1: # exclude the outermost 2 numbers in each row
                number_list.append(number)

    # Counting the numbers
    number_set = set(number_list) 
    pascal_multiples = []
    for unique_number in number_set:
        count = 0
        for number in number_list:
            if number == unique_number:
                count = count + 1
        if count > 3:
            pascal_multiples.append(unique_number)
    
    return sorted(pascal_multiples)


from timeit import default_timer as timer

def main():
	row_limit = 250

	start = timer()
	print(search_pascal_multiples_slow(row_limit))
	end = timer()
	runtime_slow = end-start

	start = timer()
	print(search_pascal_multiples_fast(row_limit))
	end = timer()
	runtime_fast = end-start

	print(round(runtime_slow / runtime_fast, 2))

if __name__ == "__main__":
	main()