class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums=set(nums)
        max_counter=1
        counter=1
        for i in nums:
            if i-1 not in nums:
                j=i+1
                counter=1
                while j in nums:
                    counter=counter+1
                    j=j+1
            max_counter=max(max_counter,counter)
        return max_counter
                    
        