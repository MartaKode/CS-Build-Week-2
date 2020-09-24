# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search? 
        
        start = 0
        end = len(nums) -1
        
        
        while start <= end :
            mid = (start + end) // 2
            
            # check mid a s well as as end points
            if target == nums[mid] or target == nums[start] or target == nums[end]:
                return nums.index(target)
            
            # check if left side is sorted (mid is the smallest number of the right side)
            if nums[start] < nums[mid]:
                # if target is smaller than start number -- must be on the right side --> we must change the start point
                # if target is greater than mid --> must be on the right side since left is sorted (mid is the smallest number of the right side)
                if target < nums[start] or target > nums[mid]:
                    start = mid + 1
                # otherwise, target must be on the left side -- change the end point
                else:
                    end = mid - 1
                
            # otherwise, right side is sorted (mid the largest number of the left side)
            else:
                #if target is either greater than end (end must be smaller than the start number) or smaller than mid --> target must be on the left side --> must change end point
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                # otherwise, target must be on the right side --> must change start point
                else:
                    start = mid + 1
                
        # if we exist the loop, target is not in the array       
        return -1       
    