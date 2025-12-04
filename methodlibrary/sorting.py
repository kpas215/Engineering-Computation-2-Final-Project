"""
sorting.py
Hybrid Merge + Insertion Sort for movie-related data.

Author: Killian Slattery
Date: [fill in]

This module provides:
    - insertion_sort: simple O(n^2) sort used on small arrays
    - hybrid_merge_sort: merge sort that switches to insertion sort
                         below a size threshold, for efficiency.
"""

def insertion_sort(arr, key=lambda x: x):
    """
    In-place insertion sort.

    arr: list to sort
    key: function that returns the comparison key for each element
         (for example: key=lambda x: x[0] to sort by first entry of a tuple)
    """
    for i in range(1, len(arr)):
        val = arr[i]          # element we want to insert
        j = i - 1

        # Shift elements to the right until the correct spot for `val`
        while j >= 0 and key(arr[j]) > key(val):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = val


def merge(left, right, key):
    """
    Merge step for merge sort. Assumes `left` and `right`
    are sorted according to `key`, returns a new merged list.
    """
    result = []
    i = j = 0

    # Merge until one side is exhausted
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append leftovers from either side
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def hybrid_merge_sort(arr, threshold=16, key=lambda x: x):
    """
    Hybrid merge + insertion sort.

    arr: list to sort (will return a new sorted list)
    threshold: when subarrays are <= this size, use insertion_sort
    key: function used to extract a comparison key from each element
    """
    # Base case: small list → use insertion sort in-place
    if len(arr) <= threshold:
        insertion_sort(arr, key=key)
        return arr

    mid = len(arr) // 2

    # Recursively sort left and right halves
    left = hybrid_merge_sort(arr[:mid], threshold, key=key)
    right = hybrid_merge_sort(arr[mid:], threshold, key=key)

    # Merge the two sorted halves
    return merge(left, right, key)