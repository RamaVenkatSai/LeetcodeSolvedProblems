class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1 for i in range(len(nums))]
        PrefixProduct=1
        for i in range(len(nums)):

            res[i]=res[i]*PrefixProduct
            PrefixProduct=PrefixProduct*nums[i]
        
        SuffixProduct=1
        for i in range(len(nums)-1,0,-1):
            SuffixProduct=SuffixProduct*nums[i]
            res[i-1]=res[i-1]*SuffixProduct
        return res
        
        