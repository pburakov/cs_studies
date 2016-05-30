def counting_sort(A, k):
    """
    Sorts an array of integers using counting sort algorithm and returns sorted array.

    Counting sort assumes that each element in the array is an integer in the range
     `[0..k]`. The algorithm determines, for each element `x`, the number of elements
     less than `x`. It uses this information to place element `x` directly into its
     position in the output array. The values of the elements are used to index.

    Counting sort algorithm breaks the lower bound of comparison sort log(n). In fact,
     no comparisons between input elements occur in the code.

    Note that this is a stable implementation of counting sort. Stability is not important
     for sorting arrays of integers without satellite data carried with them, but it is
     critical, when counting sort is used as a subroutine in radix sort.

    Complexity: O(n+k), where `k` is the number of distinct elements in the array.
     Counting sort is stable and requires additional `n` storage for the output and
     auxiliary working storage of size `k` for count.
    :param list A: Array to sort
    :param int k: Inclusive upper bound for the range of integers in the array, for
     instance for A = [0, 1, 3], k = 3 or `max(A)`.
    :return list: Sorted product of array `A`
    """
    n = len(A)
    P = [None] * n     # Allocated memory for sorted output
    C = [0] * (k + 1)  # Working storage (auxiliary array for counting)

    for x in A:
        C[x] += 1
    # `C[x]` now contains number (count) of elements equal to `x`

    s = n  # Running sum of total counted elements, going backwards
    for x in range(k, -1, -1):
        C[x] = s - C[x]
        s = C[x]
    # `C[x]` now contains number of elements less than or equal to `x`. Array `C` will
    # serve as a map for a final location of each element picked from input array.
    for x in A:
        i = C[x]  # Location index of the element `x` in output array
        P[i] = x
        # Counter is updated in order to keep next element of the same value from
        # overwriting previous one.
        C[x] += 1
    return P
