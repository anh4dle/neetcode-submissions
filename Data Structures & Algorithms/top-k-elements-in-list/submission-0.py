from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter (nums)
        most_common = counts.most_common()
        result = []
        for _k,v in most_common:
            if k == 0:
                return result
            result.append(_k)
            k -= 1
        print("Showing result", result)
        return result