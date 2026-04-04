class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)== 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        maximum, count = 1,1
        for i in range(1,len(nums)):
            if nums[i-1]+1 == nums[i]:
                count += 1
                maximum = max(maximum,count)
            else:
                count = 1
        return maximum