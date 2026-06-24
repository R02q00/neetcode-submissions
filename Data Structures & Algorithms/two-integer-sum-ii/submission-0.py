class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            tmp = numbers[lo] + numbers[hi]
            if tmp == target:
                return [lo + 1, hi +1]
            elif tmp < target:
                lo +=1
            else:
                hi -=1
        return []
       

Solution().twoSum([1, 2, 3, 4], 3)
