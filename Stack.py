import timeit, random
# Define the Node class to be used in the Data Structure Libraryclass Node:
    
class Node:    
    def __init__(self, data):
        self.data = data
        self.next = None

class StackList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        # Check if the stack is empty
        if self.top == None:
            return True  # Return True if the stack is empty
        else:
            return False  # Return False if the stack is not empty
        
        return self.top is None
    def is_full(self):  # Check if the stack is full
        # If the stack is not full
        if self.top != None:
            return False    # Return False if the stack is not full
        else:
            return True     # Return True if the stack is full
              
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def size(self):
        size = 0
        current = self.top
        while current:
            size += 1
            current = current.next
        return size

    def print_stack(self):
        current = self.top
        while current:      #current != None
            if current.next == None:
                print(current.data, end="\n")
            else:
                print(current.data, end=" -> ")
            current = current.next
        
case1=10
case2 =1000
case3= 10000   

start_time = timeit.timeit()

stacklist = StackList()

for i in range(case1):
    stacklist.push(random.randint(0, case1))
stacklist.print_stack()

end_time = timeit.timeit()

execution_time = end_time - start_time
print("Execution time in case 1:", execution_time, "seconds")


start_time = timeit.timeit()

stacklist = StackList()

for i in range(case2):
    stacklist.push(random.randint(0, case2))
stacklist.print_stack()
end_time = timeit.timeit()

execution_time = end_time - start_time
print("Execution time in case 2:", execution_time, "seconds")

start_time = timeit.timeit()

stacklist = StackList()

for i in range(case3):
    stacklist.push(random.randint(0, case3))

end_time = timeit.timeit()

execution_time = end_time - start_time
print("Execution time in case 3:", execution_time, "seconds")

stacklist = StackList()
insert_time1 = timeit.timeit(lambda: stacklist.push(random.randint(0, case1)), number=case1)
print("Insert time 1: ", insert_time1)
insert_time2 = timeit.timeit(lambda: stacklist.push(random.randint(0, case2)), number=case2)
print("Insert time 2: ", insert_time2)
insert_time3 = timeit.timeit(lambda: stacklist.push(random.randint(0, case3)), number=case3)
print("Insert time 3: ", insert_time3)
#stacklist.print_stack()


peek_time1 = timeit.timeit(lambda: stacklist.peek(), number=case1)
print("Peek time 1: ", peek_time1)
peek_time2 = timeit.timeit(lambda: stacklist.peek(), number=case2)
print("Peek time 2: ", peek_time2)
peek_time3 = timeit.timeit(lambda: stacklist.peek(), number=case3)
print("Peek time 3: ", peek_time3)

empty_time1 = timeit.timeit(lambda: stacklist.is_empty(), number=case1)
print("Empty time 1: ", empty_time1)
empty_time2 = timeit.timeit(lambda: stacklist.is_empty(), number=case2)
print("Empty time 2: ", empty_time2)
empty_time3 = timeit.timeit(lambda: stacklist.is_empty(), number=case3)
print("Empty time 3: ", empty_time3)

full_time1 = timeit.timeit(lambda: stacklist.is_full(), number=case1)
print("Full time 1: ", full_time1)
full_time2 = timeit.timeit(lambda: stacklist.is_full(), number=case2)
print("Full time 2: ", full_time2)
full_time3 = timeit.timeit(lambda: stacklist.is_full(), number=case3)
print("Full time 3: ", full_time3)

remover_time1 = timeit.timeit(lambda: stacklist.pop(), number=case1)
print("Remove time 1: ", remover_time1)
remover_time2 = timeit.timeit(lambda: stacklist.pop(), number=case2)
print("Remove time 2: ", remover_time2)
remover_time3 = timeit.timeit(lambda: stacklist.pop(), number=case3)
print("Remove time 3: ", remover_time3)





        

        