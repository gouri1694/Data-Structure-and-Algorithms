# Inversion count for an array is the number of inversions in the array.It indicates how far the array is from being sorted
# If array is already sorted, then inversion count is 0. If array is sorted in reverse order, then inversion count is equal to number of elements in array.
# Function to return number of inversions in an array

def number_of_inversions(arr):
    # Find the number of inversions using brute-force approach
    # Time complexity: O(n^2)
    number_of_inversions = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                number_of_inversions += 1
    return number_of_inversions
print(number_of_inversions([1,2,3,4,5,6,7,8,9,10]))
print(number_of_inversions([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(number_of_inversions([1,21,3,4,5,6,75,8,9,10,11,12,13,14,15,16]))
# Function to return number of inversions in an array using divide and conquer
# How to get number of inversions in merge()? 
# In merge process, let i is used for indexing left subarray and j is used for indexing right subarray. At any step in merge(), if ith array element is greater than jth array element, then there are mid-i inversions. coz,left and right subarray are sorted, so all remaining elements in left subarray will be greater than jth array element.
# Approach: Enhance merge sort
def mergeSort(arr, n):
    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)


def _mergeSort(arr, temp_arr, left, right):
  inv_count = 0
  if left < right:
    mid = left + (right - left)//2
    inv_count += _mergeSort(arr, temp_arr, left, mid)
    inv_count += _mergeSort(arr, temp_arr, mid + 1, right)
    inv_count += merge(arr, temp_arr, left, mid, right)
  return inv_count
 
def merge(arr, temp_arr, left, mid, right):
    i = left     
    j = mid + 1 
    k = left    
    inv_count = 0
    while i <= mid and j <= right:
      if arr[i] <= arr[j]:          ## No Inversions
        temp_arr[k] = arr[i]
        k += 1
        i += 1
      else:
        temp_arr[k] = arr[j]        ## Inversion will occur.
        inv_count += (mid-i + 1)    ## Number of swaps
        k += 1
        j += 1
 
    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
 
    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
 
    # Copy the sorted subarray into Original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
         
    return inv_count
 
# Driver Code
# array = [70, 50, 60, 10, 20, 30, 80, 15]
array=[1,21,3,4,5,6,75,8,9,10,11,12,13,14,15,16]
n = len(array)
count = mergeSort(array, n)
print("Number of Inversions are:", count)