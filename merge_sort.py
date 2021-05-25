def merge(left_array, right_array, original_array):
    """Merge function takes the left and right array halves and the original non-halved array
        and overwrites the original non-halved while iterating the two as to find the smallest
        elements
        ____________

        PARAMETERS
        ____________

        left_array = left half of the original array
        right_array = right half of the original array
        original_array = original array to be sorted

    """
    left_array_length = len(left_array)
    right_array_length = len(right_array)

    i, j, k = 0, 0, 0
    while i < left_array_length and j < right_array_length:
        if left_array[i] < right_array[j]:
            original_array[k] = left_array[i]
            i += 1
        else:
            original_array[k] = right_array[j]
            j += 1
        k += 1

    while i < left_array_length:
        original_array[k] = left_array[i]
        i += 1
        k += 1

    while j < right_array_length:
        original_array[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(num_array):
    """Merge sort is a divide and conquer sorting algorithm that divides the array
        into two halves and then merges them in a sorted order to sort the passed array.
        The original array is overwritten with the sorted one
        ____________

        PARAMETERS
        ____________

        num_array = list of Integers or Float

    """
    array_length = len(num_array)

    if array_length < 2:
        return

    mid_point = array_length // 2

    left_partition = num_array[:mid_point]
    right_partition = num_array[mid_point:]

    merge_sort(left_partition)
    merge_sort(right_partition)
    merge(left_partition, right_partition, num_array)

