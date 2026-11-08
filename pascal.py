import numpy as np


def search_pascal_multiples_fast(row_limit):
    # Credit: https://medium.com/@jelambrar/generating-pascals-triangle-in-python-using-numpy-d7cd9a20570e
    ptriangle = np.zeros((row_limit, row_limit), dtype=np.int64)
    ptriangle[:, 0] = 1
    for i in range(1, row_limit):
        ptriangle[i, 1:i + 1] = ptriangle[i - 1, 1:i + 1] + ptriangle[i - 1, 0:i]
    r_indices, c_indices = np.indices((row_limit, row_limit))
    valid_mask = (c_indices > 1) & (c_indices < r_indices)
    arr, counts = np.unique(ptriangle[valid_mask], return_counts=True)
    four_or_more = counts > 3
    return sorted([int(c) for c in arr[four_or_more]])

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