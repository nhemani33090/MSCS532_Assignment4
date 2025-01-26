
# README

## **Priority Queue and Heapsort Implementation**

### **Overview:**
This project implements two important algorithms: **Heapsort** and **Priority Queue** using a **binary heap**. The project consists of two main Python files:
1. **`heapsort_comparision.py`** – Implements the Heapsort algorithm and compares its performance against other sorting algorithms.
2. **`priority_queue.py`** – Implements a priority queue using a binary heap with key operations such as **add_to_heap**, **remove_highest_priority**, **modify_task_priority**, and **is_heap_empty**.

### **Files:**
1. **`heapsort_comparision.py`**
   - Implements the **Heapsort** algorithm.
   - Compares the performance of Heapsort against other sorting algorithms like **QuickSort** and **MergeSort** on various distributions (sorted, reverse-sorted, and random data).

2. **`priority_queue.py`**
   - Implements a **max-heap** based **priority queue** with operations:
     - **add_to_heap**: Insert a new task.
     - **remove_highest_priority**: Extract the highest-priority task.
     - **modify_task_priority**: Modify the priority of a task.
     - **is_heap_empty**: Check if the priority queue is empty.

---

### **How to Run the Code:**

1. **Install Python:**
   Make sure Python 3.x is installed on your machine. If not, download and install it from [python.org](https://www.python.org/).

2. Clone this repository:
    ```bash
   git clone https://github.com/nhemani33090/MSCS532_Assignment4.git
   cd MSCS532_Assignment4
   ```

3. **Run Heapsort Comparison Script:**
   - Run the script using Python:
     ```bash
     python3 heapsort_comparision.py
     ```
   - This will run the Heapsort implementation and print the comparison results between **Heapsort**, **QuickSort**, and **MergeSort**.

4. **Run Priority Queue Script:**
   - Run the script using Python:
     ```bash
     python3 priority_queue.py
     ```
   - This will test the operations of the priority queue, including adding tasks, extracting the highest-priority task, adjusting task priorities, and checking if the queue is empty.

---

### **Summary of Findings:**

- **Heapsort Algorithm Comparison:**
  - Heapsort provides an **O(n log n)** time complexity in all cases (worst, best, and average). It performs better in terms of **space complexity** compared to algorithms like QuickSort and MergeSort, which can have larger space overhead.
  - **QuickSort** generally performs faster than Heapsort and MergeSort, especially with randomly ordered data. However, QuickSort has a **O(n²)** worst-case time complexity when the pivot choice is poor (e.g., sorted or reverse-sorted input), making Heapsort a more stable choice in scenarios where the worst-case performance is critical.

- **Priority Queue:**
  - The **priority queue** implemented with a **max-heap** works efficiently, with **O(log n)** time complexity for the major operations: **add_to_heap**, **remove_highest_priority**, and **modify_task_priority**.
  - The queue is used to manage tasks with priorities and allows for efficient extraction of the highest-priority tasks.
  - **Heap-based priority queues** are preferred when **logarithmic time complexity** for insertion and extraction is essential, especially in scenarios like scheduling and task management.

---
