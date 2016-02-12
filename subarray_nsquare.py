import random

"""
Andrew McCann
Homework 2
Algorithms & Complexity
CS350
"""

NUM_ELEMENTS = 10

array = []
for i in range(NUM_ELEMENTS):
    array.append(random.randint(-10, 10))

print(array)




def max_subarray(array):
    max_substring = 0
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
    l_max = merge_subarray(l_array)
    r_max = merge_subarray(r_array)

    current_val = 0
    if array[0] > 0:
        current_val += array[0]
    if l_max > 0:
        current_val += l_max
    if r_max > 0:
        current_val += r_max



    # Fuck all this shit below
    current_max = array[0]

    if current_max + l_max > l_max:
        current_max += l_max
    if current_max + r_max > r_max:
        current_max += r_max
    if current_max < l_max:
        current_max = l_max
    if current_max < r_max:
        current_max = r_max


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


