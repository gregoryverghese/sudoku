from functools import reduce



def getIncompleteLocations(problem):

    n = len(problem)
    locations = [((i, j), num) for i in range(n) for j, num in enumerate(problem[i])]
    locations = list(filter(lambda x: (len(x[1]) != 1), locations))

    return locations


def playAgain(response, prompt):

    while response not in ['Y', 'y', 'N', 'n']:
        response = input('Sorry I do not recognize your answer \n' + prompt)

    return response


def main():

    while play in {'Y', 'y'}:
        name = input('Could you you please provide the file name? \n')
        sudoku_grid = read_sudoku(name)
        print_sudoku(sudoku_grid)
        problemAsSets = convertToSets(sudoku_grid)
        result = solve(problemAsSets)
        solved = convertToInts(problemAsSets)
        print_sudoku(solved)
        incomplete_locations = getIncompleteLocations if not result else None
        prompt = 'Would you like to play again?'
        response = input(prompt + 'please answer Y or y for Yes or N or n for No \n')
        play = playAgain(response, prompt)

        print('Thankyou for playing Sudoku')


def print_sudoku(problem):

    for i, num in enumerate(problem):

        print(("|" + "{} {} {} |" * 3).format(*[x for x in num]))
        if i %  3 == 2:
            print("-" * 22)
        else:
            pass

    return 0


def getLocation(indexArgs):

    getLoc_func = [getRowLocations, getColumnLocations, getBoxLocations]
    location_lst = (map(lambda x, y: x(y), getLoc_func, indexArgs))
    all_locations = [l for loc in location_lst  for l in loc]

    return all_locations

def solve(problem):

    n = len(problem)

    for k in range(10):
        for i in range(n):
                for j in range(n):
                    loc2 = getLocation([i, j, (i, j)])
                    count =  (eliminate(problem, (i, j), loc2))

    return(problem)


def isSolved(problem):
    '''given a 2d array this checks to see if each element is a set of a
    single number and returns true if it is false otherwise
    Args:
        problem: nested list of sets
    Returns:
        boolean value if the array contains sets of single numbers, false otherwise
    '''
    n = len(problem)
    return (all([len(problem[i][j]) == 1 for j in range(n) for i in range(n)]))


def eliminate(problem, location, listOfLocations):
    ''''Given a 2d array (nested list), a location within the array and and list of
    other locations remove, the number which resides at location if it exists in the
    sets at the other locations, changing the array accordingly and returning the
    number of times it was removed
    Args:
        problem: nested list of sets
        location: tuple of 2 ints containg locatation of a single sized set in problem
        listOfLocations: list of tuples containing locations in problem
    Returns:
        count: number of times the number in the set at location was removed from other sets
        that exists at locations listed in listOfLocations
    '''
    count = 0

    if len(problem[location[0]][location[1]]) != 1:
        return 0

    else:
        number = list(problem[location[0]][location[1]])[0]
        for loc in listOfLocations:
            num_set = problem[loc[0]][loc[1]]
            if number in num_set and loc!= location:
                #if len(num_set) != 1:
                count += 1
                num_set.remove(number)
                problem[loc[0]][loc[1]] = num_set

    return count


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
    #for val
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
        [(3, 0), (3, 1), (3, 2), (3, 3),     (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)]
    '''
    Grid_dict = {"box1": (0, 2), "box2": (3, 5), "box3": (6, 8)}

    row_locations = [(rowNumber, i) for i in range(9)]
    return row_locations


def getColumnLocations(columnNumber):
    '''Given a column number returns a list of tuples containing
    all 9 possible locations.
    Args:
        columnNumber: integer between 0 and 8
    Returns:
        a list contaning tuples of all possible locations
        for example if rowNumber is 3 this would returns
        [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)]
    '''

    column_locations = [(i, columnNumber) for i in range(9)]
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

def convertToSets(problem):
    '''Reads in a 2d nested list of numbers and converts
    each element to  a set of range(n) if the element is
    a 0 or a set of the number if it's not 0
    Args:
        problem: 2d list
    Returns:
        A 2d list containing sets
    '''
    n = len(problem)
    s = set(range(1, (n) + 1))

    problem_set = [[{problem[i][j]} if problem[i][j] != 0 else {1, 2, 3, 4, 5, 6, 7, 8, 9} for j in range(n)] for i in range(n)]

    return problem_set

def convertToInts(problem):
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
    problem_set = [[int(list(problem[i][j])[0]) if len(problem[i][j]) == 1
                                                             else 0 for j in range(n)] for i in range(n)]

    return problem_set

if __name__ == '__main__':
    main()
