def counting_sort(A, k):
    """
    Sorts an array of integers using counting sort algorithm and returns sorted array.

    Counting sort assumes that each element in the array is an integer in the range
     `[0..k]`. It determines, for each element `x`, the number of elements less than `x`.
     The algorithm uses this information to place element `x` directly into its position
     in the output array.

    This algorithm breaks lower bound of comparison sort log(n). In fact, no comparisons
     between input elements occur in the code. The values of the elements are used to
     index into an array. Counting sort stability is not important for sorting arrays of
     integers without satellite data carried with them, but it is critical, when counting
     sort is used as a subroutine in radix sort (see sorting/radix_sort.py)

    Complexity: O(n+k), where `k` is the number of distinct elements in the array.
     Counting sort is stable and requires additional `n` storage for the output and
     auxiliary working storage of size `k` for count.
    :param list A: Array to sort
    :param int k: Inclusive upper bound for the range of integers in the array, for
     instance for A = [0, 1, 3], k = 3 or `max(A)`.
    :return list: Sorted product of an array `A`
    """
    n = len(A)
    P = [None] * n     # Allocated memory for sorted output
    C = [0] * (k + 1)  # Working storage (auxiliary array)

    for j in range(0, n):
        C[A[j]] += 1
    # `C[i]` now contains number (count) of elements equal to `i`

    s = n  # Running sum of total counted elements, going backwards
    for i in range(k, -1, -1):
        C[i] = s - C[i]
        s = C[i]
    # `C[i]` now contains number of elements less than or equal to `i`. Array `C` will
    # serve as a map for a final location of each element picked from input array.
    for e in A:
        j = C[e]  # Location index of the element `e` in output array
        P[j] = e
        # Counter is updated in order to keep next element of the same value
        # from overwriting previous one.
        C[e] += 1
    return P