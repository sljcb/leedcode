class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex == 2:
            return [1,2,1]
        else:
            n = 3
            preRow = [1,2,1]
            while n <= rowIndex:
                preRow = [0] + preRow + [0]
                newRow = []
                for i in range(n+1):  
                    newRow = newRow + [preRow[i] + preRow[i+1]]
                preRow = newRow
                n += 1
            return newRow      
                    
