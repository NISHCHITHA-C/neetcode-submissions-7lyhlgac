class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        s = ''.join([l for l in s if re.fullmatch(r'[a-z0-9]', l)])
        i, j = 0, len(s)-1
        while i<j:
            if s[i] == s[j]:
                i+=1
                j -= 1
            else:
                return False
        return True