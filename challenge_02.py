class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

    
def test_count_leaves():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(count_leaves(root))  # Expected output: 3

    # Test Case 2: Empty tree
    empty_tree = None
    print(count_leaves(empty_tree))  # Expected output: 0

    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    print(count_leaves(single_node))  # Expected output: 1

    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    print(count_leaves(left_skewed))  # Expected output: 1

    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    print(count_leaves(perfect))  # Expected output: 4

# Very important: Call the test function to actually run it!
test_count_leaves()
