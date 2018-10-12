class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.storage = [value]

    def depth_first_for_each(self, cb):
        parent_left = self.left
        parent_right = self.right
        cb(self.value)
        current = parent_left
        cb(current.value)
        # search through the left subtrees first then through the right
        while current.left is not None or current.right is not None:
            if current.left is not None:
                current = current.left
            elif current.right is not None:
                current = current.right
            cb(current.value)
        # end of the left side
        current = parent_right
        cb(current.value)
        while current.left is not None or current.right is not None:
            if current.left is not None:
                current = current.left
            elif current.right is not None:
                current = current.right
            cb(current.value)
        # end of the function

    def breadth_first_for_each(self, cb):
        # since  breadth uses the first in first out method
        # i set up a "semi" queue in the form of an array.
        # inserting the items into the array to keep their order true.
        for item in self.storage:
            cb(item)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        self.storage.append(new_tree.value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
