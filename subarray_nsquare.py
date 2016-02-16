import random

"""
Andrew McCann
Homework 2
Algorithms & Complexity
CS350
"""

NUM_ELEMENTS = 11
LOW_VAL = -10
HIGH_VAL = 10

array = []
for i in range(NUM_ELEMENTS):
    array.append(random.randint(LOW_VAL, HIGH_VAL))

print(array)




def max_subarray(array):
    max_substring = LOW_VAL
    for i in range(len(array)):
        current_subarray = 0
        for j in range(i, len(array)):
            current_subarray += array[j]
            if current_subarray > max_substring:
                max_substring = current_subarray
    print(max_substring)





def merge_subarray(array):
    if len(array) == 1:
        # Return the max value and the array
        return array[0], array
    # Split the array using // to make sure its an integer line.
    mid = len(array)//2
    l_array = array[:mid]
    r_array = array[mid:]
    # Have great faith that this will work.
    # Ideally it will return the maximum sub array.
    l_max, l_result_array = merge_subarray(l_array)
    r_max, r_result_array = merge_subarray(r_array)



    left_side = 0
    left_max = LOW_VAL
    for num in reversed(l_result_array):
        left_side += num
        if left_side > left_max:
            left_max = left_side

    right_side = 0
    right_max = LOW_VAL
    for num in r_result_array:
        right_side += num
        if right_side > right_max:
            right_max = right_side

    spanning_total = right_max + left_max

    left_right_max = max(l_max, r_max)
    real_max = max(left_right_max, spanning_total)

    return real_max, l_result_array + r_result_array


# Pulled Mergesort from Interactivepython.org
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1




max_subarray(array)

print(merge_subarray(array))


