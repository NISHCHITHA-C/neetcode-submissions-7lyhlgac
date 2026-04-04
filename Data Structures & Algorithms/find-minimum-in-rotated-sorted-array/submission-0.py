class Solution:
    def findMin(self, nums: List[int]) -> int:
        # low, high = 0, len(nums)-1
        # while low < high:
        #     mid = low + (high - low) //2
        #     if nums[mid] > nums[high]:
        #         low = mid + 1
        #     else:
        #         high = mid -1
        # return nums[low]
        left, right = 0, len(nums) - 1
 
        while left < right:
            mid = (left + right) // 2
 
            if nums[mid] > nums[right]:  # min is in RIGHT half
                left = mid + 1
            else:                        # min is in LEFT half (including mid)
                right = mid
 
        return nums[left]
