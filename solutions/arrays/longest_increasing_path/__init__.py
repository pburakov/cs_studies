def scan(M):
    """
    Longest increasing path solver.

    Constructs the cache and runs DFS-like longest path subroutine for every element in
     the matrix.

    Complexity: O(n) where `n` is the total number of cells, O(n) space is used for
     memoization.
    :param list[list[int]] M: Input matrix
    :return int: Length of a longest increasing path in the matrix
    """
    cache = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
    maximum = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            longest_path(M, i, j, cache)
            maximum = max(maximum, cache[i][j])
    return maximum


"""
Auxiliary subroutines used in the solution
"""


def longest_path(M, x, y, cache) -> int:
    """
    Longest increasing path subroutine.

    DFS-like path search algorithm with memoization. We evaluate the path in 4 possibly
     directions from every cell in the matrix.

    Complexity: O(1) amortized time. First run might give us O(n) runtime, but the use of
     memoization allows to calculate longest path exactly once for each cell, so every
     consecutive call will give O(1). Previously computed values are pulled from the
     cache. This allows dramatic optimization over O(4^n) if going in each direction
     recursively.
    :param list[list[int]] M: Input matrix
    :param int x: Vertical coordinate
    :param int y: Horizontal coordinate
    :param list[list[int]] cache: Memoized solutions cache
    :return int: Length of a longest path starting at `x` and `y`
    """
    if cache[x][y] != 0:
        return cache[x][y]
    if 0 <= x < len(M) or 0 <= y < len(M[0]):
        val = M[x][y]
        up, down, left, right = 0, 0, 0, 0
        if x - 1 >= 0 and M[x - 1][y] < val:
            up = longest_path(M, x - 1, y, cache)
        if y + 1 < len(M[x]) and M[x][y + 1] < val:
            right = longest_path(M, x, y + 1, cache)
        if y - 1 >= 0 and M[x][y - 1] < val:
            left = longest_path(M, x, y - 1, cache)
        if x + 1 < len(M) and M[x + 1][y] < val:
            down = longest_path(M, x + 1, y, cache)
        cache[x][y] = 1 + max(up, right, left, down)
        return cache[x][y]
    else:
        return 0
