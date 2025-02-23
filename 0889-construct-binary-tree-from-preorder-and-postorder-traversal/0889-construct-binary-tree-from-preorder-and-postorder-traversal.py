# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        # Find the index of the left child in postorder
        left_child = preorder[1]
        left_subtree_size = postorder.index(left_child) + 1
        
        # Recursively construct left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:left_subtree_size+1], postorder[:left_subtree_size])
        root.right = self.constructFromPrePost(preorder[left_subtree_size+1:], postorder[left_subtree_size:-1])
        
        return root