class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(nums,goal):
            if goal<0:
                return 0
            sum1=0
            l=0
            counter=0
            for r in range(len(nums)):
                sum1=sum1+nums[r]
                while sum1>goal and l<=r:
                    sum1=sum1-nums[l]
                    l+=1
                counter=counter+(r-l+1)
            return counter
        return helper(nums,goal)-helper(nums,goal-1)