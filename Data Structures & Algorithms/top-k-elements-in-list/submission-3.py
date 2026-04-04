class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic ={}
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] = dic[i]+1
        res = []
        for key, value in dic.items():
            res.append([key,value])
        res = sorted(res,key = lambda x : x[1], reverse = True)
        res = [x[0] for x in res]
        return res[:k]
        