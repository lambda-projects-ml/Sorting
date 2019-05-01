import random
arr = [random.randint(0, 100) for i in range(0, 20)]


def quick_sort(arr, low, high):
    # base case
    if low >= high:
        return arr

    # Start by choosing a pivot
    else:
        # divide
        pivot_index = low

        for i in range(low, high):
            # Move all elements smaller than pivot to its left-hand side. Move all elements larger than pivot to its right-hand side.
            if arr[i] < arr[pivot_index]:
                arr[i], arr[pivot_index+1] = arr[pivot_index+1], arr[i]
                # swap pivot with element on its right
                arr[pivot_index], arr[pivot_index +
                                      1] = arr[pivot_index + 1], arr[pivot_index]

    # (recursive case) Recursively Quick Sort LHS and RHS until (base case) a side only contains a single element
    arr = quick_sort(arr, low, pivot_index)

    arr = quick_sort(arr, pivot_index+1, high)

    return arr


# print(quick_sort([1, 3, 5, 7, 2, 8, 9, 4, 6],
#                  0, len([1, 3, 5, 3, 2, 8, 9, 5, 3])))

# TO-DO: complete the helpe function below to merge 2 sorted arrays
array = [random.randint(0, 100) for i in range(0, 20)]


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    ia = 0
    ib = 0

    for i in range(0, len(merged_arr)):
        if len(arrA)-1 < ia:
            merged_arr[i] = arrB[ib]
            ib += 1
        elif len(arrB)-1 < ib:
            merged_arr[i] = arrA[ia]
            ia += 1
        elif arrA[ia] <= arrB[ib]:
            merged_arr[i] = arrA[ia]
            ia += 1
        else:
            merged_arr[i] = arrB[ib]
            ib += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    if len(arr) > 1:
        left = merge_sort(arr[: (len(arr)//2)])
        right = merge_sort(arr[(len(arr)//2):])
        arr = merge(left, right)

    return arr


# print(array)
print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
