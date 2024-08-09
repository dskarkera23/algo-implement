"""
Algorithm:
BinarySearch(A[0..n-1],key)
//Search for the key element in the array sorted in non-decreasing order.
//Input: An array A[0..n-1] sorted in non-decreasing order, key element to be searched
//Output: Position of key elements in array A
    low ← 0; high←n-1
    while low <=high do
        mid ← (low+high)/2
        if A[mid]=key
            return mid
        if key < A[mid]
            high ← mid -1
        else
            low ← mid + 1
    return -1
"""
def binary_search(arr,key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        print(arr[low:high+1])
        if key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = [1, 2, 9, 3, 7, 4, 5, 6]
arr.sort() #[1,2,3,4,5,6,7,9]
pos=binary_search(arr,5)
print(pos+1)

"""
Output:
for key=5:
5
for key=0:
-1

Iteration:
[1, 2, 3, 4, 5, 6, 7, 9]
[5, 6, 7, 9] //left half discarder

Calculates the mid idx and if mid ele is same as key 
then returns idx mid ,else discards the respective size 
based on mid ele compared with key until its found. 

Time Complexity: O(logn)
Space Complexity: O(1)
"""