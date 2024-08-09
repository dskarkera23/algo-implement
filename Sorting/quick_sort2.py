#pivot as first element

def quickSort(arr,low,high):
        if low<high:
            s=partition(arr,low,high)
            quickSort(arr,low,s-1)
            quickSort(arr,s+1,high)
    
def partition(arr,low,high):
    p=arr[low]
    start=low+1
    end=high
    while True:
        while start<=end and arr[end]>=p:
            end-=1
        while start<=end and arr[start]<=p:
            start+=1
        if start<=end:
            arr[end],arr[start]=arr[start],arr[end]
        else:
            break
    arr[end],arr[low]=arr[low],arr[end]
    return end

ip=[4,1,2,3,6,1,5]
quickSort(ip,0,len(ip)-1)
print(ip)

"""
Output:
[1, 1, 2, 3, 4, 5, 6]

Each iteration of partitioning:
[4, 1, 2, 3, 6, 1, 5] -> Pivot: 4, Partitioned: [1, 1, 2, 3, |4|, 6, 5]
[1, 1, 2, 3, 4, 6, 5] -> Pivot: 1, Partitioned: [1, |1|, 2, 3, 4, 6, 5]
[1, 1, 2, 3, 4, 6, 5] -> Pivot: 2, Partitioned: [1, 1, |2|, 3, 4, 6, 5]
[1, 1, 2, 3, 4, 6, 5] -> Pivot: 3, Partitioned: [1, 1, 2, |3|, 4, 6, 5]
[1, 1, 2, 3, 4, 5, 6] -> Pivot: 5, Partitioned: [1, 1, 2, 3, 4, |5|, 6]
[1, 1, 2, 3, 4, 5, 6] -> Pivot: 6, Partitioned: [1, 1, 2, 3, 4, 5, |6|]

In each iteration of the quick sort algorithm, 
a pivot element (the first element of the current segment) is used to partition the array. 
Elements smaller than the pivot are placed to its left, and elements greater are placed to its right. 
The process is recursively applied to the subarrays, 
gradually sorting the entire array.

Time Complexity: O(n log n) on average, O(n²) in the worst case
Space Complexity: O(log n) (due to the recursive stack)
"""