def merge_sorted_arrays(arrays):
    k = len(arrays)
    n = len(arrays[0])

    merged_array = []

    for i in range(k * n):
        compare_array = []
        mini = float('inf')
        index_pop = -1
        for j, array in enumerate(arrays):
            if array:
                compare_array.append(array[0])
                if array[0] < mini:
                    mini = array[0]
                    index_pop = j

        if index_pop == -1:
            break

        merged_array.append(mini)
        arrays[index_pop].pop(0)

    return merged_array


# Test cases
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]

array_group = [array1, array2, array3]

sorted_merged_array = merge_sorted_arrays([array.copy() for array in array_group])
print(sorted_merged_array)

array1 = [1,3,7]
array2 = [2,4,8]
array3 = [9,10,11]

array_group = [array1, array2, array3]

sorted_merged_array = merge_sorted_arrays([array.copy() for array in array_group])
print(sorted_merged_array)