class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        #当选0块木板时
        if not k:
            return []
        #当场模板与短木板长度一致时
        if shorter == longer:
            return [shorter * k]
        #初始化res为[0, ..., 0]
        res = [0] * (k + 1)
        #构成的不同长度木板的结果必有 k + 1 个，分别为 shorter * k + (longer - shorter) * i，其中 0 <= i <= k。
        for i in range(k + 1):
            #从小到大f放入可能的排列长度
            res[i] = shorter * (k - i) + longer * i
        return res