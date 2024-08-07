"""
Algorithm:
InsertionSort(A[0..n-1])
//Sorts a given array by insertion sort
//Input: An array A[0..n-1] of n orderable elements
//Output: Array A[0..n-1] sorted in nondecreasing order
for i ←1 to n-1 do
    v ←A[i]
    j ←i-1
    while j ≥ 0 and A[j]> v do
        A[j + 1]←A[j]
        j ←j-1    
    A[j + 1]←v
"""


def insertion_sort(l):
    for i in range(1,len(l)):
        v=l[i]
        j=i-1
        while j>=0 and l[j]>v:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=v
        print(l)
        

ip=[4,1,2,3,6,1,5]
insertion_sort(ip)
print(ip)
"""
Output:
[1, 1, 2, 3, 4, 5, 6]

each iteration of i:
[1, 4, 2, 3, 6, 1, 5]
[1, 2, 4, 3, 6, 1, 5]
[1, 2, 3, 4, 6, 1, 5]
[1, 2, 3, 4, 6, 1, 5]
[1, 1, 2, 3, 4, 6, 5]
[1, 1, 2, 3, 4, 5, 6]

In each iteration of the insertion sort algorithm, 
the current element is placed at its correct position 
within the already sorted portion of the list, 
and it is not moved in subsequent iterations.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""