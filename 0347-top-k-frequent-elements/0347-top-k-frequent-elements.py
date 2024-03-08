class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict= Counter(nums)
        counter_dict=dict(sorted(counter_dict.items(), key=lambda item: -item[1]))
        m=list(counter_dict.keys())
        
        return m[0:k]