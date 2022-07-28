# Insertion Sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
# Function to sort an array of integers using insertion sort (O(n^2))
def insertion_sort(arr):
    # loop through the array
    for i in range(1, len(arr)):
        # set the current element as the key
        key = arr[i]
        # set the index of the current element
        j = i - 1
        # loop through the array again
        while j >= 0 and key < arr[j]:
            # swap the elements
            arr[j + 1] = arr[j]
            # decrement the index
            j -= 1
        # insert the key at the correct index
        arr[j + 1] = key
    return arr
print(insertion_sort([67,1, 3,23, 5, 7, 9, 2, 4, 6, 8, 0,97]))
# # Number of comparisons in insertion sort:O(n^2) [after each 1 element is less(ex: 1st pass n-1, 2nd pass n-2, so on..), n-1+n-2+...3+2+1=n(n-1)/2]
# # Number of swaps in insertion sort:O(n^2) [after each pass n-1 swap is done, so its n-1+n-2+...3+2+1=n(n-1)/2]
# # Time complexity: O(n^2)

# Best case time complexities: O(n);
# Worst case time complexities: O(n^2)
# Average case time complexities: O(n^2)
# Best case number of comparisons: O(n); n-1
# Worst case number of comparisons: O(n^2)
# Average case number of comparisons: O(n^2)
# Best case number of swaps: 0
# Worst case number of swaps: O(n)
# Average case number of swaps: O(n)