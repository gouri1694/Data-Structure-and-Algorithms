# Bubble sort is a simple sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
# # function to sort an array of integers using bubble sort (O(n^2))
def bubble_sort(arr):
    # loop through the array till end-1
    for i in range(len(arr)-1):
        # loop through the array again till end-i-1
        for j in range(len(arr) - i-1):
            # if the current element is greater than the next element
            if arr[j] > arr[j + 1]:
                # swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(bubble_sort([67,1, 3,23, 5, 7, 9, 2, 4, 6, 8, 0,97]))
# # Number of comparisons in bubble sort:O(n^2) [after each 1 element is less(ex: 1st pass n-1, 2nd pass n-2, so on..), n-1+n-2+...3+2+1=n(n-1)/2]
# # Number of swaps in bubble sort:O(n^2) [after each pass n-1 swap is done, so its n-1+n-2+...3+2+1=n(n-1)/2]
# # Time complexity: O(n^2)