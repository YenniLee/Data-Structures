'''
insert:
    check if empty 
    if empty:
        put node here/at root
    else:
        if new < node.value:
            leftnode.insert value
        if new >= node.value:
            rightnode.insert value


get_max;
if there's a right:
    get max on right
else:
    return node.value



find:
if node.value === findvalue
    return true
else
    if find < node.value
    if node.left
        find on left node
    else 
    if node.right
        find on right node

find
     if node is none
        return false
    if node.value == findvalue 
        return true
    else if find< node.value 
        find on lefft node
        else 
         find on right node

def insert(self, value):
    if value < self:
        if self.left is None:
            self.left = BinarySearchTree(value)
        else:
            # recurse left
            self.left.insert(value)
    else: # value >= self.value
        if self.right is None:
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)

def contains(self, target): # O(logn)
    if self.value == target:
        return True
    if target < self.value:
        if self.left is None:
            return False
        else: # recurse left
            self.left.contains(target) 
    else:
        if self.right is None:
            return False
        else: # recurse right
            return self.right.contains(target)

def get_max(self): # O(logn)
    if self.right is not None:
            return self.right.get_max()
    else:
        return self.value

def for_each(self, cb): # depth-traversal goes down all of one branch first
    cb(self.value)
    if self.left:
        self.left.for_each(cb)
    if self.right:
        self.right.for_each(cb)
# Ologn


******************BFT/DFT and Queues/Stacks**********************

O(n)
Iterative BFT(breadth-first-traversal)
- create a queue
- add root to queue 
while queue is not empty
node = head of queue
DO THE THING(e.g., print, compare values, update counter, etc)
- add children of node to queue (left to right)
- pop node off queue 

Iterative DFT(depth-first-traversal)
- create a stack
- add root to stack
while stack is not empty 
node = pop top of stack
DO THE THING
- add children of the node to stack




'''