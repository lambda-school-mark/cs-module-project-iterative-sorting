def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] is target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr) - 1
    right_is_greater = left <= right

    while right_is_greater:
        midpoint = (left + right) // 2

        # what if the midpoint is the target
        if arr[midpoint] == target:
            return midpoint

        # if midpoint is less than target, start from left
        if arr[midpoint] < target:
            left = midpoint + 1

        else:
            right = midpoint - 1

    return -1  # not found
