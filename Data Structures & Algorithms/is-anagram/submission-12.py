class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sr = [0]*26
        tg= [0]*26
        for i in range(len(s)):
            sr[ord(s[i]) - ord('a')] += 1
            tg[ord(t[i]) - ord('a')] += 1
        return sr == tg