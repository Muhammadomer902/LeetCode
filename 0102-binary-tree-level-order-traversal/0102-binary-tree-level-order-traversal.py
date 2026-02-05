# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def traversal(self,arr, rootNode, level):
        if level==len(arr):
            arr.append([])
        arr[level].append(rootNode.val)
        if rootNode.left!=None:
            self.traversal(arr,rootNode.left,level+1)
        if rootNode.right!=None:
            self.traversal(arr,rootNode.right,level+1)

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        rarr = [];level = 0

        if not root:
            return rarr
        else: 
            rarr.append([])

        self.traversal(rarr,root,level)

        return rarr
