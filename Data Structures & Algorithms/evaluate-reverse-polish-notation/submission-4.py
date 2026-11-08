class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens :
            if s not in "+*-/" :
               stack.append(int(s))
            elif s == "+" : 
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 + val1)
            elif s == "*" :
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 * val1)
            elif s == "-" :
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif s == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
        return stack[0]       