"""
only one set of methods for either min-heap or max-heap operations should exist at a time
In this file , we are implementing the max-heap operations
"""



import timeit, random

class Heap: 
    def __init__(self, maxsize): 
        self.maxsize = maxsize # used to initialize the heap for the first time and determines the maximum number of elements the heap can hold
        self.size = 0   # represents the current size of the heap
        self.Heap = [0]*(self.maxsize + 1)  # is an array that represents the heap structure, the 0th index is not used
        self.Heap[0] = -1 * self.maxsize  # initialize the heap with -1 * maxsize as the 0th index
        self.FRONT = 1  # initialize the front of the heap as 1

    def insert(self, element): 
        if self.size >= self.maxsize: 
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] > self.Heap[self.getParent(current)]: 
            self.Heap[current], self.Heap[self.getParent(current)] = self.Heap[self.getParent(current)], self.Heap[current]
            current = self.getParent(current)

    def getParent(self, pos):
        return pos // 2
    
    def getMax(self): 
        return self.Heap[self.FRONT]  # return the maximum element always at the root, index 1

    # remove the maximum element
    def deleteMax(self): 
        popped = self.Heap[self.FRONT]  # store the popped element equal to the maximum element
        self.Heap[self.FRONT] = self.Heap[self.size]  # replace the maximum element with the last element
        self.Heap[self.size] = 0  # delete the last element
        self.size -= 1   # decrease the size of the heap
        self.heapify(self.FRONT)  # heapify the heap to maintain the heap property
        return popped

    # reordering the elements of an array to maintain the heap property
    def heapify(self, pos):
        left_child = 2 *  pos # because the position of the array and index starts from 1
        right_child = 2 * pos + 1 # because the index starts from 1
        largest = pos
        # check if the left child is larger than the parent
        if left_child <= self.size and self.Heap[left_child] > self.Heap[largest]:
            largest = left_child
        # check if the right child is larger than the parent    
        if right_child <= self.size and self.Heap[right_child] > self.Heap[largest]:
            largest = right_child
        # if the largest is not the parent    
        if largest != pos:
            self.Heap[pos], self.Heap[largest] = self.Heap[largest], self.Heap[pos] # swap the parent and the largest
            self.heapify(largest)  # recursively heapify the heap to assign largest as the parent

    # Sort the heap
    def heapSort(self): 
        for i in range(self.size // 2, 0, -1): 
            self.heapify(i) 
        for i in range(self.size, 1, -1): 
            self.Heap[i], self.Heap[1] = self.Heap[1], self.Heap[i] 
            self.heapify(1)

case = 10000
# Create a heap
myheap=Heap(case)
for i in range(case):
    myheap.insert(random.randint(1,case))

# Time complexity of insertion and deletion is O(log n)
insert_time = timeit.timeit(lambda: myheap.insert(5), number=case)
print("Insertion time:", insert_time)

delete_time = timeit.timeit(lambda: myheap.deleteMax(), number=case)
print("Deletion time:", delete_time)

# Time complexity of sorting is O(n log n)
sort_time = timeit.timeit(lambda: myheap.heapSort(), number=case)
print("Sorting time:", sort_time)


            