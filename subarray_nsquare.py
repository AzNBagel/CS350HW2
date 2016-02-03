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

# Need to brute force, so that means testing every single possible sub string.


