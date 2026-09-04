class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return True

        s = s.lower()
        clean = [x for x in s if x.isalnum()]
        len_c = len(clean)

        if len_c <= 1:
            return True

        for i in range(0, len_c // 2):
            if clean[i] != clean[len_c - 1 - i]:
                return False
        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))