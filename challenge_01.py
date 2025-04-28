class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_height(node):
    if not node:
        return -1  
    left_height = tree_height(node.left)
    right_height = tree_height(node.right)
    return max(left_height, right_height) + 1

def test_tree_height():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(tree_height(root))  # Expected output: 2

    # Test Case 2: Empty tree
    empty_tree = None
    print(tree_height(empty_tree))  # Expected output: -1

    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    print(tree_height(single_node))  # Expected output: 0

    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    print(tree_height(left_skewed))  # Expected output: 3

    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    print(tree_height(perfect))  # Expected output: 2


test_tree_height()
