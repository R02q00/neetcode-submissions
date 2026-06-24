class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            curr = nums[mid]
            if curr == target:
                return mid
            elif curr > target:
                hi = mid
            else:
                lo = mid + 1
                
        return -1
nums = [5]
print(Solution().search(nums, 5))