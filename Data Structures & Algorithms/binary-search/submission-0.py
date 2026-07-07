class Solution:
    def search(self, nums: List[int], target: int) -> int:
        import math
        low=0
        high=len(nums)-1
        while high>=low:
            mid=low+math.floor((high-low)//2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1   
        return -1             
        