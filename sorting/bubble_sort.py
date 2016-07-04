def bubble_sort(A):
    """
    Sort an array of objects in place using bubble sorting algorithm.

    Bubble Sort is considered one the most ineffective sorting methods. It makes `n`
     runs over the whole array. In every pass it iterates backwards over the
     yet-to-be-sorted part and repeatedly swaps neighbour elements that are out of
     order. As a result elements "bubble" up or down (depending on sorting direction)
     in the array.

    Complexity: average/worst O(n^2), O(n) if array is already sorted. Bubble sort is
     a stable in-place sorting algorithm.
    :param list A: Array (list) to sort
    :return None: List `A` is mutated.
    """
    n = len(A)
    i_n = n - 1  # Index of last element
    for k in range(0, i_n):
        for i in range(i_n, k, -1):
            if A[i] < A[i - 1]:  # Flip this comparison for reversed order
                A[i], A[i - 1] = A[i - 1], A[i]
