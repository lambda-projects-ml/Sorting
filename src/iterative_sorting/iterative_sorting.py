
# TO-DO: Complete the selection_sort() function below


arr = [2, 5, 8, 1, 3, 6, 7, 4]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        x = i
        temp = arr[i]
        while x > 0 and temp < arr[x - 1]:
            arr[x] = arr[x - 1]
            x -= 1
            arr[x] = temp
    return arr


print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below

arr = [2, 5, 8, 1, 3, 6, 7, 4]


def bubble_sort(arr):
    for i in range(len(arr)):
        x = i
        temp = arr[i]
        while i > 0:
            if arr[x] < arr[x-1]:
                arr[x] = arr[x-1]
                x-+1
                arr[x] = temp
            elif arr[x] > arr[x+1]:
                arr[x] = arr[x+1]
                i +=1
                arr[x]=temp
            else
                return arr


print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below


# arr = [2, 5, 8, 1, 3, 6, 7, 4]


def count_sort(arr, maximum=-1):

    return arr
