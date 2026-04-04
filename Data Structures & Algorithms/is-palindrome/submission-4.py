class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        s = ''.join([l for l in s if re.fullmatch(r'[a-z0-9]', l)])
        return s == s[::-1]