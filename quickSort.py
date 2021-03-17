# Quick Sort takes a random pivot and then places it as
# all the smaller elements are on left and greater elements are on the right
# then the choosing pivot and moving elements continues recursively
# Unlike Merge Sort Quick doesnt require extra space

# TC: O(NlogN)  - division by half
# SC: O(N)

# Helper method
# Takes last as pivot and place it ass all smaller on left and greater on right
def partition(custom_list, first, last):
    i = first - 1
    # pivot is right most element
    pivot = custom_list[last]
    for j in range(first, last):
        if custom_list[j] <= pivot:
            i += 1
            # swap
            custom_list[i], custom_list[j] = custom_list[j], custom_list[i]
    # if not swap
    custom_list[i + 1], custom_list[last] = custom_list[last], custom_list[i+1]
    return (i + 1)


def quickSort(custom_list, first, last):
    if first < last:
        # recursive calls
        pi = partition(custom_list, first, last)
        quickSort(custom_list, first, pi-1)
        quickSort(custom_list, pi+1, last)