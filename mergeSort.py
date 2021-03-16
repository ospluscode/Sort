
# Merge Sort divides list into 2 halves until cant divide
# then merges the laves by sorting them

# TC: O(NLogN)
# SC: O(N)


# takes first index , middle and last index
def merge(custom_list, first, middle, last):
    # first subarray and second subarray elems
    num1 = middle - first + 1
    num2 = last - middle

    # right and left subrarrays
    left_temp = [0] * (num1)
    right_temp = [0] * (num2)

    # copy elements from input list to subarrays
    for i in range(0, num1):
        left_temp[i] = custom_list[first+i]
    
    for j in range(0, num2):
        right_temp[j] = custom_list[middle+1+j]

    # first index of first subarray
    i = 0
    # first index of second subarray
    j = 0
    # first index of merged subarray
    k = first

    # Merging with sorted order
    while i < num1 and j < num2:
        if left_temp[i] <= right_temp[j]:
            custom_list[k] = left_temp[i]
            i += 1
        else:
            custom_list[k] = right_temp[j]
            j += 1
        k += 1

    # copy elements of left sarray, if there are any
    while i < num1:
        custom_list[k] = left_temp[i]
        i += 1
        k += 1

    # copy elements of right sarray, if there are any
    while j < num2:
        custom_list[k] = right_temp[j]
        j += 1
        k += 1


# first index and last index of list
def mergeSort(custom_list, first, last):
    if first < last:
        middle = (first+(last-1))//2
        # These calls will be recursive
        # merge sort for first part
        mergeSort(custom_list, first, middle)
        # second part
        mergeSort(custom_list, middle+1, last)
        # divide and merge the parts
        merge(custom_list, first, middle, last)
    return custom_list        