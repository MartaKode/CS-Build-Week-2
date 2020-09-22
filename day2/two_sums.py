# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        cache = {}
    
        # hash number as key and index as value 
        for i in range(len(nums)):
            cache[nums[i]] = i
        
        for i in range(len(nums)):
#             filler will be the number we need to complete the sum for each num we encounter through iteration
            filler = target - nums[i]
        
            # if filler exists in our dictionary and is not at the index of num (meanining if filler isnt the number we are currently looking at)
            if filler in cache and cache[filler] !=i:
                # return the index we are at currently and its filler index 
                return [i, cache[filler]]
        
