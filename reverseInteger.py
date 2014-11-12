class Solution:
    # @return an integer
    def reverse(self, x):
        if x >= 0:
            sig = 1
        else:
            sig = -1
            x = -1*x
        result = 0
        while x != 0:
            result = result * 10 + x % 10
            x = x / 10
            
        if abs(result) > 2**31-1:
            return 0
        else:
            return result * sig
