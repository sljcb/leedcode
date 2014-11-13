class Solution:
    # @return an integer
    def romanToInt(self, s):
        romanC = ['I','V','X','L','C','D','M']
        romanN = [1,5,10,50,100,500,1000]
        result = 0
        for i in range(len(s)):
            if i == 0:
                last_num = romanN[romanC.index(s[i])]
                result = romanN[romanC.index(s[i])]
            else:
                cur_num = romanN[romanC.index(s[i])]
                if cur_num > last_num:
                   result = result + cur_num - last_num - last_num
                   last_num = cur_num
                else:
                    result = result + cur_num
                    last_num = cur_num
        return result
