import timeit

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, current, value):
        if current is None:
            return Node(value)
        if value < current.data:
            current.left = self._insert(current.left, value)
        elif value > current.data:
            current.right = self._insert(current.right, value)
        return current

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def delete(self,value):  #with 3 cases
        # case 1: base Case
        if self.root == None:  #if tree is empty
            return self.root
        # if value is less than root value
        if value < self.root.data:
            self.root.left = self.delete(value)
        elif value > self.root.data:
            self.root.right = self.delete(value)
        else:
            # case 2 Node with only one child or no child
            if self.root.left == None:
                temp = self.root.right
                self.root = None
                return temp
            if self.root.right == None:
                temp = self.root.left
                self.root = None
                return temp
            # case 3: Node with two children
            temp = self.find_min(self.root.right) #find min in right subtree
            self.root.data = temp.data  #copy min
            self.root.right = self.delete(temp.data) #delete min

        return self.root
    def find_min(self, current):
        if current.left == None:
            return current
        else:
            return self.find_min(current.left)
        
    def _inorder(self, current):
        if current is not None:
            self._inorder(current.left)
            print(current.data)
            self._inorder(current.right)

    def inorder(self):
        self._inorder(self.root)

    def _postorder(self, current):
        if current is not None:
            self._postorder(current.left)
            self._postorder(current.right)
            print(current.data)

    def postorder(self):
        self._postorder(self.root)

    def _preorder(self, current):
        if current is not None:
            print(current.data)
            self._preorder(current.left)
            self._preorder(current.right)

    def preorder(self):
        self._preorder(self.root)

    def height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    def find_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.find_height(node.left), self.find_height(node.right))
   
    def _search(self, current, value):
        if current == None:
            return False
        elif current.data == value:
            return True
        elif value < current.data:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)

    def search(self, value):
        return self._search(self.root, value)
    
    def preorder(self, current):
        if current is not None:
            self.visit(current)
            self.preorder(current.left)
            self.preorder(current.right)

    def preprint(self):
        self.preorder(self.root)

    def visit(self, node):
        print(node.data)


# Create a BST instance
bst = BST()
case = 1000
# Insert elements into the BST
insertion_time = timeit.timeit(lambda: bst.insert(5), number=case)
print("Insertion time:", insertion_time)

# Search for an element in the BST
search_time = timeit.timeit(lambda: bst.search(5), number=case)
print("Search time:", search_time)

# Delete an element from the BST
deletion_time = timeit.timeit(lambda: bst.delete(5), number=case)
print("Deletion time:", deletion_time)

# Perform inorder traversal
inorder_time = timeit.timeit(lambda: bst.inorder(), number=case)
print("Inorder traversal time:", inorder_time)

# Perform preorder traversal
preorder_time = timeit.timeit(lambda: bst.preprint(), number=case)
print("Preorder traversal time:", preorder_time)

# Perform postorder traversal
postorder_time = timeit.timeit(lambda: bst.postorder(), number=case)
print("Postorder traversal time:", postorder_time)
