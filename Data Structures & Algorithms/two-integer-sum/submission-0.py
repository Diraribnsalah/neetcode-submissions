class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        detec = {}
        for i , num in enumerate(nums) :
            diff = target - num 
            if diff in detec :
                return [detec[diff] , i]
            detec[num] = i    

    
        