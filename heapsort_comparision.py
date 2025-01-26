# Heapsort Algorithm Implementation 

def heapify(array, size, current_idx):
    largest = current_idx  # Assume current_idx is the largest
    left_child_idx = 2 * current_idx + 1  # Left child index
    right_child_idx = 2 * current_idx + 2  # Right child index

    # Check if left child exists and is larger than the root
    if left_child_idx < size and array[left_child_idx] > array[largest]:
        largest = left_child_idx

    # Check if right child exists and is larger than the current largest
    if right_child_idx < size and array[right_child_idx] > array[largest]:
        largest = right_child_idx

    # If the largest is not the root, swap and continue heapifying the affected subtree
    if largest != current_idx:
        array[current_idx], array[largest] = array[largest], array[current_idx]
        heapify(array, size, largest)

def build_max_heap(arr):
    length = len(arr)
    # Start from the last non-leaf node and ensure heap property
    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, length, i)

def perform_heapsort(arr):
    length = len(arr)
    build_max_heap(arr)  # Convert the array into a max heap

    # Extract max element from the heap and adjust the heap
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root with the last element
        heapify(arr, i, 0)  # Re-adjust the heap after extraction

# Example usage of Heapsort
array = [10, 40, 30, 20, 50]
perform_heapsort(array)  # Sorting the array using Heapsort
print("Sorted array:", array)

# Empirical Comparison of Sorting Algorithms
import time
import random

# Generate data sizes for testing
sizes = [100, 1000, 5000, 10000]

# QuickSort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted
    pivot = arr[len(arr) // 2]  # Select the pivot element (middle element)
    smaller = [x for x in arr if x < pivot]  # Elements smaller than pivot
    equal = [x for x in arr if x == pivot]  # Elements equal to pivot
    larger = [x for x in arr if x > pivot]  # Elements larger than pivot
    return quicksort(smaller) + equal + quicksort(larger)  # Recursively sort

# MergeSort implementation
def merge(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted
    mid = len(arr) // 2  # Find the middle index
    left_sorted = merge(arr[:mid])  # Recursively sort the left half
    right_sorted = merge(arr[mid:])  # Recursively sort the right half
    return merge_sorted_lists(left_sorted, right_sorted)

# Merge two sorted arrays into one sorted array
def merge_sorted_lists(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Add remaining elements from left
    result.extend(right[j:])  # Add remaining elements from right
    return result

# Function to measure time taken by each sorting algorithm
def measure_sort_time(sort_func, data):
    start_time = time.time()
    sort_func(data)  # Perform the sorting
    return time.time() - start_time  # Return the time taken

# Store the sorting times for comparison
sorting_times = {"Heapsort": [], "Quicksort": [], "Mergesort": []}

for size in sizes:
    test_data = [random.randint(0, 10000) for _ in range(size)]  # Generate random test data
    for sort_name, sort_func in zip(sorting_times.keys(), [perform_heapsort, quicksort, merge]):
        sorting_times[sort_name].append(measure_sort_time(sort_func, test_data.copy()))  # Measure time

# Display the sorting time comparison results
for sort_name, timings in sorting_times.items():
    print(f"{sort_name}:")
    for size, time_taken in zip(sizes, timings):
        print(f"  Input Size: {size}, Time: {time_taken:.6f} seconds")
