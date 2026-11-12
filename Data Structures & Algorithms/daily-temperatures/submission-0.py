class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we use in this case the Monotonic stack Algorithm
        n = len(temperatures)
        stack = []
        results = [0]*n

        for i in range(n) :
            if not stack or temperatures[i] <= temperatures[stack[-1]] :
                stack.append(i)
            elif temperatures[i] > temperatures[stack[-1]] :
                prev_day = stack.pop()
                results[prev_day] =  i - prev_day
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    prev_day = stack.pop()
                    results[prev_day] =  i - prev_day
                stack.append(i)
        return results           
                        
            
