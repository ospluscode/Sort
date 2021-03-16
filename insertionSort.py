
# Insertion Sort is similar to Selection but it gets the First instead of Min
# Get the first element, bring to sorted, then get the next and compare with sorted and put on place
# TC: O(n^2)  SC: O(1)


def insertionSort(custom_list):
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i-1
        while j>=0 and key < custom_list[j]:
            # swap
            custom_list[j+1] = custom_list[j]
            j -= 1
        custom_list[j+1] = key
    return custom_list