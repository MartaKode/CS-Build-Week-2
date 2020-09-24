# https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # we can make a cache and keep track of every number we encounter
        # if we ran across a number that we already stored in the cache, return True
        # otherwise, no dupes in the array: return False
        
        cache = {}
        
        for num in nums:
            if num in cache:
                return True
            else:
                cache[num]= 1
        return False
        
        
        # another approach: 
        # we can take a set of our array (get rids of all the dupes)
        # if its length is less than the length of the original array: must have dupes --> will return True
        
        # return len(set(nums)) < len(nums)