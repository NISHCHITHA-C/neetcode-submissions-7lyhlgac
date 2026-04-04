class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            if ''.join(sorted(word)) in dic.keys():
                dic[''.join(sorted(word))] = dic[''.join(sorted(word))]+[word]
            else:
                dic[''.join(sorted(word))] = [word] 
        return list(dic.values())