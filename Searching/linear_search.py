"""
Algorithm:
linear_search (list, value)
//Input: An array 'list' of elements , a key to be found 'value'
//Output: Position of value in list
   for each item in the list
      if match item == value
         return the item's location
"""
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [1, 2, 9, 3, 7, 4, 5, 6]
pos=linear_search(arr,5)
print(pos+1)

"""
Output:
for key=5:
7
for key=0:
-1

In a single iteration compares the key with the value 
of the cuurent ele of arr , if matches returns index 
if not return -1

Time Complexity: O(n)
Space Complexity: O(1)
"""