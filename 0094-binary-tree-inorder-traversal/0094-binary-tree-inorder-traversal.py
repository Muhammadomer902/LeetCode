# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursion(self, root, arr):
        if root:
            self.recursion(root.left,arr)
            arr.append(root.val)
        if root:
            self.recursion(root.right,arr)

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        rarr = []
        self.recursion(root,rarr)
        return rarr