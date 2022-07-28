# function to find the index of the first occurrence of an element in a sorted array
# returns -1 if the element is not in the array
def binary_search(arr, target):
    # set the left and right pointers
    left = 0
    right = len(arr) - 1
    # while the left pointer is less than or equal to the right pointer
    while left <= right:
        # set the midpoint
        # mid = (left + right) // 2
        mid=left+(right-left)//2
        # if the target is equal to the midpoint
        if arr[mid] == target:
            # return the midpoint
            return mid
        # if the target is less than the midpoint
        elif target < arr[mid]:
            # set the right pointer to the midpoint - 1
            right = mid - 1
        # if the target is greater than the midpoint
        else:
            # set the left pointer to the midpoint + 1
            left = mid + 1
    # if the target is not in the array
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# function to find the index of the first occurrence of an element in a sorted array with recursion
# returns -1 if the element is not in the array
def binary_search_recursive(arr, target, left, right):
    # if the left pointer is greater than or equal to the right pointer
    if left >= right:
        # return -1
        return -1
    # set the midpoint
    # mid = (left + right) // 2
    mid=left+(right-left)//2 # This avoids overflow
    # overflow is when the midpoint is greater than the right pointer, which is the case when the array is not sorted and the target is not in the array and the midpoint is the last element in the array ex: [1,2,3,4,5,6,7,8,9,10] and the target is 11 mid=10 right=10 left=10. How (left+right)//2 have overflow? left+right=10+10=20. 20//2=10. 
    # Suppose your 'low' and 'high' are 16 bit unsigned integers. That means, they can only have a maximum value of 2^16=65536. Consider this, low = 65530 high = 65531 If we added them first, (low+high) would end up being junk since that big a number (131061) cannot be stored in a your 16-bit integer. And so, mid would be a wrong value. Instead, if we do high-low//2 and then add low, we get the correct value.
    # if the target is equal to the midpoint
    if arr[mid] == target:
        # return the midpoint
        return mid
    # if the target is less than the midpoint
    elif target < arr[mid]:
        # set the right pointer to the midpoint - 1
        return binary_search_recursive(arr, target, left, mid - 1)
    # if the target is greater than the midpoint
    else:
        # set the left pointer to the midpoint + 1
        return binary_search_recursive(arr, target, mid + 1, right)
print(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 0, 9))