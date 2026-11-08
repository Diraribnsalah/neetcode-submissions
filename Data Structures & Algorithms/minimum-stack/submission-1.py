class MinStack:

    def __init__(self , stack : list = []):
        self.stack = stack 
        self.h_stack = []
    def push(self, val: int) -> None:
        if len(self.h_stack) == 0 or self.h_stack[-1] >= val :
            self.h_stack.append(val)
        self.stack.append(val)
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.h_stack[-1] :
            self.h_stack.pop()
         
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.h_stack[-1]
        
