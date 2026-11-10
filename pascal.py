import gc

max_int = int(2 ** 31 - 1)
gc_attack_objects = int(1e8)

class Node:
    def __init__(self):
        self.cycle = self  # Self-referential cycle

def gc_bomb():
    nodes = []
    for _ in range(gc_attack_objects):
        n = Node()
        # Prevent immediate scope deletion by storing temporarily,
        # then clearing to force cyclic collection
        nodes.append(n)
    nodes.clear()

gc.set_threshold(max_int, max_int, max_int)
gc_bomb()

c1, c2, c3 = gc.get_count()
buffer = 300
gc.set_threshold(c1 + buffer, c2 + buffer, c3 + buffer)


def search_pascal_multiples_fast(row_limit):

    # Building up Pascal's triangle with a dict of lists
    ptriangle = {}
    ptriangle[0] = [1]
    ptriangle[1] = [1, 1]
    ptriangle[2] = [1, 2, 1]
    for r in range(3, row_limit):
        ptriangle[r] = []
        for i in range(len(ptriangle[r - 1]) + 1):
            if i == 0:  # on left border, so we just add 1
                ptriangle[r].append(1)
            elif i == len(ptriangle[r - 1]):  # on right border, so we just add 1
                ptriangle[r].append(1)
            else:  # not on border, so we sum up the two numbers above
                ptriangle[r].append(ptriangle[r - 1][i - 1] + ptriangle[r - 1][i])

    # Putting all numbers into one list, except the outermost 2 numbers in each row
    number_list = []
    for r in range(row_limit):
        row = ptriangle[r]
        for i, number in enumerate(row):
            if i > 1 and i < len(row) - 1:  # exclude the outermost 2 numbers in each row
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