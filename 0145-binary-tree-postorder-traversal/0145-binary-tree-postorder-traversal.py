# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.out = [] 

    def postorderTraversal(self, root):
        if root is None:
            return
        if root.left is not None:
            self.postorderTraversal(root.left)
        if root.right is not None:
            self.postorderTraversal(root.right)
        self.out.append(root.val)
        return self.out
        
        