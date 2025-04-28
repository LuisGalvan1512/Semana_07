class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node:
        print(node.value)
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value)


def test_tree_traversals():
    # Test Case: Standard binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Preorder Traversal:")
    preorder_traversal(root)
    # Expected output: 1 2 4 5 3

    print("\nInorder Traversal:")
    inorder_traversal(root)
    # Expected output: 4 2 5 1 3

    print("\nPostorder Traversal:")
    postorder_traversal(root)
    # Expected output: 4 5 2 3 1

# Important: Call the test function
test_tree_traversals()
