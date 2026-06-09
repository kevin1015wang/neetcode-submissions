# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self, root):
        if root.left is None:
            return root
        else:
            return self.findMinNode(root.left)
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                minLeftNodeVal = self.findMinNode(root.right)
                root.val = minLeftNodeVal.val
                root.right = self.deleteNode(root.right, minLeftNodeVal.val)

        return root