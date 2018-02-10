


def read_sudoku(file):
    '''Reads in a file containg a n x n sudoku grid.
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
