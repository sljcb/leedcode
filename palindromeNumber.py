class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
