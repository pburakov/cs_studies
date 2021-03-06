"""
Sudoku Solver
=============

A standard Sudoku puzzle of edge size :math:`b=9` contains 81 cells, in a 9 by 9 grid, and
has 9 zones, each zone being the intersection of the first, middle, or last 3 rows, and
the first, middle, or last 3 columns. Each cell may contain a number from one to nine;
each number can only occur once in each zone, row, and column of the grid. Pre-filled
cells are provided as clues.

Sudoku puzzle board is represented by two-dimensional array of integers of size :math:`9
\\times 9`.

Example::

    B = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

"""


def solve(B):
    """Sudoku puzzle solver.

    Prints out output.

    Complexity:
        :math:`O(b^n)` where :math:`b` is the size of the board and `n` is the number of
        unfilled cells. See implementation details below.

    :param list[list[int]] B: Sudoku board.

    """
    # Check for `valid_board()` here allows to drop bad boards early
    if valid_board(B) and has_solution(B):
        print_board(B)
    else:
        print("Board has no solution")


"""
Auxiliary routines and constants used in the solution
"""
BOARD_EDGE_SIZE = 9
ZONE_SIZE = 3


def has_solution(B, x=0, y=0):
    """Evaluates if Sudoku board can be solved.

    This is a exhaustive Sudoku board solution search. Every digit is tried for every
    unfilled cell. Those that don't lead to a legit solution are dropped and board state
    backtracked.

    Backtracking algorithm follows a familiar pattern:

        - Construct a partial solution for first unfilled cell (containing `0`);
        - Try this solution;
        - If it worked for the board so far - continue, otherwise - backtrack;
        - Repeat steps above until all cells are filled out.

    Complexity:
        :math:`O(b^n)` where :math:`b` is the size of the board and `n` is the number of
        unfilled cells. Algorithm works through increasingly more cycles when searching
        for Sudokus with 20 clues or fewer. Puzzles with 17 clues are notoriously
        difficult to find. When the constraint of symmetry is applied, the expected search
        time will dramatically increase yet further.

    :param list[list[int]] B: Current state of Sudoku board.
    :param int x: Row to start solution construction (used in recursion).
    :param int y: Column to start solution construction (used in recursion).
    :return: :data:`True` if board has a solution, :data:`False` otherwise.

    """
    if x == BOARD_EDGE_SIZE:  # Go to next row
        x = 0
        y += 1
    if y == BOARD_EDGE_SIZE:
        return valid_board(B)
    else:
        if B[x][y] == 0:
            # Try every integer available for given board size in a cell
            for i in range(1, BOARD_EDGE_SIZE + 1):
                if zone_unique(i, B, x, y) and row_unique(i, B, x) and col_unique(i, B, y):
                    B[x][y] = i
                    if has_solution(B, x + 1, y):
                        return True
                    else:  # Backtrack if a candidate haven't led to a solution
                        B[x][y] = 0
            return False  # Was unable to construct viable candidate
        else:
            return has_solution(B, x + 1, y)


def valid_board(B):
    """Checks rows and columns of Sudoku board for duplicate non-zero values.

    Complexity:
        :math:`O(b^2)` with :math:`O(b)` space, where :math:`b` is the size of the board.
        :math:`b` is a constant factor.

    :param list[list[int]] B: Sudoku board.
    :return: Validation result.
    """
    for i in range(0, BOARD_EDGE_SIZE):
        row_freq_map = init_freq_map()
        for x in B[i]:  # Checking row `i`
            row_freq_map[x] += 1
            if x != 0 and row_freq_map[x] > 1:
                return False
        # Checking col `i` within same loop
        col_freq_map = init_freq_map()
        for j in range(0, BOARD_EDGE_SIZE):
            y = B[j][i]
            col_freq_map[y] += 1
            if y != 0 and col_freq_map[y] > 1:
                return False
    return True


def zone_unique(e, B, x, y):
    """Check candidate "uniqueness" within a board zone.

    Complexity:
        :math:`O(z^2)`, where :math:`z` is constant zone size (default is :math:`3`).

    :param int e: Candidate value to validate.
    :param list[list[int]] B: Sudoku board.
    :param int x: Row coordinate of a value.
    :param int y: Column coordinate of a value.
    :return: Boolean validation result.

    """
    for i in range(x - x % ZONE_SIZE, x - x % ZONE_SIZE + ZONE_SIZE):
        for j in range(y - y % ZONE_SIZE, y - y % ZONE_SIZE + ZONE_SIZE):
            if B[i][j] == e:
                return False
    return True


def row_unique(e, B, r):
    """Check candidate "uniqueness" within a board row.

    Complexity:
        :math:`O(b)`, where :math:`b` is the edge size of the board. :math:`b` is a
        constant factor.

    :param int e: Candidate value to validate.
    :param list[list[int]] B: Sudoku board.
    :param int r: Row coordinate of a value.
    :return: Boolean validation result.

    """
    for i in range(0, BOARD_EDGE_SIZE):
        if B[r][i] == e:
            return False
    return True


def col_unique(e, B, c):
    """Check candidate "uniqueness" within a board column.

    Complexity:
        :math:`O(b)`, where :math:`b` is the edge size of the board. :math:`b` is a
        constant factor.

    :param list[list[int]] B: Sudoku board.
    :param int e: Candidate value to validate.
    :param int c: Column coordinate of a value.
    :return: Boolean validation result.

    """
    for i in range(0, BOARD_EDGE_SIZE):
        if B[i][c] == e:
            return False
    return True


def init_freq_map():
    """Builds empty frequency map of size `b+1`.

    Complexity:
        :math:`O(b)`, where :math:`b` is the edge size of the board. :math:`b` is a
        constant factor.

    :return list: Frequency map containing zeroes.

    """
    return [0] * (BOARD_EDGE_SIZE + 1)


def print_board(B):
    """Prints out board.

    Example::

        5 3 4 2 7 6 9 1 8
        6 7 8 1 9 5 3 4 2
        1 9 2 3 4 8 5 6 7
        8 5 9 7 6 1 4 2 3
        4 2 6 8 5 3 7 9 1
        7 1 3 9 2 4 8 5 6
        9 6 1 5 3 7 2 8 4
        2 8 7 4 1 9 6 3 5
        3 4 5 6 8 2 1 7 9

    Complexity:
        :math:`O(b^2)`, where :math:`b` is the edge size of the board. :math:`b` is a
        constant factor.

    :param list[list[int]] B: Sudoku board.

    """
    for row in B:
        for x in row:
            print(x, end=' ')
        print()
