import copy
from Sudoku import *

def test_ConvertToSets2():
    problem = [[0, 4, 5], [0, 6, 0], [2, 0, 9]]
    s = set(range(1, 10))
    test_set = [[s, {4}, {5}], [s, {6}, s], [{2}, s, {9}]]
    problem_set = convertToSets(problem)
    assert(problem_set == test_set)
    assert(isinstance(problem[0][0], int))
    assert(isinstance(problem_set[0][0], set))

def test_ConvertToInts():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {3}]]
    problem_ints = convertToInts(sets)
    assert([[0, 3, 4], [1, 0, 2], [0, 2, 3]] == problem_ints)
    assert(isinstance(sets[0][0], set))
    assert(isinstance(problem_ints[0][0], int))

def test_GetRowLocations():
    lst = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
    row_locations = getRowLocations(5)
    assert(set(lst) == set(row_locations))

def test_GetColumnLocations():
    lst = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
    column_locations = getColumnLocations(5)
    assert(set(lst), set(getColumnLocations(5)))

def test_GetBoxLocations():
    lst = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    box_locations = getBoxLocations((3, 2))
    assert(set(lst) == set(box_locations))

def test_Eliminate():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    location = (1, 2) # contains {2}
    count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2)])
    assert(count == 2)
    assert([[{1}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 3}]] == sets)
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2), (1, 2)])
    assert(count == 3)

def test_IsSolved():

        array = [[{1}] * 9] * 9
        assert((isSolved(array) == True))
        array[3][5] = {1, 2}
        assert((isSolved(array) == False))


def test_Solve():
    # Easy
    sudoku1 = [[4, 0, 0,  0, 0, 3,  0, 7, 0],
               [0, 0, 1,  0, 0, 9,  5, 0, 8],
               [0, 0, 0,  6, 0, 8,  4, 1, 3],

               [0, 1, 0,  9, 0, 0,  3, 0, 0],
               [0, 0, 0,  0, 5, 0,  0, 0, 0],
               [0, 0, 4,  0, 0, 6,  0, 8, 0],

               [7, 9, 2,  8, 0, 5,  0, 0, 0],
               [3, 0, 5,  4, 0, 0,  9, 0, 0],
               [0, 4, 0,  2, 0, 0,  8, 0, 5]]

    solved1 = [[4, 6, 8,  5, 1, 3,  2, 7, 9],
               [2, 3, 1,  7, 4, 9,  5, 6, 8],
               [5, 7, 9,  6, 2, 8,  4, 1, 3],

               [6, 1, 7,  9, 8, 2,  3, 5, 4],
               [8, 2, 3,  1, 5, 4,  7, 9, 6],
               [9, 5, 4,  3, 7, 6,  1, 8, 2],

               [7, 9, 2,  8, 3, 5,  6, 4, 1],
               [3, 8, 5,  4, 6, 1,  9, 2, 7],
               [1, 4, 6,  2, 9, 7,  8, 3, 5]]
    # Easy
    sudoku2 = [[0, 0, 0,  7, 0, 0,  6, 8, 9],
               [3, 0, 8,  0, 0, 0,  2, 0, 0],
               [0, 0, 0,  8, 1, 0,  0, 4, 0],

               [6, 0, 0,  0, 0, 0,  8, 0, 4],
               [8, 0, 0,  3, 4, 9,  0, 0, 5],
               [7, 0, 5,  0, 0, 0,  0, 0, 3],

               [0, 8, 0,  0, 7, 6,  0, 0, 0],
               [0, 0, 7,  0, 0, 0,  1, 0, 8],
               [9, 5, 1,  0, 0, 8,  0, 0, 0]]

    solved2 = [[1, 2, 4,  7, 5, 3,  6, 8, 9],
               [3, 7, 8,  9, 6, 4,  2, 5, 1],
               [5, 9, 6,  8, 1, 2,  3, 4, 7],

               [6, 3, 9,  5, 2, 7,  8, 1, 4],
               [8, 1, 2,  3, 4, 9,  7, 6, 5],
               [7, 4, 5,  6, 8, 1,  9, 2, 3],

               [4, 8, 3,  1, 7, 6,  5, 9, 2],
               [2, 6, 7,  4, 9, 5,  1, 3, 8],
               [9, 5, 1,  2, 3, 8,  4, 7, 6]]

    # Hard
    sudoku3 = [[9, 0, 0,  0, 0, 8,  0, 0, 0],
               [0, 0, 0,  0, 3, 2,  0, 0, 0],
               [6, 8, 0,  9, 0, 1,  0, 7, 0],

               [8, 0, 9,  5, 2, 0,  0, 3, 0],
               [2, 0, 0,  0, 0, 0,  0, 0, 5],
               [0, 4, 0,  0, 9, 3,  7, 0, 8],

               [0, 2, 0,  3, 0, 9,  0, 6, 4],
               [0, 0, 0,  2, 8, 0,  0, 0, 0],
               [0, 0, 0,  6, 0, 0,  0, 0, 3]]

    solved3 = [[9, 0, 0,  0, 0, 8,  0, 0, 0],
               [0, 0, 0,  0, 3, 2,  0, 0, 0],
               [6, 8, 0,  9, 0, 1,  0, 7, 2],

               [8, 0, 9,  5, 2, 0,  0, 3, 0],
               [2, 0, 0,  0, 0, 0,  0, 0, 5],
               [5, 4, 6,  1, 9, 3,  7, 2, 8],

               [0, 2, 0,  3, 0, 9,  0, 6, 4],
               [0, 0, 0,  2, 8, 0,  0, 0, 0],
               [0, 0, 0,  6, 0, 0,  0, 0, 3]]

    solution = tryToSolve(sudoku1, solved1)
    print(solution)

    solution = tryToSolve(sudoku2, solved2)
    solution = tryToSolve(sudoku3, solved3)


def tryToSolve(problem, solution):
##        print_sudoku(problem)
    problemAsSets = convertToSets(problem)
    solve(problemAsSets)
    solved = convertToInts(problemAsSets)
    return solution==solved
##        print_sudoku(solution)
