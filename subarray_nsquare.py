import random

"""
Andrew McCann
Homework 2
Algorithms & Complexity
CS350
"""

NUM_ELEMENTS = 100

array = []
for i in range(NUM_ELEMENTS):
    array.append(random.randint(-10, 10))

print(array)



def max_subarray(array):
    max_substring = 0
    for i in range(len(array)):
        print("i = %d" % i)
        current_subarray = 0
        for j in range(len(array), i+1, -1):
            print("j = %d" % j)
            current_subarray += array[j-1]
            if current_subarray > max_substring:
                max_substring = current_subarray
        current_subarray = 0
        for k in range(i, len(array)):
            current_subarray += array[k]
            if current_subarray > max_substring:
                max_substring = current_subarray
            print("k = %d" % k)

        print(max_substring)
    print(max_substring)

max_subarray(array)


def merge_subarray(array):
    if len(array) == 1:
        return array[0]

    mid = len(array)//2
    l_array = array[:mid]
    r_array = array[mid:]

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





# Need to brute force, so that means testing every single possible sub string.


