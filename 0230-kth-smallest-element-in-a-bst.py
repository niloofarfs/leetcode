from typing import Optional
from utils.bst_utils import TreeNode, build_tree, print_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        sorted = []

        def traverse(node):
            if not node:
                return node

            nonlocal sorted

            traverse(node.left)
            sorted.append(node.val)
            traverse(node.right)

        traverse(root)

        return sorted[k - 1]


# Example input
root_list = [3, 1, 4, None, 2]
k = 1
root = build_tree(root_list)



solution = Solution()
smallest = solution.kthSmallest(root, k)

print(smallest)
