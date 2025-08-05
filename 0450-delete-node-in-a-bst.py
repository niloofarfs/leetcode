from typing import Optional
from utils.bst_utils import TreeNode, build_tree, print_tree

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:

            if not root.left:
                return root.right

            if not root.right:
                return root.left
            
            
            else:

                minNodeVal = self.minNodeVal(root.right)
                root.val  = minNodeVal
                root.right = self.deleteNode(root.right, minNodeVal)
            

        return root
            
            

    def minNodeVal(self, root: TreeNode) -> int:
        while root.left:
            root = root.left

        return root.val


# Example input
root_list = [5, 3, 6, 2, 4, None, 7]
key_to_delete = 3
root = build_tree(root_list)

# root_list = [5,3,6,2,4,None,7]
# key = 0


solution = Solution()
new_root = solution.deleteNode(root, key_to_delete)

print_tree(new_root)
