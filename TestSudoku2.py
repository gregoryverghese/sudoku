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
        
