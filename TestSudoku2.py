import copy
from Sudoku import *

def test_ConvertToSets2():
    problem = [[0, 4, 5], [0, 6, 0], [2, 0, 9]]
    s = set(range(1, 10))
    test_set = [[s, {4}, {5}], [s, {6}, s], [{2}, s, {9}]]
    problem_set = ConvertToSets(problem)
    assert(problem_set == test_set)
    assert(isinstance(problem[0][0], int))
    assert(isinstance(problem_set[0][0], set))

def test_ConvertToInts():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {3}]]
    problem_ints = ConvertToInts(sets)
    assert([[0, 3, 4], [1, 0, 2], [0, 2, 3]] == problem_ints)
    assert(isinstance(sets[0][0], set))
    assert(isinstance(problem_ints[0][0], int))

def test_GetRowLocations():
    lst = [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]
    row_locations = getRowLocations(5)
    assert(set(lst) == set(row_locations))

def testGetColumnLocations():
    lst = [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
    column_locations = getColumnLocations(5)
    assert(set(lst), set(getColumnLocations(5)))

def testGetBoxLocations():
    lst = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
    box_locations = getBoxLocations((3, 2))
    assert(set(lst) == set(box_locations))

def testEliminate():
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    location = (1, 2) # contains {2}
    count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2)])
    assert(count == 2)
    assert([[{1}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 3}]] == sets)
    sets = [[{1, 2}, {3}, {4}], [{1}, {3, 5, 7}, {2}], [{2, 3}, {2}, {1, 2, 3}]]
    count = eliminate(sets, location, [(0, 0), (1, 0), (2, 2), (1, 2)])
    assert(count == 3)
