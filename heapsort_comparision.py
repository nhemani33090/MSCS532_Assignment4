import time
import random

# Function to generate random, sorted, and reverse-sorted arrays
def generate_array(size, array_type="random"):
    if array_type == "random":
        return [random.randint(0, 10000) for _ in range(size)]  # Generate random values
    elif array_type == "sorted":
        return [i for i in range(size)]  # Create sorted array in ascending order
    elif array_type == "reverse-sorted":
        return [i for i in range(size, 0, -1)]  # Create sorted array in descending order

# Heapsort - maintain the heap property by adjusting the subtree
def adjust_heap(arr, n, index):
    largest = index  # Assume the largest is the current index
    left = 2 * index + 1  # Left child index
    right = 2 * index + 2  # Right child index

    # Compare left child with root
    if left < n and arr[left] > arr[largest]:
        largest = left  # If left child is larger, update largest

    # Compare right child with largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right  # If right child is larger, update largest

    # If the largest is not root, swap and recursively adjust the affected subtree
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]  # Swap the root with the largest child
        adjust_heap(arr, n, largest)  # Recursively heapify the affected subtree

# Build the heap by applying the adjust_heap operation on all non-leaf nodes
def build_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and apply heapify on each node
    for i in range(n // 2 - 1, -1, -1):  # Traverse all non-leaf nodes in reverse order
        adjust_heap(arr, n, i)  # Apply heapify starting from the last non-leaf node

# Perform Heapsort by first building the heap and then extracting elements
def heapsort(arr):
    build_heap(arr)  # Step 1: Build the max heap
    n = len(arr)
    
    # Step 2: Extract the root and adjust the heap after each extraction
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        adjust_heap(arr, i, 0)  # Re-adjust the heap to maintain the max-heap property

# QuickSort implementation
def quicksort(arr):
    """
    QuickSort algorithm that selects a pivot and partitions the array into smaller and larger elements.
    """
    if len(arr) <= 1:  # Base case: single-element or empty array is already sorted
        return arr
    pivot = arr[len(arr) // 2]  # Select the pivot element from the middle of the array
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements larger than pivot
    
    # Recursively sort the subarrays and concatenate the results
    return quicksort(left) + middle + quicksort(right)

# MergeSort implementation
def mergesort(arr):
    """
    MergeSort algorithm that splits the array into halves and merges them in sorted order.
    """
    if len(arr) <= 1:  # Base case: single-element or empty array is already sorted
        return arr
    mid = len(arr) // 2  # Find the midpoint of the array
    left_half = mergesort(arr[:mid])  # Recursively sort the left half
    right_half = mergesort(arr[mid:])  # Recursively sort the right half
    
    # Merge the sorted halves into one sorted array
    return merge(left_half, right_half)

# Merge two sorted arrays into one sorted array
def merge(left, right):
    result = []
    i, j = 0, 0
    # Compare elements from both arrays and append the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1  # Move pointer in the left array
        else:
            result.append(right[j])
            j += 1  # Move pointer in the right array
    
    # Append any remaining elements from both arrays
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Function to measure time taken by each sorting algorithm
def time_sort(sort_func, data):
    start = time.time()  # Record the start time
    sort_func(data)  # Perform the sorting
    return time.time() - start  # Return the elapsed time

# Store sorting times for comparison
sorting_times = []

# Test for different distributions: random, sorted, reverse-sorted
sizes = [100, 1000, 5000, 10000]
distributions = ["random", "sorted", "reverse-sorted"]

# Run the sorting algorithms on various input sizes and distributions
for size in sizes:
    for dist in distributions:
        test_data = generate_array(size, array_type=dist)  # Generate data based on the distribution
        for sort_name, sort_func in zip(["Heapsort", "QuickSort", "MergeSort"], [heapsort, quicksort, mergesort]):
            time_taken = time_sort(sort_func, test_data.copy())  # Measure time for each distribution
            sorting_times.append((size, dist, sort_name, time_taken))

# Display results in columns: Input Size, Distribution, Algorithm, Time
print(f"{'Input Size':<12}{'Distribution':<20}{'Algorithm':<12}{'Time in Seconds'}")
print("-" * 60)

# Print the sorting times in a readable format
for size, dist, algo, time_taken in sorting_times:
    print(f"{size:<12}{dist:<20}{algo:<12}{time_taken:.6f}")
