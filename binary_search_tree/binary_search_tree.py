import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to root
        if value < self.value:
            # if there is no child node
            if self.left is None:
                # then insert 
                self.left = BinarySearchTree(value)
            else:
                # continue left to the child node and run again
                self.left.insert(value)
        else: # if value >= self.value
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        return self.value

    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Call the function `cb` on the value of each node
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        else:
            return None

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # initialize a queue
        q = Queue()
        # add root to queue
        q.enqueue(node)
        # while queue is not empty
        while q.len() > 0:
            # remove node from queue
            traverse = q.dequeue()
            # DO THE THING
            print(traverse.value)
            # add children of node to queue
            if traverse.left:
                q.enqueue(traverse.left)
            if traverse.right:
                q.enqueue(traverse.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize a stack
        s = Stack()
        # add root to stack
        s.push(node)
        # while stack is not empty
        while s.len() > 0:
            # pop node off top of stack
            traverse = s.pop()
            # DO THE THING
            print(traverse.value)
            # add children of node to stack
            if traverse.left:
                s.push(traverse.left)
            if traverse.right:
                s.push(traverse.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # Until all nodes are traversed −
    # Step 1 − Visit root node.
    # Step 2 − Recursively traverse left subtree.
    # Step 3 − Recursively traverse right subtree.
    def pre_order_dft(self, node):
        # visit root node
        if node:
            print(node.value)
            # recurse left 
            self.pre_order_dft(node.left)
            # recurse right
            self.pre_order_dft(node.right)



    # Print Post-order recursive DFT
    # 1. Traverse the left subtree, call Postorder(left-subtree)
    # 2. Traverse the right subtree, call Postorder(right-subtree)
    # 3. Visit the root.
    def post_order_dft(self, node):
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)
        
