class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.storage = [value]

    def depth_first_for_each(self, cb):
        # storage keeps true order.
        for item in self.storage:
            cb(item)

    def breadth_first_for_each(self, cb):

        left = self.left
        right = self.right
        cb(self.value)  # root value
        if left is not None:
            cb(left.value)  # left of root
        if right is not None:
            cb(right.value)  # right of root

        def checkLevels(node):
            left = node.left
            right = node.right
            if left is not None:
                cb(left.value)
            if right is not None:
                cb(right.value)

        checkLevels(left)
        checkLevels(right)

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
