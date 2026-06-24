class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(filter(str.isalnum, s)).lower()
        lo, hi = 0, len(cleaned) - 1
        while lo < hi:
            if cleaned[lo] != cleaned[hi]:
                return False
            lo +=1
            hi -=1
        return True

Solution().isPalindrome("Was it a car or a cat I saw?")