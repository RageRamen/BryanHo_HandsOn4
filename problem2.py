
def remove_dupes(sorted_array):
    i = 1
    while i < len(sorted_array):
        previous = sorted_array[i - 1]
        current = sorted_array[i]

        if previous == current:
            sorted_array.pop(i)
        else:
            i += 1

    return sorted_array


# Test cases
array = [2, 2, 2, 2, 2]
array = remove_dupes(array)

print(array)

array = [1, 2, 2, 3, 4, 4, 4, 5, 5]
array = remove_dupes(array)

print(array)