class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minstack = []
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minstack) > 0 and self.minstack[-1][0] == x:
            self.minstack[-1][1] += 1
        elif len(self.minstack) == 0 or self.minstack[-1][0] > x:
            self.minstack.append([x, 1])

    # @return nothing
    def pop(self):
        if len(self.stack) == 0:
            return 
        if self.top() == self.getMin():
            if self.minstack[-1][1] == 1:
                self.minstack.pop()
            else:
                self.minstack[-1][1] -= 1
        self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]
        
    # @return an integer
    def getMin(self):
        return self.minstack[-1][0]
