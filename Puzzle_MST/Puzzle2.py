neighbors = ((0, 1), (1, 0), (-1, 0), (0, -1))


def manhattan_distance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def obstacle_check(board, point):
	if point == '#':
		return True
	return False


def outside_check(board, point):
	if point < (0, 0) or point > (5, 5):
		return True
	return False


def solve_puzzle(board, source, destination):
	tuple1 = (manhattan_distance(source, destination), source, None)
	queue = []
	traversed1 = []
	queue.append(tuple1)
	infinity = 99999999

	while tuple1[1] != destination:
		if queue is None:
			return None
		tuple1 = queue
		tempTuple = (infinity, (-1, -1), None)

		for v in neighbors:
			neighbor1 = (tuple1[1][0] + v[0], tuple1[1][1] + v[1])
			if outside_check(board, neighbor1) or obstacle_check(board, neighbor1) or neighbor1 in traversed1:
				continue
			curDist = manhattan_distance(neighbor1, destination)
			if curDist < tempTuple[0]:
				tempTuple = (curDist, neighbor1, tuple1)

		if tempTuple[0] != infinity:
			traversed1.append(tempTuple[1])
			queue.append(tempTuple)
			queue.append(tuple1)
			queue = tuple(sorted(queue))  # Sort by first element
			tuple1 = tempTuple

	output = []
	output.append(tempTuple[1])
	while tempTuple[2] is not None:
		tempTuple = tempTuple[2]
		output.append(tempTuple[1])

	output.reverse()
	return output


Puzzle = [
	['-', '-', '-', '-', '-'],
	['-', '-', '#', '-', '-'],
	['-', '-', '-', '-', '-'],
	['#', '-', '#', '#', '-'],
	['-', '#', '-', '-', '-']
]

source = (0, 2)
destination = (2, 2)

solve_puzzle(Puzzle, source, destination)
