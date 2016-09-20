def find(A):
    """
    Finds majority element in the list.

    This solution implements Moore’s Voting Algorithm which is a two step process. First
     we get an element occurring most of the time in the array. By counting we evaluate
     if our candidate is supported by more occurring elements. We reset the counter if it
     went below zero.

    Statistically, the first step may give us a false positive. On the second step we
     check if the element obtained from above step is in fact a majority element.

    Complexity: O(n), no extra space is used
    :param list[object] A: Input list
    :return Optional[object]: Majority element or None if not found
    """
    c = 0  # Candidate index
    count = 1
    n = len(A)
    for i in range(1, n):
        if A[c] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            c = i
            count = 1
    candidate = A[c]
    count = 0
    for a in A:
        if a == candidate:
            count += 1
    if count >= n / 2:
        return candidate
    else:
        return None
