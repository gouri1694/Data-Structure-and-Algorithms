# Given Log(n) sorted subarrays each of size n/log(n). Find single sorted array.
# Size of single sorted array will be n/log(n)*log(n)=n
# After first merge procedure,  each sorted subarrays will be of size 2n/log(n) and total size of sorted array will be 
# [2n/log(n)]*[log(n)/2]=n
# In second merge procedure, each sorted subarrays will be of size 4n/log(n) and total size of sorted array will be n
# Suppose we have k levels, then logn/2^k=1,2^k=logn. k=log2(logn)
# Time complexity: O(nlog2(log(n)))

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    while len(arr)>1:
        merged_list=[]
        for i in range(0,len(arr),2):
            left=arr[i]
            right=arr[i+1] if i+1<len(arr) else []
            merged_list.append(merge(left,right))
        arr=merged_list
    return arr[0]
# Function to merge 2 sorted arrays into 1 sorted array
def merge(first,second):
    result=[]
    while len(first)>0 and len(second)>0:
        if first[0]<second[0]:
            result.append(first[0])
            first=first[1:]
        else:
            result.append(second[0])
            second=second[1:]
    result=result+first+second
    return result
if __name__ == '__main__':
    print(merge_sort([[1, 3,23,67], [2,5, 7, 9], [0,4, 6, 8, 97]]))