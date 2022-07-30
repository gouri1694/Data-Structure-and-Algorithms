# In-place sorting algorithm is a sorting algorithm that works in-place. It does not create a new array.
# Out-place sorting algorithm is a sorting algorithm that creates a new array.
# Merge Sort is a divide and conquer algorithm. It works by breaking down the array into smaller sub-arrays, sorting them individually, and then merging them back together. It is out-place sorting algorithm. It is also stable sort.
# function to sort an array of integers using merge sort (O(nlogn))
def merge_sort(arr):
    # if the array has only 1 element, return it
    if len(arr) <= 1:
        return arr
    # else divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # merge the two halves
    return merge(left, right)
# function to merge two arrays
def merge(left, right):
    # create a new array to store the sorted array
    result = []
    # loop through the two arrays
    while len(left) > 0 and len(right) > 0:
        # if the left element is less than the right element
        if left[0] < right[0]:
            # append the left element to the result
            result.append(left[0])
            # remove the left element from the left array
            left = left[1:]
        # else if the right element is less than the left element
        else:
            # append the right element to the result
            result.append(right[0])
            # remove the right element from the right array
            right = right[1:]
    # append the remaining elements of the left array to the result
    result += left
    # append the remaining elements of the right array to the result
    result += right
    return result
if __name__ == '__main__':
    print(merge_sort([67,1, 3,23, 5, 7, 9, 2, 4, 6, 8, 0,97]))
# log2(n) space is required while merge procedurer is running(stack space).Space complexity: O(n)