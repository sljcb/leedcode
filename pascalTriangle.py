class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            return self.process(numRows)
    
    def process(self, numRows):
        previous_solution = self.generate(numRows-1)
        previous_row = [0] + previous_solution[-1] + [0]
        new_row = []
        i = 0
        while i < numRows:
            new_row = new_row + [previous_row[i] + previous_row[i+1]]
            i += 1
        previous_solution.append(new_row)
        return previous_solution
            
