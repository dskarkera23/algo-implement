def quickSort(arr,low,high):
        # code here
        if low<high:
            s=partition(arr,low,high)
            quickSort(arr,low,s-1)
            quickSort(arr,s+1,high)
    
def partition(arr,low,high):
        # code here
        pivot=arr[high]
        i=low-1
        for j in range(low,high+1):
            if arr[j]<pivot:
                i+=1
                arr[j],arr[i]=arr[i],arr[j]
        arr[high],arr[i+1]=arr[i+1],arr[high]
        return i+1

ip=[4,1,2,3,6,1,5]
quickSort(ip,0,len(ip)-1)
print(ip)

"""
Output:
[1, 1, 2, 3, 4, 5, 6]

each iteration of i:
|[4]|[1]1, 2, 3, 6, 1, 5
[1]|[4]|1, 2, 3, 6, 1, 5
|[2]|[3]1, 4, 6, 1, 5
[2]|[3]|1, 4, 6, 1, 5
1, 2, 3, 4,|[1]|[6]5
1, 2, 3, 4, [1]|[5]|6
1, 1, 2, 3, 4|, 5, 6|

In each iteration of the merge sort algorithm, 
the array is recursively divided into smaller 
subarrays until each subarray contains a single 
element, and then these subarrays are merged back
together in a sorted order, gradually building 
up the fully sorted array.

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""