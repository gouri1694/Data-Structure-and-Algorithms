# Function to return minimum and maximum element in an array using divide and conquer approach
def DAC_maxmin(array, low, high):
  max_array = array[low]
  min_array = array[low]

  if low == high:
    return (max_array, min_array)
  
  elif low == high - 1:
    if array[low] > array[high]:
      max_array = array[low]
      min_array = array[high]
    else:
      max_array = array[high]
      min_array = array[low]
    return (max_array, min_array)
  
  else:
    mid = low + (high-low)//2
    max_1, min_1 = DAC_maxmin(array, low, mid)
    max_2, min_2 = DAC_maxmin(array, mid+1, high)

  return (max(max_1,max_2), min(min_1,min_2))

## Driver Code
array = [50, 90, 170, 25, 15, 7, 190, 4, 59,-1]
high = len(array) - 1
low = 0
max_array, min_array = DAC_maxmin(array, low, high)
print("Minimum element in an array:", max_array)
print("Maximum element in an array", min_array)
# print(DAC_maxmin([1,2,3,4,5,6,7,8,9,10],0,9))