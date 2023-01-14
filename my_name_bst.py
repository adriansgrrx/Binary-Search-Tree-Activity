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
            name = []
            if self.left:
                name += self.left.in_order_traversal()
            name.append(self.data)
            if self.right:
                name += self.right.in_order_traversal()
            return name
            
    # pre_order_traversal(): perofrms pre order traversal of a binary tree
    def pre_order_traversal(self):
        name = [self.data]
        if self.left:
            name += self.left.pre_order_traversal()
        if self.right:
            name += self.right.pre_order_traversal()
        return name

    # post_order_traversal(): performs post order traversal of a binary tree
    def post_order_traversal(self):
        name = []
        if self.left:
            name += self.left.post_order_traversal()
        if self.right:
            name += self.right.post_order_traversal()
        name.append(self.data)
        return name

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

def build_tree(name):
    print("Building tree with these name:",name)
    root = BinarySearchTreeNode(name[0])

    for i in range(1,len(name)):
        root.add_child(name[i])
    return root

if __name__ == '__main__':
    print("Welcome to Binary Search Tree Mini-Program.\nBelow, you can see my name as data that will make up the binary search tree.\n\nHere's the commands you can use to explore my name-based binary tree.")
    while True:
        print("Commands:\n1. Search for specific letter.\n2. Display in in order traversal\n3. Display in pre order traversal\n4. Display in post order traversal\n5. Exit\n")
        user_choice = int(input(">>> "))

        my_name = ["A","D","R","I","A","N"]
        my_name_tree = build_tree(my_name)
        if user_choice == 1:
            user_letter = input("Enter a letter: ").upper()
            user_search = my_name_tree.search(user_letter)
            print(f"Is letter {user_letter} included in the list? {user_search}\n")
        elif user_choice == 2:
            in_orderT = my_name_tree.in_order_traversal()
            print(f"By in order traversal: {in_orderT}\n")



    # print("Is letter A included in the list? ", )