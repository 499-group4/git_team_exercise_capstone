def selection_sort(num_array): 
    """Selection sort segments the array into two parts: unsorted and sorted.
       all we do is to check for the min element in the unsorted part and add 
       it after the sorted part. This way the whole array is sorted eventually. 
    ____________

    PARAMETERS 
    ____________
    
    num_array = list of Integers or Float
    returns sorted array. 
    
    """
    #worst case all numbers are unsorted so we have to loop through the length of the array-1
    for i in range(len(num_array)): 
        #assume that the first element of the unsorted part of the array is the smallest.
        min_element_index = i
        for j in range(i+1,len(num_array)): 
            #Traverse thru the unsorted part of the array;

            #if one finds an element smaller than current min element than make that the min element.
            if num_array[j] < num_array[min_element_index]: 
                min_element_index = j 
    #swap current i index with proper min element and this helps section the array in sorted and unsorted. 
        num_array[i], num_array [min_element_index] = num_array[min_element_index], num_array[i]

    return num_array