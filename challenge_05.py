class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(node):
    def check_height(current):
        if current is None:
            return 0

        left_height = check_height(current.left)
        if left_height == -1:
            return -1

        right_height = check_height(current.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return check_height(node) != -1



def test_is_balanced():
    # Test Case 1: Balanced tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(is_balanced(root))  # Expected output: True

    # Test Case 2: Empty tree
    empty_tree = None
    print(is_balanced(empty_tree))  # Expected output: True

    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    print(is_balanced(single_node))  # Expected output: True

    # Test Case 4: Left-skewed tree (not balanced)
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    print(is_balanced(left_skewed))  # Expected output: False

    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    print(is_balanced(perfect))  # Expected output: True

# Important: Call the test function
test_is_balanced()
