class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict= Counter(nums)
        counter_dict=dict(sorted(counter_dict.items(), key=lambda item: -item[1]))
        print(counter_dict)
        m=list(counter_dict.keys())
        print(m)
        l=[]
        
        return m[0:k]