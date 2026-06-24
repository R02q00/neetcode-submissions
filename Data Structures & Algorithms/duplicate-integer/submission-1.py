class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lo = 0
        hi = len(nums) - 1
        arr = sorted(nums)
        while(lo < hi):
            if arr[lo] == arr[lo + 1]:
                return True
            lo +=1
        return False

nums = [1,2,3,3]
solve = Solution()
print(solve.hasDuplicate(nums))
