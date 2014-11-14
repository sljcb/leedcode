class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        comStr = strs[0]
        for str in strs:
            if len(str) == 0:
                return ''
                break
            elif len(str) < len(comStr):
                minlen = len(str)
            else:
                minlen = len(comStr)
            notequal = False
            for i in range(minlen):
                if str[i] != comStr[i]:
                    notequal = True
                    break
            if notequal == True:
                comStr = comStr[:i]
            else:
                comStr = comStr[:i+1]
        return comStr
