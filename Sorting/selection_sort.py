"""
Algorithm:
SelectionSort(A[0..n-1])
//Sorts a given array by selection sort
//Input: An array A[0..n-1] of orderable elements
//Output: Array A[0..n-1] sorted in nondecreasing order
for i ←0 to n-2 do
    min←i
    for j ←i + 1 to n-1 do
        if A[j ]<A[min]
            min←j
    swap A[i] and A[min]
"""


def selection_sort(l):
    for i in range(len(l)-1):
        min=i
        for j in range(i+1,len(l)):
            if l[j]<l[min]:
                min=j
        l[i],l[min]=l[min],l[i]
        print(l)
        

ip=[4,1,2,3,6,1,5]
selection_sort(ip)
print(ip)
"""
Output:
[1, 1, 2, 3, 4, 5, 6]

each iteration of i:
[1|, 4, 2, 3, 6, 1, 5]
[1, 1|, 2, 3, 6, 4, 5]
[1, 1, 2|, 3, 6, 4, 5]
[1, 1, 2, 3|, 6, 4, 5]
[1, 1, 2, 3, 4|, 6, 5]
[1, 1, 2, 3, 4, 5|, 6]

In each iteration of the selection sort algorithm,
the smallest unsorted element is placed at its 
correct position at the beginning of the list, 
and it is not touched in subsequent iterations.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""