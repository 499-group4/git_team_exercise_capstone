def bubble_sort(array):
    """An implementation of bubble sort which takes
       a list of numbers and returns the list in 
       sorted order"""

    if(len(array)<=0): return
    # loop through the list n times
    for element in array:
        # sequentially compare each value to the next
        for i in range(0,len(array)-1):
            # if left value is larger than right-> swap
            if(array[i] > array[i+1]):
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array

