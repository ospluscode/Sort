
# Bucket Sort idea is to create buckets, distribute temp_arrayay values into buckets,
# then sort buckets and merge them

# Number of bucket = round(sqrt(number of elements))
# Which bucket for element = ceiling(value * number of bucket / max value)

# TC: O(n^2) if used Bubble, Selection or Insertion for sorting
#     O(n) if used Quick sort
# SC: O(n) - creating buckets

import math

def bucketSort(custom_list):
    number_of_buckets = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    temp_array = []

    for i in range(number_of_buckets):
        # buckets, 2d array
        temp_array.append([])
    for j in custom_list:
        # insert element to its bucket
        index_b = math.ceil(j*number_of_buckets/max_value)
        temp_array[index_b-1].append(j)

    # sort elements in buckets with Insertion sort (or any other)
    for i in range(number_of_buckets):
        temp_array[i] = insertionSort(temp_array[i])

    # merge buckets
    temp_key = 0
    for i in range(number_of_buckets):
        for j in range(len(temp_array[i])):
            custom_list[temp_key] = temp_array[i][j]
            temp_key += 1
    return custom_list