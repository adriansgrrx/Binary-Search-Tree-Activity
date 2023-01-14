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

    # delete method for removing an element in the tree
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # Modify delete method in class BinarySearchTreeNode class to use min element from left subtree.
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

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
    print("Building tree with these letters:", name)
    root = BinarySearchTreeNode(name[0])

    for i in range(1,len(name)):
        root.add_child(name[i])
    return root

if __name__ == '__main__':
    print("\nWelcome to Binary Search Tree Mini-Program.\nBelow, you can see my name as data that will make up the binary search tree.\n\nHere's the commands you can use to explore my name-based binary tree.")
    my_name = ["A","D","R","I","A","N"]
    my_name_tree = build_tree(my_name)
    while True:
        try:
            print("Commands:\n1. Search for specific letter.\n2. Display in in order traversal.\n3. Display in pre order traversal.\n4. Display in post order traversal.\n5. Remove an element.\n6. Exit.\n")
            user_choice = int(input(">>> "))
            if user_choice == 1:
                user_letter = input("Enter a letter: ").upper()
                user_search = my_name_tree.search(user_letter)
                print(f"Is letter {user_letter} included in the list? {user_search}\n")

            elif user_choice == 2:
                in_orderT = my_name_tree.in_order_traversal()
                print(f"By in order traversal: {in_orderT}\n")

            elif user_choice == 3:
                pre_orderT = my_name_tree.pre_order_traversal()
                print(f"By pre order traversal: {pre_orderT}\n")

            elif user_choice == 4:
                post_orderT = my_name_tree.post_order_traversal()
                print(f"By post order traversal: {post_orderT}\n")

            elif user_choice == 5:
                my_name = ["A","D","R","I","A","N"]
                my_name_tree = build_tree(my_name)
                in_orderT1 = my_name_tree.in_order_traversal()
                print(f"By in order traversal: {in_orderT1}")
                user_del = str(input("Enter the letter you want to remove: ")).upper()
                my_name_tree.delete(user_del)
                print(f"After deleting {user_del}: {my_name_tree.in_order_traversal()}\n")

            elif user_choice == 6:
                print("The program is now closed.\n")
                break
            else:
                print("[Input out of range. Try again]\n")
        except ValueError:
            print("The program only accpets integers. Try again.\n")