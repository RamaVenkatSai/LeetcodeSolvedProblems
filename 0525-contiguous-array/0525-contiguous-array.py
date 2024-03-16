class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res=0
        dict_index={}
        zero=0
        one=0
        for i,element in enumerate(nums):
            if element==0:
                zero=zero+1
            else:
                one=one+1
            if one-zero not in dict_index:
                dict_index[one-zero]=i
            if one==zero:
                res=i+1
            else:
                if one-zero in dict_index:
                    
                    res=max(res,i-dict_index[one-zero])
        return res
        