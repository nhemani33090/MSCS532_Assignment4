class Task:
    def __init__(self, identifier, priority_level, arrival_time, due_time):
        self.identifier = identifier  # Unique identifier for the task
        self.priority_level = priority_level  # Task priority (higher value means higher priority)
        self.arrival_time = arrival_time  # The time the task arrives
        self.due_time = due_time  # Deadline for the task

# Priority Queue operations using a binary heap (Max-Heap)

# Add a new task to the heap and maintain the heap structure
def add_to_heap(heap, new_task):
    heap.append(new_task)  # Add task to the bottom of the heap
    current_index = len(heap) - 1  # The last index of the heap
    # Maintain heap order by "bubbling up"
    while current_index > 0:
        parent_index = (current_index - 1) // 2
        if heap[parent_index].priority_level >= heap[current_index].priority_level:
            break  # Stop if the heap property is already satisfied
        heap[parent_index], heap[current_index] = heap[current_index], heap[parent_index]  # Swap with parent
        current_index = parent_index
    # Time complexity: O(log n), since the task may need to bubble up from the leaf to the root.

# Remove and return the task with the highest priority
def remove_highest_priority(heap):
    if not heap:
        return None  # Heap is empty, return None
    top_task = heap[0]  # The root has the highest priority task
    heap[0] = heap[-1]  # Replace root with the last task
    heap.pop()  # Remove the last element
    # Reorganize the heap by "bubbling down"
    index = 0
    while 2 * index + 1 < len(heap):  # Check if the current node has children
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index
        if left_child < len(heap) and heap[left_child].priority_level > heap[largest].priority_level:
            largest = left_child
        if right_child < len(heap) and heap[right_child].priority_level > heap[largest].priority_level:
            largest = right_child
        if largest == index:
            break  # The heap property is satisfied
        heap[index], heap[largest] = heap[largest], heap[index]  # Swap with the larger child
        index = largest
    return top_task  # Return the task with the highest priority

# Update the priority of a task and adjust its position in the heap
def modify_task_priority(heap, task_identifier, updated_priority):
    task_index = next((i for i, task in enumerate(heap) if task.identifier == task_identifier), -1)
    if task_index == -1:
        return  # Task not found
    if updated_priority < heap[task_index].priority_level:
        return  # If the updated priority is lower, do nothing
    heap[task_index].priority_level = updated_priority  # Set the new priority
    # Adjust the heap by bubbling up
    while task_index > 0:
        parent_index = (task_index - 1) // 2
        if heap[parent_index].priority_level >= heap[task_index].priority_level:
            break
        heap[parent_index], heap[task_index] = heap[task_index], heap[parent_index]
        task_index = parent_index
    # Time complexity: O(log n), as the task may need to move up the tree.

# Check if the heap (priority queue) is empty
def is_heap_empty(heap):
    return len(heap) == 0  # Returns True if the heap is empty

# Initialize an empty heap
task_heap = []

# Create tasks with task identifier, priority, arrival time, and due time
task1 = Task(1, 50, 1, 5)  # Task ID 1, Priority 50
task2 = Task(2, 30, 2, 6)  # Task ID 2, Priority 30
task3 = Task(3, 40, 3, 7)  # Task ID 3, Priority 40

# Add tasks to the heap
add_to_heap(task_heap, task1)
add_to_heap(task_heap, task2)
add_to_heap(task_heap, task3)

# Display the heap after insertion
print("Heap after insertion:")
for task in task_heap:
    print(f"Task ID: {task.identifier}, Priority: {task.priority_level}")
# Extract the task with the highest priority (root)
highest_priority_task = remove_highest_priority(task_heap)
print(f"\nExtracted Task ID: {highest_priority_task.identifier}, Priority: {highest_priority_task.priority_level}")

# Display the heap after extraction
print("\nHeap after extraction:")
for task in task_heap:
    print(f"Task ID: {task.identifier}, Priority: {task.priority_level}")
# Increase the priority of Task 2 to 60
modify_task_priority(task_heap, task_identifier=2, updated_priority=60)

# Display the heap after increasing the priority
print("\nHeap after increasing the priority of Task 2:")
for task in task_heap:
    print(f"Task ID: {task.identifier}, Priority: {task.priority_level}")

# Check if the heap is empty
print("\nIs the heap empty?", is_heap_empty(task_heap))
