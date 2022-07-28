# Sorting algorithm is a method of arranging a list of numbers in order. There are two types of sorting algorithms: 1.Comparison-based sorting algorithms 2.Non-comparison-based(also known as linear time) sorting algorithms
# Comparison: Quick, merge,Bubble, Selection, Insertion, Heap; Minimum time complexity: O(nlogn)
# Non-comparison based: Counting, Bucket, Radix; Minimum time complexity: O(n)
# O(n)< O(nlogn)
# function to sort an array of integers using selection sort (O(n^2))

def selection_sort(arr):
    # The idea is to loop through the array and find the minimum element and swap it with the current element.
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

# Whenever minimum number of swaps is required, we can use selection sort.
# Number of comparisons in selection sort:O(n^2) [after each 1 element is less(ex: 1st pass n-1, 2nd pass n-2, so on..), n-1+n-2+...3+2+1=n(n-1)/2]
# Number of swaps in selection sort:O(n) [after each pass 1 swap is done, so its 1+1+1...+1 till (n-1)swaps are done])]
# Time complexity: O(n^2)