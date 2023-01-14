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

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

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
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("*******************************************************************************************************************")
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
    print("*******************************************************************************************************************")
    print("In order traversal gives this sorted list of the numbers:",numbers_tree.in_order_traversal())
    print("Pre order traversal gives this sorted list of the numbers:",numbers_tree.pre_order_traversal())
    print("Pre order traversal gives this sorted list of the numbers:",numbers_tree.pre_order_traversal())
    print("*******************************************************************************************************************")
    print("In order traversal gives this sorted list of the countries:",country_tree.in_order_traversal())
    print("Pre order traversal gives this sorted list of the countries:",country_tree.pre_order_traversal())
    print("Pre order traversal gives this sorted list of the countries:",country_tree.pre_order_traversal())
    print("*******************************************************************************************************************")
    print("Max for Number's Tree:",numbers_tree.find_max())
    print("Max for Country's Tree:",country_tree.find_max())
    print("Min for Number's Tree:",numbers_tree.find_min())
    print("Min for Country's Tree:",country_tree.find_min())
    print("Summation of the Number's Tree:",numbers_tree.calculate_sum())
    print("*******************************************************************************************************************")