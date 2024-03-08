from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict1=Counter(nums)
        maxer=max(dict1.values())
        counter=0
        for key,values in dict1.items():
            if values==maxer:
                counter=counter+maxer
        return counter
        