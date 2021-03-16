
# Selection Sort finds the minimum element and
# bring it to the start of the list

# TC: O(n^2)  SC: O(1)

def selectionSort(custom_list):
    for i in range(len(custom_list)):
        # start from 0
        min_index = i
        # compare with all the other elements
        for j in range(i+1, len(custom_list)):
            # if any element is less than min, swap index
            if custom_list[min_index] > custom_list[j]:
                min_index = j
        # swap element positions
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
    print(custom_list)