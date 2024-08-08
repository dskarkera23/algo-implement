"""
Algorithm:
Mergesort(A[0..n-1])
//Sorts array A[0..n-1] by recursive mergesort
//Input: An array A[0..n-1] of orderable elements
//Output: Array A[0..n-1] sorted in nondecreasing order
    if n > 1
        copy A[0.._n/2_-1] to B[0.._n/2_-1]
        copy A[_n/2_..n-1] to C[0.._n/2_-1]
        Mergesort(B[0.._n/2_-1])
        Mergesort(C[0.._n/2_-1])
        Merge(B, C, A)
    Merge(B[0..p-1], C[0..q-1], A[0..p + q-1])
//Merges two sorted arrays into one sorted array
//Input: Arrays B[0..p-1] and C[0..q-1] both sorted
//Output: Sorted array A[0..p + q-1] of the elements of B and C
    i ←0; j ←0; k←0
    while i <p and j <q do
        if B[i]≤ C[j ]
            A[k]←B[i]; i ←i + 1
        else
            A[k]←C[j ]; j ←j + 1
        k←k + 1
    if i = p
    copy C[j..q-1] to A[k..p + q-1]
    else
    copy B[i..p-1] to A[k..p + q-1]
"""
def merge(arr, l, m, r): 
        i=l
        j=m+1
        ans=[]
        while i<=m and j<=r:
            if arr[i]<arr[j]:
                ans.append(arr[i])
                i+=1
            else:
                ans.append(arr[j])
                j+=1
        if i>m:
            while j<=r:
                ans.append(arr[j])
                j+=1
        else:
            while i<=m:
                ans.append(arr[i])
                i+=1
        for i in range(l,r+1):
            arr[i]=ans[i-l]
        #print(f"{arr[:l]}|{arr[l:r+1]}|{arr[r+1:]}")       
def mergeSort(arr, l, r):
        if l<r:
            m=(l+r)//2
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            merge(arr,l,m,r)
            

ip=[4,1,2,3,6,1,5]
mergeSort(ip,0,len(ip)-1)
#print(ip)

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