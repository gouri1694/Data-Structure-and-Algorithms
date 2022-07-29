# Function to find missing number in an array of integers using formula
# Time complexity: O(n)
def missing_number(arr):
    # Find the sum of all the elements in the array
    sum_of_array = sum(arr)
    # Find the sum of all the numbers between 1 and the length of the array
    sum_of_expected_array = (len(arr) + 1) * (len(arr) + 2) / 2
    # Return the difference between the two
    return int(sum_of_expected_array - sum_of_array)
print(missing_number([1,2,3,5,6,7,8,9,4]))

# Function to find missing number in an array of integers using XOR and functools
# XOR Property: 1. a xor 0 = a      2. a xor a = 0          3. a xor b xor a = b
# Time complexity: O(n)
import functools
def missing_number_xor(arr):
    # Find the XOR of all the elements in the array
    xor_of_array = functools.reduce(lambda x, y: x ^ y, arr)
    # Find the XOR of all the numbers between 1 and the length of the array
    xor_of_expected_array = functools.reduce(lambda x, y: x ^ y, range(1, len(arr) + 2))
    # Return the XOR of the two
    return xor_of_expected_array ^ xor_of_array
print(missing_number_xor([1,2,3,5,6,7,8,9,4]))

# Function to find missing number in an array of integers using XOR
def missing_number_xor2(arr):
    # Find the XOR of all the elements in the array
    xor_of_array=arr[0]
    # xor_of_expected_array=1
    for i in range(1,len(arr)):
        xor_of_array=xor_of_array^arr[i]
    # Find the XOR of all the numbers between 1 and the length of the array
    for i in range(1,len(arr)+2):
        xor_of_array=xor_of_array^i
    # Return the XOR of the two
    return xor_of_array
print(missing_number_xor2([1,2,3,5,6,7,8,9,4]))