# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursion(self, root, targetSum, s):
        if root and root.right==None and root.left==None and s+root.val==targetSum:
            return True

        if not root:
            return False

        return self.recursion(root.left,targetSum,s+root.val) or self.recursion(root.right,targetSum,s+root.val)

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        return self.recursion(root,targetSum,s = 0)