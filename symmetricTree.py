# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        else :
            return self.checkSymmetric(root.left, root.right)
            
    def checkSymmetric(self, left, right):
        if left == right == None:
            return True
        elif left and right and left.val == right.val:
            return self.checkSymmetric(left.left, right.right) and self.checkSymmetric(left.right, right.left)
        else :
            return False
