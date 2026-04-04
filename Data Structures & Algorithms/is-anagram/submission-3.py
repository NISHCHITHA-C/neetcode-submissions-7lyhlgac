class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s)!= set(t):
            return False
        for ele in set(t):
            if s.count(ele) != t.count(ele):
                return False
        return True