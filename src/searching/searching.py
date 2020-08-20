# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if target <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        
        elif target < arr[mid]:
            rec_end = mid - 1
            return binary_search(arr, target, start, rec_end)

        else:
            rec_start = mid + 1
            return binary_search(arr, target, rec_start, end)
    else: 
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

