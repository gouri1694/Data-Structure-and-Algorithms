# Sorting algorithm is a method of arranging a list of numbers in order. There are two types of sorting algorithms: 1.Comparison-based sorting algorithms 2.Non-comparison-based(also known as linear time) sorting algorithms
# Comparison: Quick, merge,Bubble, Selection, Insertion, Heap; Minimum time complexity: O(nlogn)
# Non-comparison based: Counting, Bucket, Radix; Minimum time complexity: O(n)
# O(n)< O(nlogn)
# function to sort an array of integers using selection sort (O(n^2)
def selection_sort(arr):
    # loop through the array
    for i in range(len(arr)):
        # set the minimum to the current index
        min_index = i
        # loop through the array again
        for j in range(i + 1, len(arr)):
            # if the current element is less than the minimum
            if arr[j] < arr[min_index]:
                # set the minimum to the current index
                min_index = j
        # swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print(selection_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
