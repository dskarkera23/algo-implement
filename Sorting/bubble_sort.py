"""
Algorithm:
BubbleSort(A[0..n-1])
//Sorts a given array by bubble sort
//Input: An array A[0..n-1] of orderable elements
//Output: Array A[0..n-1] sorted in nondecreasing order
for i ←0 to n-2 do
    for j ←0 to n-2-i do
        if A[j + 1]<A[j ]
            swap A[j ] and A[j + 1]
"""


def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j+1]<l[j]:
                l[j],l[j+1]=l[j+1],l[j]
        

ip=[4,1,2,3,6,1,5]
bubble_sort(ip)
print(ip)
"""
Output:
[1, 1, 2, 3, 4, 5, 6]

each iteration of i:
[1, 2, 3, 4, 1, 5,|6]
[1, 2, 3, 1, 4,|5, 6]
[1, 2, 1, 3,|4, 5, 6]
[1, 1, 2,|3, 4, 5, 6]
[1, 1,|2, 3, 4, 5, 6]
[1,|1, 2, 3, 4, 5, 6]

In each iteration of the bubble sort algorithm, 
the largest unsorted element is placed at its 
correct position at the end of the list, and 
it is not touched in subsequent iterations.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""