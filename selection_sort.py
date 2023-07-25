def smallest(arr):
    ''' 
    input: list
    output: smallest value's index
    '''
    smallest_value = arr[0]
    smallest_value_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_value_index = i
    
    return smallest_value_index

def selection_sort(arr):
    ''' 
    input: list
    output: sorted list in ascending order
    '''
    new_arr = []
    for i in range(len(arr)):
        smallest_item = smallest(arr)
        new_arr.append(arr.pop(smallest_item))

    return new_arr

print(selection_sort([2,4,5,1,3,3]))