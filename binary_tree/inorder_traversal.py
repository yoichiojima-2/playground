from binary_tree import TreeNode


def binary_tree() -> TreeNode:
    return TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            left=TreeNode(val=4),
            right=TreeNode(val=5, left=TreeNode(val=6), right=TreeNode(val=7)),
        ),
        right=TreeNode(val=3, right=TreeNode(val=8, left=TreeNode(val=9))),
    )


def inorder_traversal(root: TreeNode) -> list[int]:
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)


bt = binary_tree()
inorder_traversal(bt)