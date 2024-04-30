import timeit, random
# Define the Node class to be used in the Data Structure Libraryclass Node:

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.front is None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.data
    def peek(self):
        if self.front is None:
            return None
        else:
            return self.front.data
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False
    def is_full(self):
        return False
    def print_queue(self):
        current = self.front
        while current:
            if current.next == None:
                print(current.data, end="\n")
            else:
                print(current.data, end=" -> ")
            current = current.next


case1=10
case2 =1000
case3= 10000 

queue = Queue()
insert_time1 = timeit.timeit(lambda: queue.enqueue(10), number=case1)
insert_time2 = timeit.timeit(lambda: queue.enqueue(2), number=case2)
insert_time3 = timeit.timeit(lambda: queue.enqueue(3), number=case3)
print("Insert time 1: ", insert_time1)
print("Insert time 2: ", insert_time2)
print("Insert time 3: ", insert_time3)
print()
peek_time1 = timeit.timeit(lambda: queue.peek(), number=case1)
print("Peek time 1: ", peek_time1)
peek_time2 = timeit.timeit(lambda: queue.peek(), number=case2)
print("Peek time 2: ", peek_time2)
peek_time3 = timeit.timeit(lambda: queue.peek(), number=case3)
print("Peek time 3: ", peek_time3)
print()
empty_time1 = timeit.timeit(lambda: queue.is_empty(), number=case1)
print("Empty time 1: ", empty_time1)
empty_time2 = timeit.timeit(lambda: queue.is_empty(), number=case2)
print("Empty time 2: ", empty_time2)
empty_time3 = timeit.timeit(lambda: queue.is_empty(), number=case3)
print("Empty time 3: ", empty_time3)
print()
full_time1 = timeit.timeit(lambda: queue.is_full(), number=case1)
print("Full time 1: ", full_time1)
full_time2 = timeit.timeit(lambda: queue.is_full(), number=case2)
print("Full time 2: ", full_time2)
full_time3 = timeit.timeit(lambda: queue.is_full(), number=case3)
print("Full time 3: ", full_time3)
print()
remove_time1 = timeit.timeit(lambda: queue.dequeue(), number=case1)
print("Remove time 1: ", remove_time1)
remove_time2 = timeit.timeit(lambda: queue.dequeue(), number=case2)
print("Remove time 2: ", remove_time2)
remove_time3 = timeit.timeit(lambda: queue.dequeue(), number=case3)
print("Remove time 3: ", remove_time3)




