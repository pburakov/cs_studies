"""
Build a Binary Search Tree
==========================

Implement an algorithm to build a BST from a sorted array of integers, for instance
:math:`\{1,2,3,4,5,6\}`. Return the root of a tree.

"""
from trees.bst import Node as Node


def build_tree(A, l=None, r=None):
    """Builds a binary search tree from a sorted array.

    Algorithm is a basic inverted version of a binary search. A tree is guaranteed to be a
    properly balanced BST, because the array is already sorted.

    Complexity:
        :math:`O(n)`, bound by the size of an array.

    :param list[int] A: Input array.
    :param int l: Left index (used in recursion).
    :param int r: Right index (used in recursion).
    :return: Root node of created tree.

    """
    if l is None or r is None:
        l, r = 0, len(A) - 1  # Initialize indices
    if l > r:
        return None
    i = l + (r - l) // 2
    root = Node(A[i])
    root.left = build_tree(A, l, i - 1)
    root.right = build_tree(A, i + 1, r)
    return root
