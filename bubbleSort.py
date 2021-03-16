
# Bubble Sort is the simplest sort (a.k.a Sinking Sort)
# Idea is to compare with the adjacent node and swap if order is wrong
# Repeat this until rightmost node and the loop this process

# Time Complexity: O(n^2)
# Space Complexity: O(1)


def bubbleSort(custom_list):
    for i in range(len(custom_list)-1):
        # compare with adjacents loop
        for j in range(len(custom_list)-i-1):
            # swap condition
            if custom_list[j] > custom_list[j+1]:
                # swapping
                custom_list[j], custom_list[j+1] = custom_list[j+1], custom_list[j]
    print(custom_list)
