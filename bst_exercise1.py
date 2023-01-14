# Starting from creating a class for binary tree properties
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data: # this condition will prevent having the same child/node
            return

        if data < self.data: # this condition will put the child to the left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else: # this condition will put the child to the right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)