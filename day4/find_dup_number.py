# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupes = {}
        
        for num in nums:
            if num in dupes:
                return num
            else:
                dupes[num] = 1