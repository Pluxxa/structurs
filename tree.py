class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def insert_left(self, current_node, value):
        """Вставляет элемент слева."""
        if current_node.left is None:
            current_node.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        """Вставляет элемент справа."""
        if current_node.right is None:
            current_node.right = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def preorder_traversal(self, start, traversal):
        """Прямой обход (pre-order) дерева."""
        if start:
            traversal.append(start.value)
            self.preorder_traversal(start.left, traversal)
            self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        """Центрированный обход (in-order) дерева."""
        if start:
            self.inorder_traversal(start.left, traversal)
            traversal.append(start.value)
            self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        """Обратный обход (post-order) дерева."""
        if start:
            self.postorder_traversal(start.left, traversal)
            self.postorder_traversal(start.right, traversal)
            traversal.append(start.value)
        return traversal

# Пример использования:
bt = BinaryTree(1)
bt.insert_left(bt.root, 2)
bt.insert_right(bt.root, 3)
bt.insert_left(bt.root.left, 4)
bt.insert_right(bt.root.left, 5)

print(bt.preorder_traversal(bt.root, []))  # [1, 2, 4, 5, 3]
print(bt.inorder_traversal(bt.root, []))  # [4, 2, 5, 1, 3]
print(bt.postorder_traversal(bt.root, []))  # [4, 5, 2, 3, 1]
