class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 0:
            return ""
        elif n == 1:
            return str(1)
        else:
            previousStr = self.countAndSay(n-1)
            currentStr = ''
            currentChar = previousStr[0]
            firstIndex = 0
            for i in range(len(previousStr)):
                if previousStr[i] != currentChar:
                    currentStr = currentStr + str(i - firstIndex) + currentChar
                    currentChar = previousStr[i]
                    firstIndex = i
            currentStr = currentStr + str(i - firstIndex+1) + currentChar
            return currentStr
