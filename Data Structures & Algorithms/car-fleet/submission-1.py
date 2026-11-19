class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # s = d/t => t = d/s 
        times_stack : list = []
        cars = sorted(zip(position , speed) , reverse = True)
        for i in range(len(cars)) :
            remeaning_distance = target - cars[i][0]
            remeaning_time =  remeaning_distance / cars[i][1]
            if not times_stack or remeaning_time > times_stack[-1] :
                times_stack.append(remeaning_time)
            if times_stack and remeaning_time <= times_stack[-1] :
                continue       
        return len(times_stack)
