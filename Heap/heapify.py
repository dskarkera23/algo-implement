# Min-Heapify Function
def heapify(arr, n, i):
    smallest = i  # Initialize the smallest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If the left child exists and is smaller than the root
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # If the right child exists and is smaller than the smallest so far
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If the smallest is not the root, swap with the smallest and continue heapifying
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap
        heapify(arr, n, smallest)  # Recursively heapify the affected subtree


# Max-Heapify Function
def heapify_max(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If the left child exists and is larger than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If the right child exists and is larger than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap with the largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify_max(arr, n, largest)  # Recursively heapify the affected subtree


# Function to Build a Min-Heap
def build_heap(arr):
    n = len(arr)

    # Build a min-heap by applying heapify starting from the last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


# Function to Build a Max-Heap
def build_max_heap(arr):
    n = len(arr)

    # Build a max-heap by applying heapify starting from the last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify_max(arr, n, i)


# Example usage
arr_min = [3, 9, 2, 1, 4, 5]
build_heap(arr_min)
print("Min-Heap:", arr_min)  # Output: [1, 3, 2, 9, 4, 5]

arr_max = [3, 9, 2, 1, 4, 5]
build_max_heap(arr_max)
print("Max-Heap:", arr_max)  # Output: [9, 4, 5, 1, 3, 2]
