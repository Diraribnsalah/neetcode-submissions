class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # define the variables
        counter = {}
        most_frequent = []
        buckets = [[] for _ in range(len(nums) + 1)] 
        # adding any value with it's number of iterations
        for  num in nums :
            counter[num] = counter.get(num , 0) + 1
        # add each value with it's frequence in buckets list (index refrenced to freq) 
        for value , freq in counter.items() :
            buckets[freq].append(value)
        # push the values to most_frequence list 
        for i in range(len(buckets) - 1 , 0 , -1) :
            for num in buckets[i] :
                most_frequent.append(num)
                if len(most_frequent) == k :
                    print(most_frequent)
                    return most_frequent      
        

