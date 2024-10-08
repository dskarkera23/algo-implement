## Sorting Algorithms Overview

The following table summarizes the time and space complexity of each sorting algorithm for both best and worst-case scenarios:

| Algorithm      | Best Case Time Complexity | Worst Case Time Complexity | Space Complexity |
|----------------|---------------------------|----------------------------|------------------|
| **Bubble Sort**    | O(n)                        | O(n²)                       | O(1)             |
| **Selection Sort** | O(n²)                       | O(n²)                       | O(1)             |
| **Insertion Sort** | O(n)                        | O(n²)                       | O(1)             |
| **Merge Sort**     | O(n log n)                  | O(n log n)                  | O(n)             |
| **Quick Sort**     | O(n log n)                  | O(n²)                       | O(log n)         |

## Algorithm Descriptions

- **Bubble Sort**: Repeatedly swaps adjacent elements if they are in the wrong order. The algorithm gets its name because smaller elements "bubble" to the top of the list.

- **Selection Sort**: Selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first unsorted element. This process is repeated until the entire list is sorted.

- **Insertion Sort**: Builds the sorted array one element at a time by repeatedly picking the next element and inserting it into its correct position in the sorted portion of the list.

- **Merge Sort**: A divide-and-conquer algorithm that divides the list into smaller sublists, sorts each sublist, and then merges them back together in sorted order.

- **Quick Sort**: Another divide-and-conquer algorithm that selects a "pivot" element, partitions the array around the pivot, and recursively sorts the subarrays.
