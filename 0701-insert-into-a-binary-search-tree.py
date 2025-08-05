from typing import Optional
from utils.bst_utils import TreeNode, build_tree, print_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root


# Example input
root_list = [4, 2, 7, 1, 3]
new_node = 5
root = build_tree(root_list)


solution = Solution()
new_root = solution.insertIntoBST(root, new_node)

print_tree(new_root)
