def getBoxLocations(location):
    '''Given a location this determines which box of the grid the location
    resides in and returns all other locations in that box within a list
    Args:
        location: tuple containt x and y coordinate of the location onthe Grid_dict
    Returns:
        List containing tuples of all the locations within the box
    '''

    Grid_dict = {"box1": (0, 2), "box2": (3, 5), "box3": (6, 8)}

    for val in Grid_dict.values():
        if location[0] in range(val[0], val[1] + 1):
            row_upper = val[1]
            row_lower = val[0]

    for val in Grid_dict.values():
        if location[1] in range(val[0], val[1] + 1):
            column_upper = val[1]
            column_lower = val[0]

    box_locations = [(i, j) for j in range(column_lower, column_upper + 1) for i in range(row_lower, row_upper + 1)]

    return box_locations


def getRowLocations(rowNumber):
    '''Given a row number returns a list of tuples containing
    all 9 possible locations.
    Args:
        rowNumber: integer between 0 and 8
    Returns:
        a list contaning tuples of all possible locations
        for example if rowNumber is 3 this would returns
        [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)]
    '''

    row_locations = [(rowNumber, i) for i in range(9)]
    return row_locations


def getColumnLocations(rowNumber):
    '''Given a column number returns a list of tuples containing
    all 9 possible locations.
    Args:
        columnNumber: integer between 0 and 8
    Returns:
        a list contaning tuples of all possible locations
        for example if rowNumber is 3 this would returns
        [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)]
    '''

    column_locations = [(columnNumber, i) for i in range(9)]
    return column_locations


def read_sudoku(file):
    '''Reads in a file containing a n x n sudoku grid.
    Args:
        file: string containing file path
    Returns:
        a string format of sudoku grid
    '''
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))

def ConvertToSets(problem):
    '''Reads in a 2d nested list of numbers and converts
    each element to  a set of range(n) if the element is
    a 0 or a set of the number if it's not 0
    Args:
        problem: 2d list
    Returns:
        A 2d list containing sets
    '''
    n = len(problem)
    s = set(range(1, (n * n) + 1))

    problem_set = [[{problem[i][j]} if problem[i][j] != 0 else s for j in range(n)] for i in range(n)]

    return problem_set

def ConvertToInts(problem):
    '''Reads in a 2d nested list of sets and converts
    each element to a number if the element is
    a set with a single number or a 0 of the set contains
    multiple numbers
    Args:
        problem: 2d list of sets
    Returns:
        A 2d list containing numbers
        '''
    n = len(problem)
    problem_set = [[int(list(problem[i][j])[0]) if len(problem[i][j]) == 1  else 0 for j in range(n)] for i in range(n)]

    return problem_set
