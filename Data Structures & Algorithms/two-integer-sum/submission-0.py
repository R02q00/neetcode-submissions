class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0, len(nums)) :
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff],i]
            seen[nums[i]]= i
        return []
        
print(Solution().twoSum([3,4,5,6], 7))