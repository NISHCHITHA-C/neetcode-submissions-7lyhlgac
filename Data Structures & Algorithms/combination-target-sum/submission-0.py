class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(start:int, current:List, remaining:int)-> None:
            if remaining == 0:
                result.append(current.copy())
                return
            for i in range(start, len(nums)):
                num = nums[i]
                if num > remaining:
                    break
                current.append(num)
                backtrack(i, current, remaining-num)
                current.pop()
        backtrack(0, [], target)
        return result
          
        