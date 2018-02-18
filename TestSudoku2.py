import copy
from Sudoku import *


#def test_play():

#response = 'Y'
#play = playAgain(response)
#assert play in ['Y', 'y', 'N', 'n']:


def test_getIncompleteLocations():

    problem = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {3}]]
    incomplete = getIncompleteLocations(problem)
    assert incomplete == [[(0,0), {1, 2}], [(1, 1), {3, 5, 7}], [(2, 1), {2, 3}]]


def test_getLocation():

    indexArgs = [1, 1, (1, 2)]
    location_lst = getLocation(indexArgs)
    assert isinstance(location_lst, int)


def test_ConvertToSets2():
    problem = [[0, 4, 5], [0, 6, 0], [2, 0, 9]]
    s = set(range(1, 10))
    test_set = [[s, {4}, {5}], [s, {6}, s], [{2}, s, {9}]]
    problem_set = convertToSets(problem)
    assert problem_set == test_set
    assert isinstance(problem[0][0], int)
    assert isinstance(problem_set[0][0], set)

def test_ConvertToInts():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {3}]]
    problem_ints = convertToInts(sets)
    assert [[0, 3, 4], [1, 0, 2], [0, 2, 3]] == problem_ints
    assert isinstance(sets[0][0], set)
    assert isinstance(problem_ints[0][0], int)

def test_GetRowLocations():
    lst = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
    row_locations = getRowLocations(5)
    assert set(lst) == set(row_locations)

def test_GetColumnLocations():
    lst = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
    column_locations = getColumnLocations(5)
    print(column_locations)
    print(lst)
    assert set(lst) == set(column_locations)

def test_GetBoxLocations():
    lst = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    box_locations = getBoxLocations((3, 2))

    assert set == set(box_locations)

def test_Eliminate():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    location = (1, 2) # contains {2}
    count = eliminate(sets, location, [(1, 0), (1, 1), (1, 2)])
    assert count == 0

    problem = [[4, 0, 0,  0, 0, 3,  0, 7, 0],
                [0, 0, 1,  0, 0, 9,  5, 0, 8],
                [0, 0, 0,  6, 0, 8,  4, 1, 3],

                [0, 1, 0,  9, 0, 0,  3, 0, 0],
                [0, 0, 0,  0, 5, 0,  0, 0, 0],
                [0, 0, 4,  0, 0, 6,  0, 8, 0],

                [7, 9, 2,  8, 0, 5,  0, 0, 0],
                [3, 0, 5,  4, 0, 0,  9, 0, 0],
                [0, 4, 0,  2, 0, 0,  8, 0, 5]]

    problemAsSets = convertToSets(problem)
    listOfLocations = [(1, 0), (1, 1), (1, 2), (1, 3),
                                        (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
    count = eliminate(problemAsSets, (1, 5), listOfLocations)

    assert count == 5

    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2), (1, 2)])
    assert count == 2
    assert [[{1}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 3}]] == sets

def test_IsSolved():

        array = [[{1}] * 9] * 9
        assert isSolved(array) == True
        array[3][5] = {1, 2}
        assert isSolved(array) == False

def test_getSingleLocations(problem, n):

    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    n = len(sets)
    single_locations = getSingleLocations(sets, n)
    single_sets = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 1)]
    assert all(len(sets[single_locations[i][0]][single_locations[i][1]]) == 1 for i in
                                                                range(len(single_locations)))
    assert set(single_sets) == set(single_locations)

def test_print_sudoku():

        problem = [[4, 6, 8,  5, 1, 3,  2, 7, 9],
                   [2, 3, 1,  7, 4, 9,  5, 6, 8],
                   [5, 7, 9,  6, 2, 8,  4, 1, 3],

                   [6, 1, 7,  9, 8, 2,  3, 5, 4],
                   [8, 2, 3,  1, 5, 4,  7, 9, 6],
                   [9, 5, 4,  3, 7, 6,  1, 8, 2],

                   [7, 9, 2,  8, 3, 5,  6, 4, 1],
                   [3, 8, 5,  4, 6, 1,  9, 2, 7],
                   [1, 4, 6,  2, 9, 7,  8, 3, 5]]

        test = print_sudoku(problem)
        assert 1 == test

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
    problemAssets = convertToSets(sudoku1)
    test = solve(problemAssets)

    solved = convertToInts(test)
    print_sudoku(solved)
    assert(0 == solved)

    #solution = tryToSolv(sudoku2, solved2)
    #solution = tryToSolve(sudoku3, solved3)


def tryToSolve(problem, solution):
##        print_sudoku(problem)
    problemAsSets = convertToSets(problem)
    solve(problemAsSets)
    solved = convertToInts(problemAsSets)
    return solved
##        print_sudoku(solution)
