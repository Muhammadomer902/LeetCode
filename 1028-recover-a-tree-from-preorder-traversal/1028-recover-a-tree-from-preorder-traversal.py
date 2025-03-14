# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        def recoverFromPreorder(self, traversal):
            stack = []  # Stack to maintain path of nodes
            i = 0
            while i < len(traversal):
                depth = 0
                while i < len(traversal) and traversal[i] == '-':
                    depth += 1
                    i += 1
                
                value = 0
                while i < len(traversal) and traversal[i].isdigit():
                    value = value * 10 + int(traversal[i])
                    i += 1
                
                node = TreeNode(value)
                
                while len(stack) > depth:
                    stack.pop()
                
                if stack:
                    if stack[-1].left is None:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                
                stack.append(node)
            
            return stack[0]  # Root of the reconstructed tree