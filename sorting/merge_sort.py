def merge_sort(list):
    """
    Merge sort is a recursive sorting algorithm that continuously splits a list in
     half recursively until eventually, it hits two lists containing a single element.
     Sorted halves, starting with two single-element lists (that are already sorted by
     definition) are then merged back together.

    The implementation of merge sort is a great example of divide-and-conquer technique,
     when the problem is broken to smaller pieces each or which is solved and then solved
     parts are combined back together.

    `merge(list)` method does the both the "conquer" and "combine" part, merging two sorted
     arrays. The body of the `merge_sort()` method implements the recursive "divide",
     or the slicing of the array.

    Complexity: O(n log(n)) in all cases. Log(n) for splitting, n for merge.
     Merge Sort requires additional memory to hold the sliced two halves.
    """

    def merge(l, r):
        s = len(l) + len(r)                    # Final size of the product of the merge
        p = [None] * s                         # Allocated memory for the product of the merge
        i_l, i_r = 0, 0                        # Pointers for `l` and `r` arrays
        max_l, max_r = len(l) - 1, len(r) - 1  # Upper bounds for the pointers
        for i in range(0, s):
            # Pointers went out-of-bounds cases (adding element from the remaining side)
            if i_l > max_l:
                p[i] = r[i_r]
                i_r += 1
                continue
            if i_r > max_r:
                p[i] = l[i_l]
                i_l += 1
                continue
            # Picking smaller element at the pointer
            if r[i_r] > l[i_l]:  # Flip this comparison for reversed ordering
                p[i] = l[i_l]
                i_l += 1
            else:
                p[i] = r[i_r]
                i_r += 1
        return p

    n = len(list)
    if n < 2:
        # Base case. Single-element list is already sorted by definition.
        return list
    else:
        # The array will be sliced down recursively to smaller pieces until the base case
        # is hit and then merged back up.
        n_2 = n // 2  # Slice-point
        l = merge_sort(list[0:n_2])
        r = merge_sort(list[n_2:n])
        return merge(l, r)


print(merge_sort([9, 7, 8, 1, 5, 3, 4, 2, 6]))
