class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic.keys():
                dic[s[i]] = 1
            else:
                dic[s[i]] = dic.get(s[i])+1
        for i in range(len(t)):
            if t[i] not in dic.keys():
                return False
            else:
                dic[t[i]] = dic.get(t[i])-1
        print([i == 0 for i in dic.values()])
        return all([i == 0 for i in dic.values()])