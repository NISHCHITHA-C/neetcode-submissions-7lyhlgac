class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            current = ''.join(sorted(word))
            if current in dic:
                dic[current] = dic[current] + [word]
            else:
                dic[current] = [word]
        return list(dic.values())
        
        