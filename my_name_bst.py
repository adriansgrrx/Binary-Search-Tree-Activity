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
    
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def in_order_traversal(self):
            elements = []
            if self.left:
                elements += self.left.in_order_traversal()
            elements.append(self.data)
            if self.right:
                elements += self.right.in_order_traversal()
            return elements
            
    # pre_order_traversal(): perofrms pre order traversal of a binary tree
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    # post_order_traversal(): performs post order traversal of a binary tree
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    # find_min(): finds minimum element in entire binary tree
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    # find_max(): finds maximum element in entire binary tree
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # calculate_sum(): calcualtes sum of all elements
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    my_name = ["A","D","R","I","A","N"]
    my_name_tree = build_tree(my_name)

    print("Is letter A included in the list? ", my_name_tree.search("A"))
    print("Is letter X included in the list? ", my_name_tree.search("X"))
    print("By in order traversal:",my_name_tree.in_order_traversal())