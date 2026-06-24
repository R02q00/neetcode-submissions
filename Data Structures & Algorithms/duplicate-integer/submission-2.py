class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lo = 0
        hi = len(nums)
        seen = set()
        while(lo < hi):
            if nums[lo] in seen:
                return True
            seen.add(nums[lo])
            lo +=1
        return False

nums = [1,2,3,3]
solve = Solution()
print(solve.hasDuplicate(nums))
