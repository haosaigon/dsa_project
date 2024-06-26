import timeit

# Python code to insert a node in AVL tree 
  
# Generic tree node class 
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  
# AVL tree class which supports the  
# Insert operation 
class AVL_Tree(object): 
  
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
    
    # Recursive function to delete a node with
    # given key from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, key):
 
        # Step 1 - Perform standard BST delete
        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key)
 
        elif key > root.val:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                      temp.val)
 
        # If the tree has only one node,
        # simply return it
        if root is None:
            return root
 
        # Step 2 - Update the height of the 
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
    
    def search(self, root, key):

        if not root:
            return False
        
        if root.val == key:
            return True
        
        if root.val < key:
            return self.search(root.right, key)
        
        if root.val > key:
            return self.search(root.left, key)
        
        return False
    
    # Function to left rotate subtree rooted with y
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    # Function to right rotate subtree rooted with y
    def rightRotate(self, z): 
  
        y = z.left      # y is z's left child
        T3 = y.right  # T3 is y's right child
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights to reflect change in height
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
    
    def postOrder(self, root):

        if not root:
            return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print("{0} ".format(root.val), end="")

    def inOrder(self, root):

        if not root:
            return

        self.inOrder(root.left)
        print("{0} ".format(root.val), end="")
        self.inOrder(root.right) 
  
# Driver program to test above function 
myTree = AVL_Tree() 
root = None
  
root = myTree.insert(root, 5) 
root = myTree.insert(root, 1) 
root = myTree.insert(root, 4)

case = 1000


# Time complexity of insertion and search is O(log n)
insert_time = timeit.timeit(lambda: myTree.insert(root, 2), number=case)
print("Insertion time:", insert_time)

search_time = timeit.timeit(lambda: myTree.search(root, 2), number=case)
print("Search time:", search_time)

# Time complexity of deletion is O(log n)
deletion_time = timeit.timeit(lambda: myTree.delete(root, 2), number=case)
print("Deletion time:", deletion_time)

print()

# Preorder Traversal 
print("Preorder traversal of the", 
      "constructed AVL tree is") 

preorder_time = timeit.timeit(lambda: myTree.preOrder(root), number=case)
print("\nPreorder traversal time:", preorder_time)
print()

# Inorder Traversal 
print("Inorder traversal of the", 
      "constructed AVL tree is") 

inorder_time = timeit.timeit(lambda: myTree.inOrder(root), number=case)
print("\nInorder traversal time:", inorder_time)
print()

# Postorder Traversal 
print("Postorder traversal of the", 
      "constructed AVL tree is") 

postorder_time = timeit.timeit(lambda: myTree.postOrder(root), number=case)
print("\nPostorder traversal time:", postorder_time)
print()
