# Function to search element of a sorted 2D array and return the index of the element
# if the element is not found, return -1
# Brute-force search: O(n^2)
def search2DArray1(arr, n, x):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == x:
                return i, j
    return -1

# O(n) search
def search2DArray(arr, target):
    row = 0
    col = len(arr[0]) - 1
    n=len(arr)
    while row < n and col >= 0:
        if arr[row][col] == target:
            return row, col
        elif arr[row][col] > target:
            col -= 1
        else:
            row += 1
    return -1
print(search2DArray([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1))