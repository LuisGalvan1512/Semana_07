class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror_tree(node):
    if node is None:
        return
    node.left, node.right = node.right, node.left
    mirror_tree(node.left)
    mirror_tree(node.right)

def test_mirror_tree():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    mirror_tree(root)
    print(root.left.value)  # Expected output: 3
    print(root.right.value) # Expected output: 2

    # Test Case 2: Empty tree
    empty_tree = None
    mirror_tree(empty_tree)  # Should do nothing (no error)

    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    mirror_tree(single_node)
    print(single_node.value)  # Expected output: 1

    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    mirror_tree(left_skewed)
    print(left_skewed.right.value)  # Expected output: 2
    print(left_skewed.right.right.value)  # Expected output: 3

    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    mirror_tree(perfect)
    print(perfect.left.value)  # Expected output: 3
    print(perfect.right.value) # Expected output: 2

# Important: Call the test function
test_mirror_tree()
