# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
            return True
        elif abs(self.findDepth(root.left)-self.findDepth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    def findDepth(self, node):
        if node == None:
            return 0
        else:
            return 1 + max(self.findDepth(node.left), self.findDepth(node.right))
