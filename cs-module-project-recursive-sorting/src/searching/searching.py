# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    #check base case
    if start >= end:
        return -1
    else:
        midpoint = (start + end)  // 2
        #if element is present at the midpoint
        if target == arr[midpoint]:
            return midpoint   #return location / index
        elif target < arr[midpoint]:
            # return binary_search(arr, target, start, midpoint-1)
            return binary_search(arr, target, start, midpoint)
        else:
            #return binary_search(arr, target, midpoint+1, end)
            return binary_search(arr, target, midpoint, end)


arr = [-4,-2,2,3,5,6,7,8,10,12]
target = -4

print(binary_search(arr, target, 0, len(arr)-1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

