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

Each iteration of partitioning:
[4, 1, 2, 3, 6, 1, 5] -> Pivot: 5, Partitioned: [4, 1, 2, 3, 1, |5|, 6]
[4, 1, 2, 3, 1, |5|, 6] -> Pivot: 1, Partitioned: [|1|, 1, 2, 3, 4, 5, 6]
[1, 1, 2, 3, 4, |5|, 6] -> Pivot: 4, Partitioned: [1, 1, 2, 3, |4|, 5, 6]
[1, 1, 2, 3, |4|, 5, 6] -> Pivot: 3, Partitioned: [1, 1, 2, |3|, 4, 5, 6]
[1, 1, 2, |3|, 4, 5, 6] -> Pivot: 2, Partitioned: [1, 1, |2|, 3, 4, 5, 6]
[1, 1, |2|, 3, 4, 5, 6] -> Pivot: 1, Partitioned: [1, |1|, 2, 3, 4, 5, 6]
[1, |1|, 2, 3, 4, 5, 6]

In each iteration of the quick sort algorithm, 
a pivot element is chosen, and the array is 
partitioned such that elements smaller than the 
pivot are placed to its left, and elements 
greater are placed to its right. The process 
is recursively applied to the subarrays, 
gradually sorting the entire array.

Time Complexity: O(nlogn) , worst case O(n^2)
Space Complexity: O(logn) (due to the recursive stack)
"""