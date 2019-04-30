
# TO-DO: Complete the selection_sort() function below


arr = [2, 5, 8, 1, 3, 6, 7, 4]


def instertion_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        x = i
        temp = arr[i]
        while x > 0 and temp < arr[x - 1]:
            arr[x] = arr[x - 1]
            x -= 1
            arr[x] = temp
    return arr


print(instertion_sort(arr))


arr = [2, 5, 8, 1, 3, 6, 7, 4]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below


arr = [2, 5, 8, 1, 3, 6, 7, 4]


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Recrusive version

# def bubble_sort(arr):
#     swapped = False
#     for i in range(0, len(arr) - 1):
#         if arr[i+1] < arr[i]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
    # swapped = True
    # if swapped:
    #     return bubble_sort(arr)
    # return arr


print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below


# arr = [2, 5, 8, 1, 3, 6, 7, 4]


def count_sort(arr, maximum=-1):

    return arr
